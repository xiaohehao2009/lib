#!/usr/bin/env python3

import curses
def main(scr):
    scr.addstr(0, 0, str(scr.getmaxyx()))
    scr.refresh()
    while True:
        ch = scr.getch()
        if ch == curses.KEY_RESIZE:
            scr.addstr(0, 0, str(scr.getmaxyx()))
            scr.refresh()
        else:
            return
curses.wrapper(main)
