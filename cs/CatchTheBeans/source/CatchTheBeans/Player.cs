using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CatchTheBeans
{
    internal class Player
    {
        private const int maxX = Config.WindowWidth - Config.PlayerWidth;
        public const int y = Config.WindowHeight - 3;
        public int x;
        private static readonly string str = new string(Config.PlayerChar, Config.PlayerWidth);
        private static readonly string reseter = new string(' ', Config.PlayerWidth);
        public void Print()
        {
            Console.SetCursorPosition(this.x, y);
            Console.Write(str);
        }
        public bool Update(List<ConsoleKeyInfo> chars)
        {
            if (chars.Count == 0)
            {
                return false;
            }
            int lastX = this.x;
            bool changed = false;
            foreach (ConsoleKeyInfo info in chars)
            {
                char ch = info.KeyChar;
                switch (ch)
                {
                    case 'a':
                    case 'A':
                        if (info.Modifiers != ConsoleModifiers.Shift)
                        {
                            if (this.x != 0)
                            {
                                this.x--;
                                changed = true;
                            }
                        }
                        else
                        {
                            if (this.x > 1)
                            {
                                this.x -= 2;
                                changed = true;
                            }
                        }
                        break;
                    case 'd':
                    case 'D':
                        if (info.Modifiers != ConsoleModifiers.Shift)
                        {
                            if (this.x != maxX)
                            {
                                this.x++;
                                changed = true;
                            }
                        }
                        else
                        {
                            if (this.x < maxX - 1)
                            {
                                this.x += 2;
                                changed = true;
                            }
                        }
                        break;
                    case (char)ConsoleKey.Escape:
                    case 'r':
                    case 'R':
                        chars.Clear();
                        return true;
                }
            }
            chars.Clear();
            if (changed)
            {
                Console.SetCursorPosition(lastX, y);
                Console.Write(reseter);
                this.Print();
            }
            return false;
        }
    }
}
