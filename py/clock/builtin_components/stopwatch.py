from base import Screen
import curses
from time import time
from threading import Lock, Thread


class StopWatch(Screen):
    name = '秒表'
    used_pairs = (
        (curses.COLOR_YELLOW, -1),
    )
    styles = None

    state = 0
    # state:
    # 0: Unstarted
    # 1: Started
    # 2: Started but paused

    # time at start stopwatching
    last_time = None
    cached_time = 0.0
    # to set the thread to end
    end_flag = False
    # to set the component to end
    end = False
    # the thread
    thread = None

    def __init__(self, scr):
        Screen.__init__(self, scr)
        self.lock = Lock()
        self.ticks = []
        # if StopWatch.style is None:
            # curses.init_pair(2, curses.COLOR_YELLOW, -1)
            # StopWatch.style = curses.color_pair(2)

    def format(self, time):
        mins = int(time % 3600 / 60)
        secs = int(time % 60)
        dots = int(time * 100) % 100
        msg = f'{mins:0>2}:{secs:0>2}.{dots:0<2}'
        if time >= 3600:
            hours = int(time / 3600)
            return f'{hours:0>2}:{msg}'
        return msg

    def get_midx(self, length=1):
        return (self.maxx - length) // 2
    def get_leftx(self):
        return (self.maxx - 1) // 2 - 2
    def get_rightx(self):
        return (self.maxx - 1) // 2 + 2

    def draw_btns(self, y):
        # to draw buttons
        if self.state == 1:
            self.scr.addstr(y, self.get_leftx(), 'Ⅱ')
            self.scr.addstr(y, self.get_rightx(), '●︎')
            return
        if self.state == 0:
            self.scr.addstr(y, self.get_midx(), '▶')
            return
        self.scr.addstr(y, self.get_leftx(), '▶')
        self.scr.addstr(y, self.get_rightx(), '■︎')

    def get_curr_time(self):
        if self.state == 1:
            return time() - self.last_time + self.cached_time
        if self.state == 0:
            return 0.
        return self.cached_time

    def draw(self):
        self.scr.erase()
        msg = self.format(self.get_curr_time())
        y = self.get_time_y()
        x = self.get_midx(len(msg))
        self.draw_tick_list()
        self.draw_btns(y + 2)
        self.scr.addstr(y, x, msg)
        self.scr.refresh()

    def get_tick_list_max_length(self):
        return min(self.maxy // 3 * 2, 99)

    def draw_tick_list(self):
        length = min(len(self.ticks), self.get_tick_list_max_length())
        if length == 0:
            return
        for i in range(length):
            if length >= 10:
                id = f'#{i + 1:0>2}'
            else:
                id = f'#{i + 1}'
            y = length - i - 1
            total_tick = self.ticks[i]
            total_time = self.format(total_tick)
            if i != 0:
                append_tick = total_tick - self.ticks[i - 1]
                append_time = f'+{self.format(append_tick)}'
            else:
                append_time = f'+{total_time}'
            midx = self.get_midx(len(append_time))
            endx = self.maxx - len(total_time)
            style = StopWatch.styles[0]
            self.scr.addstr(y, 0, id, style)
            self.scr.addstr(y, midx, append_time, style)
            self.scr.addstr(y, endx, total_time, curses.A_STANDOUT)

    def get_time_y(self):
        length = min(len(self.ticks), self.get_tick_list_max_length())
        y = self.maxy // 2 - 1
        if length >= y:
            y = length + 1
        return y

    def on_load(self):
        self.draw()

    def on_unload(self):
        if self.state == 1:
            self.lock.acquire()
            self.end_flag = True
            self.scr.erase()
            self.scr.refresh()
            self.end = True
            self.lock.release()
            if self.thread is not None:
                self.thread.join()
                self.thread = None
            return
        self.scr.erase()
        self.scr.refresh()

    def target(self):
        self.last_time = time()
        while not self.end_flag:
            curses.napms(34)
            self.lock.acquire()
            if self.end_flag:
                self.lock.release()
                break
            self.draw()
            self.lock.release()
        if self.end:
            return
        if self.state == 2:
            self.cached_time += time() - self.last_time
        else:
            self.cached_time = 0.0
        self.draw()
        self.end_flag = False

    def switch(self, btn=0):
        if self.state == 0:
            # only one btn
            if btn == 1:
                return
            # do start
            self.state = 1
            self.thread = Thread(target=self.target)
            self.thread.start()
            return
        if self.state == 1:
            if btn == 0:
                # do pause
                self.lock.acquire()
                self.end_flag = True
                self.state = 2
                self.lock.release()
                self.thread.join()
                self.thread = None
                return
            # do tick
            num = len(self.ticks)
            if num > self.get_tick_list_max_length():
                return
            self.lock.acquire()
            self.ticks.append(self.cached_time + (time() - self.last_time))
            self.lock.release()
            return
        if btn == 0:
            # do start
            self.state = 1
            self.thread = Thread(target=self.target)
            self.thread.start()
            return
        # do close
        self.state = 0
        self.cached_time = 0.0
        self.last_time = None
        self.ticks.clear()
        self.draw()

    def on_press(self, key):
        if key == ord('f') or key == ord('F'):
            self.switch(0)
        elif key == ord('h') or key == ord('H'):
            self.switch(1)

    def on_resize(self):
        if self.state != 1:
            Screen.on_resize(self)
            self.draw()
            return
        self.lock.acquire()
        Screen.on_resize(self)
        self.lock.release()

    def on_mouse(self, y, x):
        my = self.get_time_y() + 2
        rg = max(min(self.maxx, self.maxy) // 30, 2)
        if abs(y - my) > rg:
            return
        if self.state == 0:
            if abs(x - self.get_midx()) <= rg:
                self.switch(0)
            return
        lx = self.get_leftx()
        rx = self.get_rightx() + 1
        # because the charactor uses two letters' space in terminal
        if abs(x - lx) <= rg:
            self.switch(0)
            return
        if abs(x - rx) <= rg:
            self.switch(1)

export = StopWatch
