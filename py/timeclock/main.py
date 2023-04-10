from datetime import datetime
from typing import NoReturn, Optional
from threading import Thread, Timer, Lock
from time import sleep, time
import curses

lock = Lock()

class Scene:
    name: str = ''
    key: list = []
    def on_enter(self) -> NoReturn: pass
    def on_press(self, press_key) -> NoReturn: pass
    def on_exit(self) -> NoReturn: pass

class TimeScene(Scene):
    name: str = '时钟'
    key: list = [ord('q')]
    active: bool = True
    def output(self) -> NoReturn:
        msg = datetime.now().strftime("%a %b %d %Y %H:%M:%S")
        x = (width - len(msg)) // 2
        scr.erase()
        scr.addstr(center_y, x, msg)
        scr.refresh()
    def on_enter(self) -> NoReturn:
        self.output()
        current_time = time()
        current_timer = Timer(int(current_time) + 1 - current_time, self.timer)
        current_timer.start()
    def timer(self) -> NoReturn:
        while self.active:
            lock.acquire()
            self.output()
            lock.release()
            current_time = time()
            sleep(int(current_time) + 1 - current_time)
    def on_press(self, press_key) -> NoReturn: pass
    def on_exit(self) -> NoReturn:
        self.active = False
        lock.acquire()
        lock.release()

def delta_to_str(delta: float) -> str:
        result = f'{int(delta % 3600) // 60:0>2d}:{int(delta % 60):0>2d}.{int(delta % 1 * 100):0<2d}'
        return f'{hours:0>2d}:{result}' if (hours := int(delta) // 3600) else result
class StopWatchScene(Scene):
    name: str = '秒表'
    key: list = [ord('w')]
    active: bool = False
    start_time: float = 0
    extend_time: float = 0
    stages: list[float]
    def __init__(self):
        self.stages = []
    def delta(self, delta: float) -> NoReturn:
        msg = delta_to_str(delta)
        if num := len(self.stages):
            scr.addstr(0, (width - len(msg)) // 2, msg)
            for i in range(num):
                y = num - i
                scr.addstr(y, 0, f'{i + 1:0>2d}')
                t = self.stages[i] - self.stages[i - 1] if i else self.stages[i]
                time = delta_to_str(t)
                scr.addstr(y, (width - len(time) - 1) // 2, '+ ' + time)
                if i: time = delta_to_str(self.stages[i])
                scr.addstr(y, width - len(time) - 1, time)
        else:
            scr.addstr(center_y - 1, (width - len(msg)) // 2, msg)
    def state(self) -> NoReturn:
        msg: str
        if self.active: msg = '%  Ⅱ'
        elif self.extend_time != 0: msg = '■  ▶'
        else: msg = '▶'
        scr.addstr(center_y, (width - len(msg)) // 2, msg)
    def output(self) -> NoReturn:
        scr.erase()
        self.state()
        if self.active:
            delta = time() - self.start_time
            self.delta(delta + self.extend_time)
        else:
            self.refreshed = True
            self.delta(self.extend_time)
        scr.refresh()
    def on_enter(self) -> NoReturn:
        self.output()
    def on_press(self, press_key) -> NoReturn:
        if press_key == ord('o'):
            if not self.active and self.extend_time != 0:
                self.active = False
                self.start_time = self.extend_time = 0
                self.stages.clear()
                self.output()
                return
            if self.active:
                lock.acquire()
                self.stages.append(time() - self.start_time + self.extend_time)
                lock.release()
        elif press_key == ord('p'):
            self.refreshed = False
            if self.active:
                lock.acquire()
                self.active = False
                self.extend_time += time() - self.start_time
                self.start_time = 0
                self.output()
                lock.release()
            else:
                self.active = True
                self.start_time = time()
                self.output()
                thread = Thread(target=self.thread)
                thread.start()
    def thread(self):
        while self.active:
            lock.acquire()
            self.output()
            lock.release()
            sleep(0.04)
    def on_exit(self) -> NoReturn:
        lock.acquire()
        self.active = False
        lock.release()

def top(stdscr, types, id):
    num = len(types)
    for i in range(num):
        stdscr.addstr(0, int((width // num) * (i + 0.5)), types[i].name, curses.A_REVERSE if i != id else 0)
    stdscr.refresh()

def main(stdscr):
    global scr, width, height, center_x, center_y

    width = curses.COLS
    height = curses.LINES
    center_x = width // 2
    center_y = height // 2 - 1

    scr = curses.newwin(height - 1, width, 1, 0)
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    stdscr.bkgd(' ', curses.color_pair(1))

    curses.curs_set(False)
    curses.halfdelay(1)
    types: list[type] = [TimeScene, StopWatchScene]
    num = len(types)
    stdscr.addstr(0, 0, ' ' * width, curses.A_REVERSE)
    top(stdscr, types, 0)

    scene = types[0]()
    scene.on_enter()
    while True:
        ch = stdscr.getch()
        if ch == ord('r'):
            scene.on_exit()
            return
        if ch != -1:
            flag: bool = True
            for i in range(num):
                if ch in types[i].key:
                    if type(scene) == types[i]: break
                    scene.on_exit()
                    top(stdscr, types, i)
                    scene = types[i]()
                    scene.on_enter()
                    flag = False
                    break
            if flag: scene.on_press(ch)

curses.wrapper(main)
