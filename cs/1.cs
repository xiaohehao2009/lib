using System;

// f(x) = f(0) + xf'(0) + x**2f''(0)/2 + x**3f3(0)/6 + ...
// e**x = 1 + x + x**2/2 + x**3/6 + ...
// e = 2 + 1/2 + 1/6 + ...

namespace Test
{
    class Program
    {
        private static void Main(string[] args)
        {
            Console.WriteLine("开始计算 E = exp(1)");
            double e = 2.5f;
            double fac = 1f / 2;
            for (int i = 3; i < 19; i++)
            {
                fac /= i;
                e += fac;
            }
            Console.WriteLine("计算结束");
            Console.WriteLine($"E = exp(1) = {e}");
        }
    }
}
