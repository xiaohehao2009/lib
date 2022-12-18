namespace CatchTheBeans
{
    internal class SelectDiff : Scene
    {
        private const int textTop = (Config.WindowHeight / 2) - 3 - 1;
        private const int textLeft = ((Config.WindowWidth - 14) / 2) - 1;
        private int selectedButton;
        private const int buttonsTop = (Config.WindowHeight / 2) + 3 - 1;
        private const int easyLeft = (Config.WindowWidth / 4) - 2 - 1;
        private const int normalLeft = (Config.WindowWidth / 2) - 2 - 1;
        private const int diffLeft = (Config.WindowWidth * 3 / 4) - 2 - 1;
        public override void Start()
        {
            Utils.SetColor(false);
            Console.Clear();
            Console.SetCursorPosition(textLeft, textTop);
            Console.Write("请选择游戏难度");
            selectedButton = Config.SelectedSpeed;
            PrintText();
        }
        private void PrintText()
        {
            Utils.SetColor(selectedButton == 0);
            Console.SetCursorPosition(easyLeft, buttonsTop);
            Console.Write("简单");
            Utils.SetColor(selectedButton == 1);
            Console.SetCursorPosition(normalLeft, buttonsTop);
            Console.Write("普通");
            Utils.SetColor(selectedButton == 2);
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
                switch (info.Key)
                {
                    case ConsoleKey.A:
                    case ConsoleKey.LeftArrow:
                        changed = true;
                        if (selectedButton != 0)
                        {
                            selectedButton--;
                        }
                        else
                        {
                            selectedButton = 2;
                        }
                        break;
                    case ConsoleKey.D:
                    case ConsoleKey.RightArrow:
                        changed = true;
                        if (selectedButton != 2)
                        {
                            selectedButton++;
                        }
                        else
                        {
                            selectedButton = 0;
                        }
                        break;
                    case ConsoleKey.Spacebar:
                    case ConsoleKey.Enter:
                        Config.SelectedSpeed = selectedButton;
                        Config.BeanSpeed = Config.BeanSpeeds[selectedButton];
                        game.chars.Clear();
                        game.ChangeScene(new BeginMenu());
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
