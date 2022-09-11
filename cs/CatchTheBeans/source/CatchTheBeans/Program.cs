using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CatchTheBeans
{
    internal class Program
    {
        private static void Main()
        {
            Console.SetWindowSize(Config.WindowWidth, Config.WindowHeight);
            Console.SetBufferSize(Config.WindowWidth, Config.WindowHeight);
            Console.CursorVisible = false;
            DisableQuickEdit.DisbleQuickEditMode();
            Game game = new Game();
            game.Start();
        }
    }
}
