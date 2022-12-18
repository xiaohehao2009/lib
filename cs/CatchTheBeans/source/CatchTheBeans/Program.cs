namespace CatchTheBeans
{
    internal class Program
    {
        private static void Main()
        {
            Console.SetWindowSize(Config.WindowWidth, Config.WindowHeight);
            Console.SetBufferSize(Config.WindowWidth, Config.WindowHeight);
            Console.CursorVisible = false;
            Game game = new Game();
            game.Start();
        }
    }
}
