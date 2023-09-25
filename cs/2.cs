using System;

// pi = 4∫(0^1)√(1-x**2)dx

namespace Test
{
    class Program
    {
        private static void Main(string[] args)
        {
            Console.WriteLine("开始计算 PI = 4∫(0^1)√(1-x**2)dx");
            double pi = 0f;
            double step = 1f / 1e7;
            for (double i = 0f; i <= 1f; i += step)
            {
                pi += Math.Sqrt(1 - i * i);
            }
            pi *= step;
            pi *= 4;
            Console.WriteLine("计算结束");
            Console.WriteLine($"PI = 4∫(0^1)√(1-x**2)dx = {pi}");
        }
    }
}
