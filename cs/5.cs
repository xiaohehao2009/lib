using System;

namespace Test
{
    class Program
    {
        public static void PutHelperMessage()
        {
            string[] messages = {
                "<=======程序=======>",
                "| 使用说明:        |",
                "| 格式: mono 5.exe |",
                "| <message>        |",
                "| 输出 message 的  |",
                "| 内容。           |",
                "└------------------┘"
            };
            Console.WriteLine(string.Join('\n', messages));
        }
        public static void Main(string[] args)
        {
            int length = args.Length;
            if (length != 1)
            {
                PutHelperMessage();
                return;
            }
            string message = args[0];
            Console.WriteLine(message);
        }
    }
}
