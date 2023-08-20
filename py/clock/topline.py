import curses

class TopLine:
    last_highlight = 0

    def __init__(self, scr, states):
        self.scr = scr
        self.maxy, self.maxx = scr.getmaxyx()
        self.states = states

    def draw(self, highlight_pos):
        self.last_highlight = highlight_pos
        length = len(self.states)
        for i in range(length):
            if i == highlight_pos:
                continue
            str_pos = int(self.maxx / length * i)
            self.scr.addstr(0, str_pos, self.states[i])
        str_pos = int(self.maxx / length * highlight_pos)
        self.scr.addstr(0, str_pos, self.states[highlight_pos],
            curses.A_REVERSE)
        self.scr.refresh()

    def on_resize(self):
        self.maxy, self.maxx = self.scr.getmaxyx()
        self.scr.erase()
        self.draw(self.last_highlight)

    def get_click_pos(self, x):
        return int(x / (self.maxx / len(self.states)))
