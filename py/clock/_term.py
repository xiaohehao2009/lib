#!/usr/bin/env python3

import curses
import curses.ascii as ascii
def main(scr):
    scr.addstr(0, 0, str(scr.getmaxyx()))
    scr.refresh()
    while True:
        ch = scr.getch()
        if ch == curses.KEY_RESIZE:
            scr.addstr(0, 0, str(scr.getmaxyx()))
            scr.refresh()
        elif ch == ascii.ESC:
            return
curses.wrapper(main)
