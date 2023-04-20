from datetime import datetime
from threading import Thread, Timer, Lock
from time import time, strftime, sleep
import curses

lock = Lock()

class Scene:
    name = ''
    key = []
    def on_enter(self): pass
    def on_press(self, press_key): pass
    def on_exit(self): pass

class TimeScene(Scene):
    name = '时钟'
    key = [ord('q'), ord('Q')]
    active = True
    def output(self):
        msg = strftime("%a %b %d %Y %H:%M:%S")
        x = (width - len(msg)) // 2
        scr.erase()
        scr.addstr(center_y, x, msg)
        scr.refresh()
    def on_enter(self):
        self.output()
        current_time = time()
        current_timer = Timer(int(current_time) + 1 - current_time, self.timer)
        current_timer.start()
    def timer(self):
        while self.active:
            lock.acquire()
            self.output()
            lock.release()
            current_time = time()
            sleep(int(current_time) + 1 - current_time)
    def on_press(self, press_key): pass
    def on_exit(self):
        self.active = False
        lock.acquire()
        lock.release()

class StopWatchScene(Scene):
    name = '秒表'
    key = [ord('w'), ord('W')]
    pause_key = [ord('p'), ord('P')]
    stage_key = [ord('o'), ord('O')]
    active = False
    start_time = 0
    extend_time = 0
    @staticmethod
    def delta_to_str(delta):
        result = f'{int(delta % 3600) // 60:0>2d}:{int(delta % 60):0>2d}.{int(delta % 1 * 100):0<2d}'
        return f'{hours:0>2d}:{result}' if (hours := int(delta) // 3600) else result
    def delta(self, delta):
        msg = self.delta_to_str(delta)
        if num := len(self.stages):
            self.win.addstr(0, (width - len(msg)) // 2, msg)
            for i in range(num):
                y = num - i
                self.win.addstr(y, 0, f'{i + 1:0>2d}')
                t = self.stages[i] - self.stages[i - 1] if i else self.stages[i]
                time = self.delta_to_str(t)
                self.win.addstr(y, (width - len(time) - 1) // 2, '+ ' + time)
                if i: time = self.delta_to_str(self.stages[i])
                self.win.addstr(y, width - len(time) - 1, time)
        else:
            self.win.addstr(center_y - 1, (width - len(msg)) // 2, msg)
    def state(self):
        if self.active: msg = '%    Ⅱ'
        elif self.extend_time != 0: msg = '■    ▶'
        else: msg = '▶'
        self.win.addstr(center_y, (width - len(msg)) // 2, msg)
    def output(self):
        self.win.erase()
        self.state()
        if self.active:
            delta = time() - self.start_time
            self.delta(delta + self.extend_time)
        else:
            self.refreshed = True
            self.delta(self.extend_time)
        self.win.refresh()
    @staticmethod
    def keys_to_cmd(keys, to):
        return f'Press {", ".join([f"<{chr(i)}>" for i in keys[:-1]])} or <{chr(keys[-1])}> to {to}'
    def on_enter(self):
        self.stages = []
        self.win = scr.subwin(height - 3, width, 1, 0)
        scr.addstr(height - 3, 0, self.keys_to_cmd(self.pause_key, 'start or pause'))
        scr.addstr(height - 2, 0, self.keys_to_cmd(self.stage_key, 'add stages or close'))
        scr.refresh()
        self.output()
    def on_press(self, press_key):
        if press_key in self.stage_key:
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
        elif press_key in self.pause_key:
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
        elif press_key == curses.KEY_MOUSE:
            try:
                _, x, y, _, n = curses.getmouse()
                if abs(y - center_y) <= 3:
                    if self.active or self.extend_time != 0:
                        if abs(x - (width - 6) // 2 + 1) <= 3:
                            self.on_press(self.stage_key[0])
                        elif abs(x - (width - 6) // 2 - 6) <= 3:
                            self.on_press(self.pause_key[0])
                    else:
                        if abs(x - center_x) <= 5:
                            self.on_press(self.pause_key[0])
            except: pass
    def thread(self):
        while self.active:
            lock.acquire()
            self.output()
            lock.release()
            curses.napms(17)
    def on_exit(self):
        lock.acquire()
        self.active = False
        lock.release()

def top(stdscr, types, id):
    num = len(types)
    for i in range(num):
        stdscr.addstr(0, int((width // num) * (i + 0.5)), types[i].name, curses.A_REVERSE if i != id else curses.A_NORMAL)
    stdscr.refresh()

def main(stdscr):
    global scr, width, height, center_x, center_y

    width = curses.COLS
    height = curses.LINES
    center_x = width // 2
    center_y = height // 2 - 1
    exit_key = [ord('r'), ord('R')]

    scr = curses.newwin(height - 1, width, 1, 0)
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    stdscr.bkgd(' ', curses.color_pair(1))

    curses.curs_set(False)
    stdscr.timeout(17)
    curses.mouseinterval(50)
    curses.mousemask(1)
    types = [TimeScene, StopWatchScene]
    num = len(types)
    stdscr.addstr(0, 0, ' ' * width, curses.A_REVERSE)
    top(stdscr, types, 0)

    scene = types[0]()
    scene.on_enter()
    while True:
        ch = stdscr.getch()
        if ch in exit_key:
            scene.on_exit()
            return
        if ch != -1:
            flag = True
            for i in range(num):
                if ch in types[i].key:
                    if type(scene) == types[i]: break
                    scene.on_exit()
                    top(stdscr, types, i)
                    scr.erase()
                    scr.refresh()
                    scene = types[i]()
                    scene.on_enter()
                    flag = False
                    break
            if flag: scene.on_press(ch)

curses.wrapper(main)
