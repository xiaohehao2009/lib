#!/usr/bin/env python3

import curses
def main(stdscr):
    curses.use_default_colors()
    stdscr.addstr('used DEFAULT colors here')
    stdscr.getch()
curses.wrapper(main)
