using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CatchTheBeans
{
    internal class Bean
    {
        private static readonly Random random = new Random();
        public readonly int x;
        public int y;
        private const int maxY = Config.WindowHeight - 3;
        private int count;
        private const int bound = Config.WindowWidth;
        public Bean()
        {
            this.x = random.Next(bound);
        }

        public void Print()
        {
            Console.SetCursorPosition(this.x, this.y);
            Console.Write(Config.BeanChar);
        }
        public void Update()
        {
            if (this.y >= maxY)
            {
                return;
            }
            this.count++;
            if (this.count >= Config.BeanSpeed)
            {
                Console.SetCursorPosition(this.x, this.y);
                Console.Write(' ');
                this.count = 0;
                this.y++;
                this.Print();
            }
        }
    }
}
