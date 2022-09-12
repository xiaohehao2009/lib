using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CatchTheBeans
{
    internal class BeginMenu : Scene
    {
        private const int BeginButtonTop = (Config.WindowHeight / 3) - 1;
        private const int DiffButtonTop = (Config.WindowHeight / 2) - 1;
        private const int EndButtonTop = (Config.WindowHeight * 2 / 3) - 1;
        private const int TextLeft = (Config.WindowWidth / 2) - 4 - 1;
        private int selectedButton;
        public override void Start()
        {
            Utils.SetColor(false);
            Console.Clear();
            PrintText();
        }

        private void PrintText()
        {
            Console.SetCursorPosition(TextLeft, BeginButtonTop);
            Utils.SetColor(selectedButton == 0);
            Console.Write("开始游戏");

            Console.SetCursorPosition(TextLeft, DiffButtonTop);
            Utils.SetColor(selectedButton == 1);
            Console.Write("选择难度");

            Console.SetCursorPosition(TextLeft, EndButtonTop);
            Utils.SetColor(selectedButton == 2);
            Console.Write("退出游戏");
        }

        public override void Update(Game game)
        {
            if (game.chars.Count == 0)
            {
                return;
            }
            bool changed = false;
            foreach (ConsoleKeyInfo info in game.chars)
            {
                switch (info.Key)
                {
                    case ConsoleKey.W:
                    case ConsoleKey.UpArrow:
                        if (selectedButton != 0)
                        {
                            selectedButton--;
                            changed = true;
                        }
                        break;
                    case ConsoleKey.S:
                    case ConsoleKey.DownArrow:
                        if (selectedButton != 2)
                        {
                            selectedButton++;
                            changed = true;
                        }
                        break;
                    case ConsoleKey.Spacebar:
                    case ConsoleKey.Enter:
                        game.chars.Clear();
                        game.ChangeScene(selectedButton switch
                        {
                            0 => new GameScene(),
                            1 => new SelectDiff(),
                            _ => new CheckSure()
                        });
                        return;
                }
            }
            game.chars.Clear();
            if (changed)
            {
                PrintText();
            }
        }
    }
}
