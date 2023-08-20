#!/usr/bin/env python3

import curses
def main(scr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
    at = curses.color_pair(1)
    ch = '*'
    rd = 15
    scr.addch(rd//2+1, rd+1, ch, at)
    for m in range(rd):
        n = int((rd * rd - m * m) ** 0.5)
        scr.addch((rd+m)//2+1, rd+n+1, ch, at)
        scr.addch((rd+m)//2+1, rd-n+1, ch, at)
        scr.addch((rd-m)//2+1, rd+n+1, ch, at)
        scr.addch((rd-m)//2+1, rd-n+1, ch, at)
        scr.addch((rd+n)//2+1, rd+m+1, ch, at)
        scr.addch((rd-n)//2+1, rd+m+1, ch, at)
        scr.addch((rd+n)//2+1, rd-m+1, ch, at)
        scr.addch((rd-n)//2+1, rd-m+1, ch, at)
    scr.refresh()
    scr.getch()
curses.wrapper(main)
