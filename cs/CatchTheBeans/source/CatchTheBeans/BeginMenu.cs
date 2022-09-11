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
        private const int TextLeft = (Config.WindowWidth / 2) - 2 - 1;
        private int selectedButton;
        public override void Start()
        {
            Utils.SetColor(false);
            Console.Clear();
            this.PrintText();
        }

        private void PrintText()
        {
            Console.SetCursorPosition(TextLeft, BeginButtonTop);
            Utils.SetColor(this.selectedButton == 0);
            Console.Write("开始游戏");

            Console.SetCursorPosition(TextLeft, DiffButtonTop);
            Utils.SetColor(this.selectedButton == 1);
            Console.Write("选择难度");

            Console.SetCursorPosition(TextLeft, EndButtonTop);
            Utils.SetColor(this.selectedButton == 2);
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
                char ch = info.KeyChar;
                switch (ch)
                {
                    case 'w':
                    case 'W':
                        if (this.selectedButton != 0)
                        {
                            this.selectedButton--;
                            changed = true;
                        }
                        break;
                    case 's':
                    case 'S':
                        if (this.selectedButton != 2)
                        {
                            this.selectedButton++;
                            changed = true;
                        }
                        break;
                    case ' ':
                    case '\n':
                        game.chars.Clear();
                        game.ChangeScene(this.selectedButton switch
                        {
                            0 => new GameScene(),
                            1 => new SelectDiff(),
                            2 => new CheckSure(),
                            _ => throw new NotImplementedException()
                        });
                        return;
                }
            }
            game.chars.Clear();
            if (changed)
            {
                this.PrintText();
            }
        }
    }
}
