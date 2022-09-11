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
            this.player.Print();
            this.bean.Print();
            this.PrintScore();
        }

        private void PrintScore()
        {
            Console.SetCursorPosition(0, scoreTop);
            Console.Write(scoreReseter);
            Console.CursorLeft = 0;
            Console.Write($"得分: {this.score}");
        }
        public override void Update(Game game)
        {
            if (this.player.Update(game.chars))
            {
                game.ChangeScene(new BeginMenu());
                return;
            }
            this.bean.Update();
            if (this.bean.y == Player.y)
            {
                if (this.bean.x < this.player.x + Config.PlayerWidth && this.bean.x >= this.player.x)
                {
                    this.score += Config.ScoreWin;
                }
                else
                {
                    this.score -= Config.ScoreLose;
                    Console.SetCursorPosition(this.bean.x, this.bean.y);
                    Console.Write(' ');
                }
                this.PrintScore();
                this.bean = new Bean();
            }
        }
    }
}
