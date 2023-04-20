from threading import Thread, Timer, Lock
from time import time, strftime, sleep
import curses

lock = Lock()

class Scene:
    name = ''
    key = []

    def on_enter(self):
        pass

    def on_press(self, press_key):
        pass

    def on_exit(self):
        pass

    def on_mouse(self, mouse):
        pass

class TimeScene(Scene):
    name = '时钟'
    key = [ord('q'), ord('Q')]
    active = True

    def output(self):
        msg = strftime("%a %b %d %Y %H:%M:%S")
        x = (width - len(msg)) // 2 - 1
        scr.erase()
        scr.addstr(center_y, x, msg)
        scr.refresh()

    def on_enter(self):
        self.output()
        current_time = time()
        Timer(int(current_time) + 1 - current_time, self.timer).start()

    def timer(self):
        while self.active:
            lock.acquire()
            self.output()
            lock.release()
            current_time = time()
            sleep(int(current_time) + 1 - current_time)

    def on_exit(self):
        lock.acquire()
        self.active = False
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
        result = f'{int(delta % 3600) // 60:0>2d}:\
{int(delta % 60):0>2d}.{int(delta % 1 * 100):0<2d}'
        return f'{hours:0>2d}:{result}' \
            if (hours := int(delta) // 3600) else result

    def delta(self, delta):
        msg = self.delta_to_str(delta)
        if num := len(self.stages):
            scr.addstr(0, (width - len(msg)) // 2 - 1, msg)
            for i in range(num):
                y = num - i
                scr.addstr(y, 0, f'{i + 1:0>2d}')
                t = ((self.stages[i] - self.stages[i - 1])
                    if i else self.stages[i])
                time = self.delta_to_str(t)
                scr.addstr(y, (width - len(time) - 1) // 2, '+ ' + time)
                if i: time = self.delta_to_str(self.stages[i])
                scr.addstr(y, width - len(time) - 1, time)
        else:
            scr.addstr(center_y - 1, (width - len(msg)) // 2 - 1, msg)

    def state(self):
        if self.active:
            scr.addstr(self.state_y, self.left_x, '+')
            scr.addstr(self.state_y, self.right_x, 'Ⅱ')
        elif self.extend_time != 0:
            scr.addstr(self.state_y, self.left_x, '■')
            scr.addstr(self.state_y, self.right_x, '▶')
        else:
            scr.addstr(self.state_y, center_x - 1, '▶')

    def output(self):
        scr.erase()
        self.state()
        if self.active:
            delta = time() - self.start_time
            self.delta(delta + self.extend_time)
        else:
            self.refreshed = True
            self.delta(self.extend_time)
        scr.refresh()

    def on_enter(self):
        self.stages = []
        self.state_y = center_y + 1
        self.left_x = center_x - 4
        self.right_x = center_x + 2
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
                self.stages.append(
                    time() - self.start_time + self.extend_time)
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

    def on_mouse(self, mouse):
        _, x, y, _, n = mouse
        if abs(y - self.state_y - 1) <= 3:
            if self.active or self.extend_time != 0:
                if abs(x - self.left_x + 1) <= 4:
                    self.on_press(self.stage_key[0])
                elif abs(x - self.right_x - 1) <= 4:
                    self.on_press(self.pause_key[0])
            else:
                if abs(x - center_x) <= 6:
                    self.on_press(self.pause_key[0])

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

def top(stdscr, types, pos, id):
    num = len(types)
    for i in range(num):
        stdscr.addstr(0, pos[i], types[i].name,
            curses.A_REVERSE if i != id else curses.A_NORMAL)
    stdscr.refresh()

def switch(scene, stdscr, types, pos, i):
    if type(scene) == types[i]: return scene
    scene.on_exit()
    top(stdscr, types, pos, i)
    scr.erase()
    scr.refresh()
    new = types[i]()
    new.on_enter()
    return new

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
    stdscr.timeout(50)
    curses.mouseinterval(50)
    curses.mousemask(curses.BUTTON1_PRESSED)
    types = [TimeScene, StopWatchScene]
    num = len(types)
    pos = [(int(width // num * (i + 0.5)) - 1) for i in range(num)]
    stdscr.addstr(0, 0, ' ' * width, curses.A_REVERSE)
    top(stdscr, types, pos, 0)

    scene = types[0]()
    scene.on_enter()
    while True:
        ch = stdscr.getch()
        if ch in exit_key:
            scene.on_exit()
            return
        if ch != curses.ERR:
            if ch == curses.KEY_MOUSE:
                flag = True
                mouse = None
                try:
                    mouse = curses.getmouse()
                    _, x, y, _, _ = mouse
                    if y <= 2:
                        for i in range(num):
                            if abs(x - pos[i]) <= 3:
                                scene = switch(scene, stdscr, types, pos, i)
                                flag = False
                                break
                    if flag:
                        scene.on_mouse(mouse)
                except:
                    if mouse != None:
                        scene.on_mouse(mouse)
            else:
                flag = True
                for i in range(num):
                    if ch in types[i].key:
                        scene = switch(scene, stdscr, types, pos, i)
                        flag = False
                        break
                if flag:
                    scene.on_press(ch)

if __name__ == '__main__':
    curses.wrapper(main)
