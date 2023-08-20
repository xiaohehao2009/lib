from base import Screen
import curses
from math import sin, cos, pi
from time import sleep, strftime
from datetime import datetime
from threading import Lock, Thread


class TimeClock(Screen):
    name = '时钟'
    used_pairs = (
        (curses.COLOR_BLACK, curses.COLOR_WHITE),
        (curses.COLOR_YELLOW, -1),
        (curses.COLOR_RED, -1),
        (curses.COLOR_GREEN, -1)
    )
    styles = None
    clock_str = '''
          ***********
      ****    XII    ****
    **  XI            I  **
   *                       *
  * X                    II *
 *                           *
 *                           *
** IX          *         III **
 *                           *
 *                           *
  * VIII                 IV *
   *                       *
    **  VII           V  **
      ****     VI    ****
          ***********
'''
    # version 0
    # r'''
          # ***********
      # ****    XII    ****
    # **  XI           I   **
   # *               /       *
  # *  X         |  /     II  *
 # *             | /           *
 # *             |/            *
# **  IX         *        III  **
 # *              \            *
 # *               \           *
  # * VIII          \     IV  *
   # *               \       *
    # **  VII         \ V  **
      # ****     VI    ****
          # ***********
    # '''
    clock_height = 15
    clock_width = 31
    clock_radio = 15
    clock_hour_rate = 0.4
    clock_min_rate = 0.55
    clock_sec_rate = 0.65
    '''convert_table = [
        (pi/2, '|'), (pi/3, '/'), (pi/6, '-'), (0, '-'),
        (pi/6*11, '-'), (pi/3*5, '\\'), (pi/2*3, '|'),
        (pi/3*4, '/'), (pi/6*7, '-'), (pi, '-'), 
        (pi/6*5, '-'), (pi/3*2, '\\')
    ]'''

    end = False
    pad = None

    def __init__(self, scr):
        # if TimeClock.styles is None:
            # curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
            # curses.init_pair(4, curses.COLOR_YELLOW, -1)
            # curses.init_pair(5, curses.COLOR_RED, -1)
            # curses.init_pair(6, curses.COLOR_GREEN, -1)
            # TimeClock.styles = [
                # curses.color_pair(3), curses.color_pair(4),
                # curses.color_pair(5), curses.color_pair(6)
            # ]
        Screen.__init__(self, scr)
        self.lock = Lock()
        self.alloc_space()
        self.draw_clock()

    def alloc_space(self):
        if self.maxx < 33 or self.maxy < 23:
            self.clock_scr = None
            self.time_scr = self.scr.subwin(1,
                self.maxx, (self.maxy - 1) // 2, 0)
            self.mode = 1
            return
        self.mode = 0
        width = TimeClock.clock_width
        height = TimeClock.clock_height
        clock_x = (self.maxx - width) // 2
        if self.maxy > 30:
            clock_y = (self.maxy - height - 6) // 2
            time_y = clock_y + height + 3
        else:
            clock_y = 3
            time_y = clock_y + height + 2
        self.clock_scr = self.scr.derwin(height, width, clock_y, clock_x)
        self.time_scr = self.scr.derwin(1, self.maxx, time_y, 0)
        # mode:
        # 0: clock painted
        # 1: no clock painting

    def get_clock_pad(self):
        pad = curses.newpad(
            TimeClock.clock_height,
            TimeClock.clock_width)
        border_style, char_style = TimeClock.styles[0:2]
        x = y = 0
        for ch in TimeClock.clock_str[1:-1]:
            if ch == '\n' or ch == '\r':
                x = 0
                y += 1
                continue
            if ch == '*':
                pad.addch(y, x, '■', border_style)
            elif ch != ' ':
                pad.addch(y, x, ch, char_style)
            x += 1
        return pad

    def draw_clock(self):
        if self.end or self.mode == 1:
            return

        # load time
        now = datetime.now()
        hour, minute, second = now.hour, now.minute, now.second
        del now

        # self.clock_scr.erase()
        min_style, hour_style, sec_style = TimeClock.styles[1:]
        '''x = y = 0
        for ch in TimeClock.clock_str[1:-1]:
            if ch == '\n' or ch == '\r':
                x = 0
                y += 1
                continue
            if ch == '*':
                self.clock_scr.addch(y, x, '■', border_style)
            elif ch != ' ':
                self.clock_scr.addch(y, x, ch, char_style)
            x += 1'''
        if self.pad is None:
            self.pad = self.get_clock_pad()
        endy = TimeClock.clock_height - 1
        endx = TimeClock.clock_width - 1
        self.pad.overwrite(self.clock_scr, 0, 0, 0, 0, endy, endx)

        # draw clock hands
        self.draw_hand(second / 5,
            TimeClock.clock_sec_rate, sec_style)
        self.draw_hand(minute / 5 + second / 300,
            TimeClock.clock_min_rate, min_style)
        self.draw_hand(hour + minute / 60,
            TimeClock.clock_hour_rate, hour_style)

        # end drawing
        self.clock_scr.refresh()

    def draw_hand(self, time, rate, style):
        # for style, see 'version 0' comment
        rd = TimeClock.clock_radio
        start_y = rd // 2
        start_x = rd
        # rad, ch = self.__convert_table[time % 12]
        time %= 12
        block = (15 - time) % 12
        rad = block * pi / 6
        if 1.8 <= time <= 4.2 or 7.8 <= time <= 10.2:
            ch = '-'
        elif 2.5 <= block <= 3.5 or 8.5 <= block <= 9.5:
            ch = '|'
        elif 0 <= block <= 3 or 6 <= block <= 9:
            ch = '/'
        else:
            ch = '\\'
        sin_rad = sin(rad)
        cos_rad = cos(rad)
        end_y = int(-sin_rad * rd / 2 * rate) + start_y
        end_x = int(cos_rad * rd * rate) + start_x
        if end_x == start_x:
            if end_y > start_y:
                for y in range(start_y + 1, end_y + 1):
                    self.clock_scr.addch(y, end_x, ch, style)
            else:
                for y in range(start_y - 1, end_y - 1, -1):
                    self.clock_scr.addch(y, end_x, ch, style)
            return
        if end_y == start_y:
            if end_x > start_x:
                for x in range(start_x + 1, end_x + 1):
                    self.clock_scr.addch(end_y, x, ch, style)
            else:
                for x in range(start_x - 1, end_x - 1, -1):
                    self.clock_scr.addch(end_y, x, ch, style)
            return
        if 1.5 <= time <= 4.5 or 7.5 <= time <= 10.5:
            tan = (end_y - start_y) / (end_x - start_x)
            if end_x > start_x:
                for x in range(start_x + 1, end_x + 1):
                    y = tan * (x - start_x) + start_y
                    self.clock_scr.addch(round(y), x, ch, style)
            else:
                for x in range(start_x - 1, end_x - 1, -1):
                    y = tan * (x - start_x) + start_y
                    self.clock_scr.addch(round(y), x, ch, style)
        else:
            tan = (end_x - start_x) / (end_y - start_y)
            if end_y > start_y:
                for y in range(start_y + 1, end_y + 1):
                    x = tan * (y - start_y) + start_x
                    self.clock_scr.addch(y, round(x), ch, style)
            else:
                for y in range(start_y - 1, end_y - 1, -1):
                    x = tan * (y - start_y) + start_x
                    self.clock_scr.addch(y, round(x), ch, style)


    def draw_time(self):
        if self.end:
            return
        msg = strftime('%a %b %d %Y %H:%M:%S %Z')
        x = (self.maxx - len(msg)) // 2
        self.time_scr.erase()
        self.time_scr.addstr(0, x, msg)
        self.time_scr.refresh()

    def on_load(self):
        self.draw_time()
        self.draw_clock()
        Thread(target=self.target).start()

    def target(self):
        while not self.end:
            for i in range(6):
                sleep(0.16)
                if self.end:
                    return
            self.lock.acquire()
            self.draw_time()
            self.draw_clock()
            self.lock.release()

    def on_unload(self):
        self.lock.acquire()
        self.end = True
        self.scr.erase()
        self.scr.refresh()
        self.lock.release()

    def on_resize(self):
        self.lock.acquire()
        Screen.on_resize(self)
        self.alloc_space()
        self.scr.erase()
        self.scr.refresh()
        self.draw_clock()
        self.draw_time()
        self.lock.release()
