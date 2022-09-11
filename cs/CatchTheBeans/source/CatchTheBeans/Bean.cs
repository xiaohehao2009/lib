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
        public int x;
        public int y;
        private const int maxY = Config.WindowHeight - 3;
        private int count;
        private const int bound = Config.WindowWidth;
        public Bean()
        {
            Reset();
        }

        private void Reset()
        {
            x = random.Next(bound);
            y = 0;
        }

        public void Print()
        {
            Console.SetCursorPosition(x, y);
            Console.Write(Config.BeanChar);
        }
        public void Update()
        {
            count++;
            if (count >= Config.BeanSpeed)
            {
                Console.SetCursorPosition(x, y);
                Console.Write(' ');
                count = 0;
                y++;
                if (y != maxY + 1)
                {
                    Print();
                }
            }
            if (y == maxY + 1)
            {
                Reset();
            }
        }
    }
}
