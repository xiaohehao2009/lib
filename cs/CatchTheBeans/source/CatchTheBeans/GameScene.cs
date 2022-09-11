using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CatchTheBeans
{
    internal class GameScene : Scene
    {
        private const int lineTop = Config.WindowHeight - 2;
        private const int scoreTop = Config.WindowHeight - 1;
        private readonly Player player = new Player();
        private Bean bean = new Bean();
        private int score;
        private static readonly string scoreReseter = new string(' ', Config.WindowWidth - 1);
        public override void Start()
        {
            Utils.SetColor(false);
            Console.Clear();
            Console.SetCursorPosition(0, lineTop);
            Console.Write(new string(Config.LineChar, Config.WindowWidth));
            Utils.SetColor(false);
            player.Print();
            bean.Print();
            PrintScore();
        }

        private void PrintScore()
        {
            Console.SetCursorPosition(0, scoreTop);
            Console.Write(scoreReseter);
            Console.SetCursorPosition(0, scoreTop);
            Console.Write($"得分: {score}");
        }
        public override void Update(Game game)
        {
            if (player.Update(game.chars))
            {
                game.ChangeScene(new BeginMenu());
                return;
            }
            bean.Update();
            if (bean.y == Player.y)
            {
                if (bean.x < player.x + Config.PlayerWidth && bean.x >= player.x)
                {
                    score += Config.ScoreWin;
                }
                else
                {
                    score -= Config.ScoreLose;
                    Console.SetCursorPosition(bean.x, bean.y);
                    Console.Write(' ');
                }
                PrintScore();
                bean = new Bean();
            }
        }
    }
}
