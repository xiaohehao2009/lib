import tty, termios, sys, os, fcntl, select

fd = sys.stdin.fileno()
def noecho():
    new_settings = termios.tcgetattr(fd)
    new_settings[3] &= ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, new_settings)

def echo():
    new_settings = termios.tcgetattr(fd)
    new_settings[3] |= termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, new_settings)

def savetty():
    global settings
    settings = termios.tcgetattr(fd)

def loadtty():
    termios.tcsetattr(fd, termios.TCSANOW, settings)

def getch():
    '''
        get a character from the stdin
    '''
    savetty()
    try:
        tty.setcbreak(fd)
        return sys.stdin.read(1)
    finally:
        loadtty()

def putchar(ch):
    '''
        put a character into the stdout
    '''
    sys.stdout.buffer.write(str.encode(ch))
    sys.stdout.flush()
    return ch

def getchar():
    '''
        get a character from the stdin and echo
    '''
    return putchar(getch())

def getch_():
    '''
        get a character from the stdin without blocking
    '''
    savetty()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    try:
        tty.setcbreak(fd)
        fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
        return sys.stdin.read(1)
    except IOError:
        return ''
    finally:
        loadtty()
        fcntl.fcntl(fd, fcntl.F_SETFL, fl)

def getchar_():
    '''
        get a character from the stdin and echo without blocking
    '''
    ch = getch_()
    if ch != '':
        putchar(ch)
    return ch

def kbhit():
    '''
        returns if a character is ready to be read
    '''
    savetty()
    try:
        tty.setcbreak(fd)
        return len(select.select([sys.stdin], [], [], 0)[0]) == 1
    finally:
        loadtty()

def wrapper(func, *args, **argv):
    savetty()
    noecho()
    try:
        return func(*args, **argv)
    finally:
        loadtty()

if __name__ == '__main__':
    def main():
        stop_flag = '\x18' # Ctrl + X
        debug = False
        while True:
            ch = getch()
            if ch == stop_flag:
                if not debug:
                    putchar('\n')
                break
            if ch == '\x11': # Ctrl + Q
                debug = not debug
                print(f'\ndebug mode {"en" if debug else "dis"}abled')
                continue
            if ch == '\x08' or ch == '\x7f':
                print('\x1b[D\x1b[P', end='')
                sys.stdout.flush()
            elif debug:
                print(ch, hex(ord(ch)))
            else:
                putchar(ch)
    wrapper(main)
