namespace CatchTheBeans
{
    internal class Bean
    {
        private static readonly Random random = new Random();
        public int X { get; private set; }
        public int Y { get; private set; }
        private const int maxY = Config.WindowHeight - 3;
        private int count;
        private const int bound = Config.WindowWidth;
        public Bean()
        {
            Reset();
        }

        private void Reset()
        {
            X = random.Next(bound);
            Y = 0;
        }

        public void Print()
        {
            Console.SetCursorPosition(X, Y);
            Console.Write(Config.BeanChar);
        }
        public void Update()
        {
            count++;
            if (count >= Config.BeanSpeed)
            {
                Console.SetCursorPosition(X, Y);
                Console.Write(' ');
                count = 0;
                Y++;
                if (Y != maxY + 1)
                {
                    Print();
                }
            }
            if (Y == maxY + 1)
            {
                Reset();
            }
        }
    }
}
