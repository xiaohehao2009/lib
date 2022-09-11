using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CatchTheBeans
{
    internal class SelectDiff : Scene
    {
        private const int textTop = (Config.WindowHeight / 2) - 3 - 1;
        private const int textLeft = ((Config.WindowWidth - 7) / 2) - 1;
        private int selectedButton;
        private const int buttonsTop = (Config.WindowHeight / 2) + 3 - 1;
        private const int easyLeft = (Config.WindowWidth / 4) - 1;
        private const int normalLeft = (Config.WindowWidth / 2) - 1;
        private const int diffLeft = (Config.WindowWidth * 3 / 4) - 1;
        public override void Start()
        {
            Utils.SetColor(false);
            Console.Clear();
            Console.SetCursorPosition(textLeft, textTop);
            Console.Write("请选择游戏难度");
            this.selectedButton = Config.SelectedSpeed;
            this.PrintText();
        }
        private void PrintText()
        {
            Utils.SetColor(this.selectedButton == 0);
            Console.SetCursorPosition(easyLeft, buttonsTop);
            Console.Write("简单");
            Utils.SetColor(this.selectedButton == 1);
            Console.SetCursorPosition(normalLeft, buttonsTop);
            Console.Write("普通");
            Utils.SetColor(this.selectedButton == 2);
            Console.SetCursorPosition(diffLeft, buttonsTop);
            Console.Write("困难");
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
                    case 'a':
                    case 'A':
                        if (this.selectedButton != 0)
                        {
                            this.selectedButton--;
                            changed = true;
                        }
                        break;
                    case 'd':
                    case 'D':
                        if (this.selectedButton != 2)
                        {
                            this.selectedButton++;
                            changed = true;
                        }
                        break;
                    case ' ':
                    case '\n':
                        Config.SelectedSpeed = this.selectedButton;
                        game.chars.Clear();
                        game.ChangeScene(new BeginMenu());
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
