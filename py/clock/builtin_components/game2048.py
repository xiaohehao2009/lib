from base import Screen
from random import randrange, random
import curses
from threading import Thread, Lock


# constants
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
DELAY_MOVED = 30 # no refresh in time when it is 0
BORD_CH = '#' # don't use chars that uses two letters' space
S = 8 # size
W = 6 # a small block width (gte 2)
H = 3 # a small block height (gte 4)
# in the terminal, the height of a letter is twice as long as the width
def GET_RAND():
    return 2 if random() < 0.9 else 4
win_msg = 'You win!'
lose_msg = 'You lose!'
end_msg = 'Game over!'
# ↑ game over after win or the number is too big
# ↑3 don't be longer than the window
win_cond = 2048
thread_delay = 50
draw_off = False
border_off = False
keyboard_map = {
    ord('f'): LEFT, ord('F'): LEFT, curses.KEY_LEFT: LEFT,
    ord('h'): RIGHT, ord('H'): RIGHT, curses.KEY_RIGHT: RIGHT,
    ord('g'): UP, ord('G'): UP, curses.KEY_UP: UP,
    ord('v'): DOWN, ord('V'): DOWN, curses.KEY_DOWN: DOWN
}
stop_keys = { ord('m'), ord('M') }
restart_keys = { ord('s'), ord('S') }
next_keys = { ord('d'), ord('D') }
auto_keys = {
    'corner': { ord('l'), ord('L') },
    'swing': { ord('k'), ord('K') },
    'hit': { ord('j'), ord('J') }
}
# controls the key binding
# don't use qwe...iop 1234567890 and SHIFT the above


# process the constants
msg_map = {
    1: win_msg,
    2: lose_msg,
    4: end_msg
}
sup_num = 10 ** ((W - 1) * (H - 1))


class Game2048(Screen):
    name = '2048'
    used_pairs = (
        (curses.COLOR_RED, curses.COLOR_WHITE), # border style
        (curses.COLOR_GREEN, -1), # number style
        (curses.COLOR_RED, curses.COLOR_GREEN) # message style
    )
    styles = None

    pad = None
    score = 0
    max = 0
    state = 0
    # state:
    # 0: normal
    # 1: win
    # 2: lose
    # 3: after-won
    # 4: game over after-won or the number is too big
    thread = None
    lock = None
    def __init__(self, scr):
        Screen.__init__(self, scr)
        self.alloc()
        self.restart()
        self.lock = Lock()
    def alloc(self):
        # width: 25 height: 17 (when S 4 W 6 H 4 BORD_CH #)
        # #########################
        # #     #     #     #     #
        # #     #     #     #     #
        # #     #     #     #     #
        # #########################
        # #     #     #     #     #
        # #     #     #     #     #
        # #     #     #     #     #
        # #########################
        # #     #     #     #     #
        # #     #     #     #     #
        # #     #     #     #     #
        # #########################
        # #     #     #     #     #
        # #     #     #     #     #
        # #     #     #     #     #
        # #########################
        if self.can_play():
            start_x = (self.maxx - W * S - 1) // 2
            # to avoid it overlays the score
            start_y = (self.maxy - H * S) // 2
            self.subwin = self.scr.derwin(H * S + 1, W * S + 1, \
                start_y, start_x)
        else:
            self.subwin = None
    def can_play(self):
        return self.maxy >= H * S + 2 and self.maxx >= W * S + 1
    def restart(self):
        self.clear()
        self.gen_rand()
        self.score = 0
    def get_pad(self):
        pad = curses.newpad(H * S + 1, W * S + 1)
        style = Game2048.styles[0]
        for y in range(0, H * S + 1):
            if y % H == 0: # a small block height is H
                self.scr.refresh()
                # a small block width is W
                pad.addstr(y, 0, BORD_CH * (W * S), style)
                # to avoid write to the right-bottom corner
                pad.insch(y, W * S, BORD_CH, style)
                continue
            for x in range(0, W * S + 1, W):
                pad.addch(y, x, '#', style)
        return pad
    def draw_num(self, j, msg, y0):
        leng = len(msg)
        strs = []
        for i in range(0, leng, W - 1):
            strs.append(msg[i:i + W - 1])
        lengt = len(strs)
        mid = lengt // 2
        for i, seg in enumerate(strs):
            x = (W + 2 - len(seg)) // 2 + W * j
            y = y0 + i - mid
            self.subwin.addstr(y, x, seg, Game2048.styles[1])
    def draw(self):
        if not self.can_play() or draw_off:
            return
        self.scr.move(0, 0)
        self.scr.clrtoeol()
        self.scr.addstr(0, 0, f'Score: {self.score} Max: {self.max}')
        self.subwin.erase()
        if not border_off:
            if self.pad is None:
                self.pad = self.get_pad()
            self.pad.overwrite(self.subwin, 0, 0, 0, 0, H * S, W * S)
        for i, row in enumerate(self.grid):
            y = H * i + (H + 1) // 2
            # the mid y in the white space of the block
            for j, item in enumerate(row):
                if item is None:
                    continue
                self.draw_num(j, str(item), y)
        if self.state in { 1, 2, 4 }:
            msg = msg_map[self.state]
            x = (W * S + 1 - len(msg)) // 2
            self.subwin.addstr(H * S, x, msg, Game2048.styles[2])
        self.subwin.noutrefresh()
        self.scr.noutrefresh()
        curses.doupdate()
        # to optimize
    def isfull(self):
        for y in range(S):
            for x in range(S):
                if self.grid[y][x] is None:
                    return False
        return True
    def clear(self):
        self.grid = [[None for j in range(S)] for i in range(S)]
    def gen_rand(self):
        from random import randrange, random
        while True:
            y, x = randrange(0, S), randrange(0, S)
            if self.grid[y][x] is None:
                self.grid[y][x] = GET_RAND()
                break
    def islose(self):
        if not self.isfull():
            return False
        for y in range(S):
            for x in range(S - 1):
                if self.grid[y][x] == self.grid[y][x + 1] or \
                    self.grid[x][y] == self.grid[x + 1][y]:
                    return False
        return True
    def iswin(self):
        for row in self.grid:
            for item in row:
                if item is not None and item >= win_cond:
                    return True
        return False
    def issup(self):
        # if number is too big too show
        for row in self.grid:
            for item in row:
                if item is not None and item >= sup_num:
                    return True
        return False
    def move(self, direction):
        if not self.can_play or self.state != 0 and self.state != 3:
            return False
        flag = False
        if direction == LEFT:
            for y in range(S):
                for x in range(1, S):
                    if self.move_one(y, x, direction):
                        if not flag:
                            flag = True
                        if DELAY_MOVED > 0:
                            self.draw()
                            curses.napms(DELAY_MOVED)
        elif direction == RIGHT:
            for y in range(S):
                for x in range(S - 1, -1, -1):
                    if self.move_one(y, x, direction):
                        if not flag:
                            flag = True
                        if DELAY_MOVED > 0:
                            self.draw()
                            curses.napms(DELAY_MOVED)
        elif direction == UP:
            for x in range(S):
                for y in range(1, S):
                    if self.move_one(y, x, direction):
                        if not flag:
                            flag = True
                        if DELAY_MOVED > 0:
                            self.draw()
                            curses.napms(DELAY_MOVED)
        elif direction == DOWN:
            for x in range(S):
                for y in range(S - 1, -1, -1):
                    if self.move_one(y, x, direction):
                        if not flag:
                            flag = True
                        if DELAY_MOVED > 0:
                            self.draw()
                            curses.napms(DELAY_MOVED)
        if not flag:
            return False
        self.gen_rand()
        if self.issup():
            self.state = 4
            self.draw()
            return None
        if self.islose():
            self.state = 2 if self.state == 0 else 4
        elif self.state == 0 and self.iswin():
            self.state = 1
        self.draw()
        return True
    def move_one(self, y0, x0, direction):
        if self.grid[y0][x0] is None:
            return False
        if direction == LEFT:
            row = self.grid[y0]
            val0 = row[x0]
            pos = x0
            for x in range(x0 - 1, -1, -1):
                if row[x] is None:
                    pos = x
                else:
                    break
            # if pos == x0:
                # return
            if pos == 0:
                if pos == x0:
                    return False
                row[x0] = None
                row[pos] = val0
            else:
                val = row[pos - 1]
                if val == val0:
                    row[x0] = None
                    row[pos - 1] = self.update_score(val0 + val)
                elif pos == x0:
                    return False
                else:
                    row[x0] = None
                    row[pos] = val0
        elif direction == RIGHT:
            row = self.grid[y0]
            val0 = row[x0]
            pos = x0
            for x in range(x0 + 1, S):
                if row[x] is None:
                    pos = x
                else:
                    break
            # if pos == x0:
                # return
            if pos == S - 1:
                if pos == x0:
                    return False
                row[x0] = None
                row[pos] = val0
            else:
                val = row[pos + 1]
                if val == val0:
                    row[x0] = None
                    row[pos + 1] = self.update_score(val0 + val)
                elif pos == x0:
                    return False
                else:
                    row[x0] = None
                    row[pos] = val0
        elif direction == UP:
            val0 = self.grid[y0][x0]
            pos = y0
            for y in range(y0 - 1, -1, -1):
                if self.grid[y][x0] is None:
                    pos = y
                else:
                    break
            # if pos == y0:
                # return
            if pos == 0:
                if pos == y0:
                    return False
                self.grid[y0][x0] = None
                self.grid[pos][x0] = val0
            else:
                val = self.grid[pos - 1][x0]
                if val == val0:
                    self.grid[y0][x0] = None
                    self.grid[pos - 1][x0] = self.update_score(val0 + val)
                elif pos == y0:
                    return False
                else:
                    self.grid[y0][x0] = None
                    self.grid[pos][x0] = val0
        elif direction == DOWN:
            val0 = self.grid[y0][x0]
            pos = y0
            for y in range(y0 + 1, S):
                if self.grid[y][x0] is None:
                    pos = y
                else:
                    break
            # if pos == y0:
                # return
            if pos == S - 1:
                if pos == y0:
                    return False
                self.grid[y0][x0] = None
                self.grid[pos][x0] = val0
            else:
                val = self.grid[pos + 1][x0]
                if val == val0:
                    self.grid[y0][x0] = None
                    self.grid[pos + 1][x0] = self.update_score(val0 + val)
                elif pos == y0:
                    return False
                else:
                    self.grid[y0][x0] = None
                    self.grid[pos][x0] = val0
        return True
    def update_score(self, score):
        self.score += score
        if self.score > self.max:
            self.max = self.score
        return score
    def on_load(self):
        self.draw()
        self.strong_draw()
    def on_unload(self):
        if self.thread is not None:
            self.lock.acquire()
        self.scr.erase()
        self.scr.refresh()
        if self.thread is not None:
            thread = self.thread
            self.thread = None
            self.lock.release()
            thread.join()
    def on_press(self, key):
        if not self.can_play():
            return
        if self.thread is not None:
            if key in stop_keys:
                self.lock.acquire()
                thread = self.thread
                self.thread = None
                self.lock.release()
                thread.join()
            return
        if (self.state == 0 or self.state == 3) and key in keyboard_map:
            self.move(keyboard_map[key])
            # move does automatic draw
            self.strong_draw()
        elif key in restart_keys:
            self.restart()
            self.state = 0
            self.draw()
            self.strong_draw()
        elif key in next_keys:
            if self.state != 1:
                return
            self.state = 3
            self.draw()
            self.strong_draw()
        elif key in auto_keys['corner']:
            if self.state == 0 or self.state == 3:
                self.thread = Thread(target=self.corner_target)
                self.thread.start()
        elif key in auto_keys['swing']:
            if self.state == 0 or self.state == 3:
                self.thread = Thread(target=self.swing_target)
                self.thread.start()
        elif key in auto_keys['hit']:
            if self.state == 0 or self.state == 3:
                self.thread = Thread(target=self.hit_target)
                self.thread.start()
    def on_resize(self):
        if self.thread is not None:
            self.lock.acquire()
        Screen.on_resize(self)
        self.alloc()
        self.scr.erase()
        if not self.can_play():
            self.scr.refresh()
            if self.thread is not None:
                thread = self.thread
                self.thread = None
                self.lock.release()
                thread.join()
            return
        self.draw()
        if self.thread is not None:
            self.lock.release()
    def corner_target(self):
        st = 0
        # 0: next is RIGHT
        # 1: next is UP
        # 2: RIGHT failed, try UP
        # 3: UP failed, try RIGHT
        while self.thread is not None and self.can_play():
            if self.state != 0 and self.state != 3:
                self.thread = None
                break
            if thread_delay > 0:
                curses.napms(thread_delay)
            self.lock.acquire()
            if st == 0:
                res = self.move(RIGHT)
                if res == False:
                    st = 2
                    self.lock.release()
                    continue
                if res == None:
                    self.thread = None
                    self.lock.release()
                    break
                st = 1
                self.lock.release()
                continue
            if st == 1:
                res = self.move(UP)
                if res == False:
                    st = 3
                    self.lock.release()
                    continue
                if res == None:
                    self.thread = None
                    self.lock.release()
                    break
                st = 0
                self.lock.release()
                continue
            if st == 2:
                res = self.move(UP)
                if res == False:
                    self.move(LEFT)
                    st = 0
                    self.lock.release()
                    continue
                if res == None:
                    self.thread = None
                    self.lock.release()
                    break
                st = 0
                self.lock.release()
                continue
            if st == 3:
                res = self.move(RIGHT)
                if res == False:
                    self.move(DOWN)
                    st = 1
                    self.lock.release()
                    continue
                if res == None:
                    self.thread = None
                    self.lock.release()
                    break
                st = 1
                self.lock.release()
                continue
        self.strong_draw()
    def strong_draw(self):
        global draw_off
        if not draw_off:
            return
        draw_off = False
        self.draw()
        draw_off = True
    def swing_target(self):
        st = 0
        direction_table = [LEFT, DOWN, RIGHT, UP]
        while self.thread is not None and self.can_play():
            if self.state != 0 and self.state != 3:
                self.thread = None
                break
            if thread_delay > 0:
                curses.napms(thread_delay)
            self.lock.acquire()
            res = self.move(direction_table[st])
            if res is None:
                self.thread = None
                break
            st += 1
            if st == 4:
                st = 0
            self.lock.release()
        self.strong_draw()
    def hit_target(self):
        st = 0
        direction_table = [LEFT, RIGHT, UP, DOWN]
        while self.thread is not None and self.can_play():
            if self.state != 0 and self.state != 3:
                self.thread = None
                break
            if thread_delay > 0:
                curses.napms(thread_delay)
            self.lock.acquire()
            res = self.move(direction_table[st])
            if res == None:
                self.thread = None
                self.lock.release()
                break
            if res == False:
                st = (st + 2) % 4
                self.lock.release()
                continue
            if st % 2 == 0:
                st += 1
            else:
                st -= 1
            self.lock.release()
        self.strong_draw()

export = Game2048
