using System;
using System.Reflection;

namespace Test
{
    class Farm
    {
        private int level = 1;
        private string name;

        public Farm(string name)
        {
            this.name = name;
        }
        public void PrintInfo()
        {
            Console.WriteLine($"这座农场的名字是 {this.name}, 等级是 {this.level}");
        }
    }

    static class FarmUtil
    {
        public static void SetName(Farm farm, string name)
        {
            typeof(Farm).GetField("name", BindingFlags.NonPublic |
                BindingFlags.Instance).SetValue(farm, name);
        }
        public static void SetLevel(Farm farm, int level)
        {
            typeof(Farm).GetField("level", BindingFlags.NonPublic |
                BindingFlags.Instance).SetValue(farm, level);
        }
    }

    class Program
    {
        private static void Main(string[] args)
        {
            Farm farm = new Farm("阳光农场");
            farm.PrintInfo();

            Console.WriteLine("------改名了！------");
            FarmUtil.SetName(farm, "清新牧场");
            farm.PrintInfo();

            Console.WriteLine("------升级了！------");
            FarmUtil.SetLevel(farm, 2);
            farm.PrintInfo();
        }
    }
}
