from base import Screen
import curses

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
DELAY_MOVED = 25

keyboard_map = {
    ord('f'): LEFT, ord('F'): LEFT, curses.KEY_LEFT: LEFT,
    ord('h'): RIGHT, ord('H'): RIGHT, curses.KEY_RIGHT: RIGHT,
    ord('g'): UP, ord('G'): UP, curses.KEY_UP: UP,
    ord('v'): DOWN, ord('V'): DOWN, curses.KEY_DOWN: DOWN
}

class Game2048(Screen):
    name = '2048'
    used_pairs = (
        (curses.COLOR_RED, curses.COLOR_WHITE),
        (curses.COLOR_GREEN, -1),
        (curses.COLOR_RED, curses.COLOR_GREEN)
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
    # 4: lost after-won
    def __init__(self, scr):
        Screen.__init__(self, scr)
        self.alloc()
        self.restart()
    def alloc(self):
        # width: 25 height: 17
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
            start_x = (self.maxx - 25) // 2
            start_y = (self.maxy - 16) // 2
            self.subwin = self.scr.derwin(17, 25, start_y, start_x)
        else:
            self.subwin = None
    def can_play(self):
        return self.maxy >= 18 and self.maxx >= 25
    def restart(self):
        self.clear()
        self.gen_rand()
        self.score = 0
    def get_pad(self):
        pad = curses.newpad(17, 25)
        style = Game2048.styles[0]
        for y in range(0, 17):
            if y % 4 == 0:
                self.scr.refresh()
                pad.addstr(y, 0, '#' * 24, style)
                # to avoid write to the right-bottom corner
                pad.insch(y, 24, '#', style)
                continue
            for x in range(0, 25, 6):
                pad.addch(y, x, '#', style)
        return pad
    def draw_num(self, j, msg, y):
        leng = len(msg)
        if leng < 6:
            x = 6 * j + 3 - leng // 2
            self.subwin.addstr(y, x, msg, Game2048.styles[1])
            return
        if leng < 11:
            len1 = leng // 2
            msg1 = msg[:len1]
            msg2 = msg[len1:]
            self.draw_num(j, msg1, y - 1)
            self.draw_num(j, msg2, y)
            return
        len1 = leng // 3
        msg1 = msg[:len1]
        msg2 = msg[len1:]
        self.draw_num(j, msg1, y - 1)
        self.draw_num(j, msg2, y + 1)
    def draw(self):
        if not self.can_play():
            return
        self.scr.addstr(0, 0, f'Score: {self.score} Max: {self.max}')
        self.subwin.erase()
        if self.pad is None:
            self.pad = self.get_pad()
        self.pad.overwrite(self.subwin, 0, 0, 0, 0, 16, 24)
        for i, row in enumerate(self.grid):
            y = 4 * i + 2
            for j, item in enumerate(row):
                if item is None:
                    continue
                self.draw_num(j, str(item), y)
        if self.state == 1:
            msg = 'You win!'
            x = (25 - len(msg)) // 2
            self.subwin.addstr(8, x, msg, Game2048.styles[2])
        elif self.state == 2:
            msg = 'You lose!'
            x = (25 - len(msg)) // 2
            self.subwin.addstr(8, x, msg, Game2048.styles[2])
        elif self.state == 4:
            msg = 'Game over!'
            x = (25 - len(msg)) // 2
            self.subwin.addstr(8, x, msg, Game2048.styles[2])
        self.subwin.noutrefresh()
        self.scr.noutrefresh()
        curses.doupdate()
    def isfull(self):
        for y in range(4):
            for x in range(4):
                if self.grid[y][x] is None:
                    return False
        return True
    def clear(self):
        self.grid = [[None, None, None, None] for i in range(4)]
    def gen_rand(self):
        from random import randrange, random
        while True:
            y, x = randrange(0, 4), randrange(0, 4)
            if self.grid[y][x] is None:
                self.grid[y][x] = 2 if random() < 0.9 else 4
                break
    def islose(self):
        if not self.isfull():
            return False
        for y in range(4):
            for x in range(3):
                if self.grid[y][x] == self.grid[y][x + 1] or \
                    self.grid[x][y] == self.grid[x + 1][y]:
                    return False
        return True
    def iswin(self):
        for row in self.grid:
            for item in row:
                if item is not None and item >= 2048:
                    return True
        return False
    def move(self, direction):
        if not self.can_play or self.state != 0 and self.state != 3:
            return
        flag = False
        if direction == LEFT:
            for y in range(4):
                for x in range(1, 4):
                    if self.move_one(y, x, direction):
                        if not flag:
                            flag = True
                        self.draw()
                        if DELAY_MOVED > 0:
                            curses.napms(DELAY_MOVED)
        elif direction == RIGHT:
            for y in range(4):
                for x in range(3, -1, -1):
                    if self.move_one(y, x, direction):
                        if not flag:
                            flag = True
                        self.draw()
                        if DELAY_MOVED > 0:
                            curses.napms(DELAY_MOVED)
        elif direction == UP:
            for x in range(4):
                for y in range(1, 4):
                    if self.move_one(y, x, direction):
                        if not flag:
                            flag = True
                        self.draw()
                        if DELAY_MOVED > 0:
                            curses.napms(DELAY_MOVED)
        elif direction == DOWN:
            for x in range(4):
                for y in range(3, -1, -1):
                    if self.move_one(y, x, direction):
                        if not flag:
                            flag = True
                        self.draw()
                        if DELAY_MOVED > 0:
                            curses.napms(DELAY_MOVED)
        if not flag:
            return
        self.gen_rand()
        if self.islose():
            self.state = 2 if self.state == 0 else 4
            self.draw()
        elif self.state == 0 and self.iswin():
            self.state = 1
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
            for x in range(x0 + 1, 4):
                if row[x] is None:
                    pos = x
                else:
                    break
            # if pos == x0:
                # return
            if pos == 3:
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
            for y in range(y0 + 1, 4):
                if self.grid[y][x0] is None:
                    pos = y
                else:
                    break
            # if pos == y0:
                # return
            if pos == 3:
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
    def on_unload(self):
        self.scr.erase()
        self.scr.refresh()
        self.grid = None
    def on_press(self, key):
        if not self.can_play():
            return
        if (self.state == 0 or self.state == 3) and key in keyboard_map:
            self.move(keyboard_map[key])
            self.draw()
        elif key == ord('s') or key == ord('S'):
            self.restart()
            self.state = 0
            self.draw()
        elif key == ord('d') or key == ord('D'):
            if self.state != 1:
                return
            self.state = 3
            self.draw()
    def on_resize(self):
        Screen.on_resize(self)
        self.alloc()
        self.scr.erase()
        if not self.can_play():
            self.scr.refresh()
            return
        self.scr.erase()
        self.draw()

export = Game2048
