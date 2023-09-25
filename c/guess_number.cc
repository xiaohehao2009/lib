#include <random>
#include <cstring>
#include <string>

#include <curses.h>

#define SHOW_NUMBER

constexpr const char TITLE[] = "Guess Number";
constexpr const char ROUND_PREFIX[] = "Round - ";
constexpr const char PS[] = ">> ";
constexpr const char COUNT_PREFIX[] = "Count - ";

constexpr int TITLE_PAIR = 1;
constexpr int ROUND_PAIR = 2;
constexpr int NUMBER_PAIR = 3;
constexpr int TIP_PAIR = 4;
constexpr int WIN_PAIR = 5;
constexpr int LOSE_PAIR = 6;
constexpr int KEYBIND_PAIR = 7;
constexpr int PS_PAIR = 8;
constexpr int COUNT_PAIR = 9;

#ifdef SHOW_NUMBER
constexpr int DEBUG_PAIR = 10;
#endif

constexpr long long LOWER_BOUND = 0;
constexpr long long UPPER_BOUND = 99999;

void start();
bool loop(int round, long long number);
long long scan_int(bool &interrupted, bool &succeeded);
long long read_input(bool &interrupted);

int main()
{
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, TRUE);

    start();
    // getch();

    endwin();
    return 0;
}

void start()
{
    // init pairs
    start_color();
    use_default_colors();
    init_pair(TITLE_PAIR, COLOR_GREEN, -1);
    init_pair(ROUND_PAIR, COLOR_BLUE, -1);
    init_pair(NUMBER_PAIR, COLOR_YELLOW, -1);
    init_pair(TIP_PAIR, COLOR_RED, -1);
    init_pair(WIN_PAIR, COLOR_GREEN, -1);
    init_pair(LOSE_PAIR, COLOR_RED, -1);
    init_pair(KEYBIND_PAIR, COLOR_BLUE, -1);
    init_pair(PS_PAIR, COLOR_GREEN, -1);
    init_pair(COUNT_PAIR, COLOR_RED, -1);

    #ifdef SHOW_NUMBER
    init_pair(DEBUG_PAIR, COLOR_CYAN, -1);
    #endif

    // draw title
    attron(COLOR_PAIR(TITLE_PAIR) | A_BOLD);
    mvinsstr(0, 0, std::string(COLS, ' ').c_str());
    mvaddstr(0, (COLS - strlen(TITLE)) / 2, TITLE);

    // draw tip
    attrset(COLOR_PAIR(TIP_PAIR));
    mvaddstr(1, 0, "TIP - The number is between ");
    attrset(COLOR_PAIR(NUMBER_PAIR));
    mvaddstr(2, 0, std::to_string(LOWER_BOUND).c_str());
    attrset(COLOR_PAIR(TIP_PAIR));
    addstr(" and ");
    attrset(COLOR_PAIR(NUMBER_PAIR));
    addstr(std::to_string(UPPER_BOUND).c_str());

    // draw key binding
    attrset(COLOR_PAIR(TIP_PAIR));
    mvaddstr(3, 0, "Press <");
    attrset(COLOR_PAIR(KEYBIND_PAIR));
    addstr("ESC");
    attrset(COLOR_PAIR(TIP_PAIR));
    addstr("> or <");
    attrset(COLOR_PAIR(KEYBIND_PAIR));
    addch('Q');
    attrset(COLOR_PAIR(TIP_PAIR));
    addstr("> to exit");

    // attrset(A_NORMAL);
    // because the attr will be set later
    refresh();

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<long long>
        distrib(LOWER_BOUND, UPPER_BOUND);
    for (int i = 1; loop(i, distrib(gen)); i++);
}

bool loop(int round, long long number) // returns false to interrupt
{
    #ifdef SHOW_NUMBER
    move(4, 0);
    clrtoeol();
    {
        std::string str = std::to_string(number);
        attrset(COLOR_PAIR(DEBUG_PAIR));
        mvaddstr(4, COLS - str.length(), str.c_str());
    }
    #endif

    attrset(COLOR_PAIR(ROUND_PAIR));
    mvaddstr(4, 0, ROUND_PREFIX);
    attrset(COLOR_PAIR(NUMBER_PAIR));
    addstr(std::to_string(round).c_str());

    attrset(A_NORMAL);
    refresh();

    attrset(COLOR_PAIR(COUNT_PAIR));
    mvaddstr(LINES - 3, 0, COUNT_PREFIX);
    clrtoeol();
    for (int i = 0; ; i++)
    {
        attrset(COLOR_PAIR(NUMBER_PAIR));
        mvaddstr(LINES - 3, strlen(COUNT_PREFIX), std::to_string(i).c_str());
        bool interrupted = false;
        long long input = read_input(interrupted);
        if (interrupted) return false;
        move(LINES - 2, 0);
        clrtoeol();
        if (input == number)
        {
            attrset(COLOR_PAIR(WIN_PAIR));
            addstr("Great! ");
            attrset(COLOR_PAIR(NUMBER_PAIR));
            addstr(std::to_string(input).c_str());
            attrset(COLOR_PAIR(WIN_PAIR));
            addstr(": It is!");
            attrset(A_NORMAL);
            refresh();
            return true;
        }
        attrset(COLOR_PAIR(LOSE_PAIR));
        addstr("Sorry! ");
        attrset(COLOR_PAIR(NUMBER_PAIR));
        addstr(std::to_string(input).c_str());
        attrset(COLOR_PAIR(LOSE_PAIR));
        addstr(": Too ");
        addstr(input < number ? "small!" : "big!");
        attrset(A_NORMAL);
        refresh();
    }
}

long long scan_int(bool &interrupted, bool &succeeded)
{
    constexpr int SIZE = 50;

    char buf[SIZE] = {};
    unsigned int pos = 0;
    for ( ; ; )
    {
        int ch = getch();
        if (ch == '\x1b' || ch == 'q' || ch == 'Q')
        {
            interrupted = true;
            return 0;
        }
        if (ch == '\n' && pos != 0 && !(pos == 1 && buf[0] == '-')) break;
        if ((ch == KEY_BACKSPACE || ch == 127 || ch == '\b') && pos != 0)
        {
            buf[--pos] = 0;
            mvdelch(getcury(stdscr), getcurx(stdscr) - 1);
            refresh();
        }
        else if (
            (ch >= '0' && ch <= '9' && pos < (SIZE - 1)) ||
            (ch == '-' && pos == 0)
        )
        {
            buf[pos++] = ch;
            addch(ch);
            refresh();
        }
    }
    try
    {
        long long value = std::stoll(std::string(buf));
        succeeded = true;
        return value;
    }
    catch (std::out_of_range)
    {
        succeeded = false;
        return 0;
    }
}

long long read_input(bool &interrupted)
{
    for ( ; ; )
    {
        move(LINES - 1, 0);
        attrset(COLOR_PAIR(PS_PAIR));
        addstr(PS);
        attrset(A_NORMAL);
        clrtoeol();
        refresh();
        bool succeeded = false;
        long long value = scan_int(interrupted, succeeded);
        if (interrupted) return 0;
        if (!succeeded)
        {
            move(LINES - 2, 0);
            clrtoeol();
            attron(COLOR_PAIR(LOSE_PAIR));
            addstr("Not a valid number!");
            attroff(COLOR_PAIR(LOSE_PAIR));
        }
        else
        {
            move(LINES - 1, strlen(PS));
            clrtoeol();
            refresh();
            return value;
        }
    }
}
