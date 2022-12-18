namespace CatchTheBeans
{
    internal class Game
    {
        private Scene scene = new BeginMenu();
        private readonly AutoResetEvent are = new AutoResetEvent(false);
        private readonly Timer timer;
        public List<ConsoleKeyInfo> chars = new List<ConsoleKeyInfo>(3);
        public Game()
        {
            timer = new Timer(_ =>
            {
                while (Console.KeyAvailable)
                {
                    chars.Add(Console.ReadKey(true));
                }
                scene.Update(this);
            }, null, Timeout.Infinite, 16);
        }

        public void ChangeScene(Scene newScene)
        {
            scene = newScene;
            newScene.Start();
        }
        public void Start()
        {
            scene.Start();
            timer.Change(16, 16);
            are.WaitOne();
            timer.Dispose();
            are.Dispose();
        }
        public void End()
        {
            are.Set();
        }
    }
}
