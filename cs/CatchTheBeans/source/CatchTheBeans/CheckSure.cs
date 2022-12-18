namespace CatchTheBeans
{
    internal class CheckSure : Scene
    {
        private const int checkerTop = (Config.WindowHeight / 2) - 3 - 1;
        private const int checkerLeft = ((Config.WindowWidth - 20) / 2) - 1;
        private const int buttonsTop = (Config.WindowHeight / 2) + 3 - 1;
        private const int cancelLeft = (Config.WindowWidth / 2) - 4 - 2 - 1;
        private const int sureLeft = (Config.WindowWidth / 2) + 4 - 2 - 1;
        private int selectedButton;
        public override void Start()
        {
            Utils.SetColor(false);
            Console.Clear();
            Console.SetCursorPosition(checkerLeft, checkerTop);
            Console.Write("您确定要退出游戏吗？");
            PrintButtons();
        }

        private void PrintButtons()
        {
            Console.SetCursorPosition(cancelLeft, buttonsTop);
            Utils.SetColor(selectedButton == 0);
            Console.Write("取消");
            Console.SetCursorPosition(sureLeft, buttonsTop);
            Utils.SetColor(selectedButton == 1);
            Console.Write("确定");
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
                    case ConsoleKey.D:
                    case ConsoleKey.LeftArrow:
                    case ConsoleKey.RightArrow:
                        selectedButton = 1 - selectedButton;
                        changed = true;
                        break;
                    case ConsoleKey.Spacebar:
                    case ConsoleKey.Enter:
                        game.chars.Clear();
                        if (selectedButton == 1)
                        {
                            Utils.SetColor(false);
                            game.End();
                        }
                        else
                        {
                            game.ChangeScene(new BeginMenu());
                        }
                        return;
                }
            }
            game.chars.Clear();
            if (changed)
            {
                PrintButtons();
            }
        }
    }
}
