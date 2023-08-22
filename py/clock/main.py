#!/usr/bin/env python3

import curses
import curses.ascii


from data_read import get_datas


program_exit_keys = { curses.ascii.ESC, ord('c'), ord('C') }


def check_states(states, max_allowed):
    if len(states) > max_allowed:
        raise Exception(f'too many states: {len(states)}, but this program \
supports only {max_allowed} ones')

def generate_switch_dict(states, chars_list):
    return {
        (ord(ch) if isinstance(ch, str) else ch):
        pos for pos in range(len(states)) for ch in chars_list[pos]
    }

def check_pairs(states, max_allowed):
    for cls in states:
        if not hasattr(cls, 'used_pairs'):
            continue
        pairs = cls.used_pairs
        if not isinstance(pairs, tuple | list):
            raise TypeError(f'not a tuple or list: {cls.__name__}.\
used_pairs')
        if len(pairs) > max_allowed:
            raise RangeError(f'in class {cls.__name__}, too many color \
pairs: {len(pairs)}, but this program only supports {max_allowed} ones')
        if not hasattr(cls, 'styles'):
            raise Exception(f'{cls.__name__}: attribute \'used_pairs\' \
defined, but attribute \'styles\' not defined yet')

def main(stdscr):
    curses.curs_set(False)
    curses.mouseinterval(33)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    curses.use_default_colors()
    maxy, maxx = stdscr.getmaxyx()

    TopLine, states, topline_mouse_area = get_datas()
    topline_height = TopLine.topline_height

    top_line_scr = stdscr.derwin(topline_height, maxx, 0, 0)
    app_body_scr = stdscr.derwin(maxy - topline_height, maxx, 1, 0)

    curr = 0
    if len(states) == 0:
        while stdscr.getch() not in program_exit_keys:
            pass
        return

    chars_list = [
        'qQ', 'wW', 'eE', 'rR', 'tT', 'yY', 'uU', 'iI', 'oO', 'pP',
        '1!', '2@', '3#', '4$', '5%', '6^', '7&', '8*', '9(', '0)'
    ]
    check_states(states, len(chars_list))

    switch_dict = generate_switch_dict(states, chars_list)
    del chars_list

    used_pairs = 1
    def init_pairs(cls):
        if not hasattr(cls, 'used_pairs'):
            return
        cls.styles = [None for i in range(len(cls.used_pairs))]
        for i, (fg, bg) in enumerate(cls.used_pairs):
            curses.init_pair(i + used_pairs, fg, bg)
            cls.styles[i] = curses.color_pair(i + used_pairs)

    if hasattr(TopLine, 'used_pairs'):
        pairs = TopLine.used_pairs
        if not (isinstance(pairs, tuple | list)):
            raise TypeError(f'not a tuple or list: {TopLine}.\
used_pairs')
        if len(pairs) + used_pairs > curses.COLOR_PAIRS:
            raise RangeError(f'in class {TopLine}, too many color \
pairs: {len(pairs)}, but this program only supports \
{curses.COLOR_PAIRS - used_pairs} ones')
        init_pairs(TopLine)
        used_pairs += len(pairs)
    check_pairs(states, curses.COLOR_PAIRS - used_pairs)

    name_list = [cls.name for cls in states]
    top_line = TopLine(top_line_scr, name_list)
    del name_list
    top_line.draw(0)
    init_pairs(states[curr])
    app_body = states[curr](app_body_scr)
    app_body.on_load()

    while True:
        key = stdscr.getch()
        if key == curses.KEY_RESIZE:
            maxy, maxx = stdscr.getmaxyx()
            top_line_scr.resize(topline_height, maxx)
            app_body_scr.resize(maxy - topline_height, maxx)
            top_line.on_resize()
            app_body.on_resize()
            continue
        if key == curses.KEY_MOUSE:
            try:
                _, x, y, _, bstate = curses.getmouse()
            except curses.error:
                continue
            if not bstate & curses.BUTTON1_CLICKED:
                continue
            if y < topline_mouse_area:
                new_pos = top_line.get_click_pos(x)
                if new_pos == curr:
                    continue
                curr = new_pos
                top_line.draw(curr)
                app_body.on_unload()
                init_pairs(states[curr])
                app_body = states[curr](app_body_scr)
                app_body.on_load()
                continue
            app_body.on_mouse(y, x)
        if key in program_exit_keys:
            app_body.on_unload()
            return
        if key in switch_dict:
            new_pos = switch_dict[key]
            if curr == new_pos:
                continue
            curr = new_pos
            top_line.draw(curr)
            app_body.on_unload()
            init_pairs(states[curr])
            app_body = states[curr](app_body_scr)
            app_body.on_load()
            continue
        app_body.on_press(key)


if __name__ == '__main__':
    curses.wrapper(main)
