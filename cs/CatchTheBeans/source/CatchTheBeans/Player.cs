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
        public int X { get; private set; }
        private static readonly string str = new string(Config.PlayerChar, Config.PlayerWidth);
        private static readonly string reseter = new string(' ', Config.PlayerWidth);
        public void Print()
        {
            Console.SetCursorPosition(X, y);
            Console.Write(str);
        }
        public bool Update(List<ConsoleKeyInfo> chars)
        {
            if (chars.Count == 0)
            {
                return false;
            }
            int lastX = X;
            bool changed = false;
            foreach (ConsoleKeyInfo info in chars)
            {
                switch (info.Key)
                {
                    case ConsoleKey.A:
                    case ConsoleKey.LeftArrow:
                        if (info.Modifiers != ConsoleModifiers.Shift)
                        {
                            if (X != 0)
                            {
                                X--;
                                changed = true;
                            }
                        }
                        else
                        {
                            if (X > 1)
                            {
                                X -= 2;
                                changed = true;
                            }
                        }
                        break;
                    case ConsoleKey.D:
                    case ConsoleKey.RightArrow:
                        if (info.Modifiers != ConsoleModifiers.Shift)
                        {
                            if (X != maxX)
                            {
                                X++;
                                changed = true;
                            }
                        }
                        else
                        {
                            if (X < maxX - 1)
                            {
                                X += 2;
                                changed = true;
                            }
                        }
                        break;
                    case ConsoleKey.R:
                    case ConsoleKey.Escape:
                        chars.Clear();
                        return true;
                }
            }
            chars.Clear();
            if (changed)
            {
                Console.SetCursorPosition(lastX, y);
                Console.Write(reseter);
                Print();
            }
            return false;
        }
    }
}
