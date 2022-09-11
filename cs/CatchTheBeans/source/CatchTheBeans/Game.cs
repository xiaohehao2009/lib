using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CatchTheBeans
{
    internal class Game
    {
        private Scene scene = new BeginMenu();
        private readonly AutoResetEvent are = new AutoResetEvent(false);
        private Timer? timer;
        public List<ConsoleKeyInfo> chars = new List<ConsoleKeyInfo>(3);
        public void ChangeScene(Scene newScene)
        {
            this.scene = newScene;
            newScene.Start();
        }
        public void Start()
        {
            this.scene.Start();
            this.timer = new(_ =>
            {
                while (Console.KeyAvailable)
                {
                    this.chars.Add(Console.ReadKey(true));
                }
                this.scene.Update(this);
            }, null, 16, 16);
            this.are.WaitOne();
            this.timer.Dispose();
            this.are.Dispose();
        }
        public void End()
        {
            this.are.Set();
        }
    }
}
