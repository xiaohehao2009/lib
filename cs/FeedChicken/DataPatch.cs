using System;
using System.IO;

namespace DataPatch
{
    class Program
    {
        public const string prompt = "请输入数字。";
        public const string excEof = "终端 I/O 异常。";
        public const string excCnp = "不是一个合法的数字。";
        public static byte ReadByte()
        {
            for ( ; ; )
            {
                Console.WriteLine(prompt);
                string str = Console.ReadLine();
                if (str == null)
                {
                    Console.WriteLine(excEof);
                    continue;
                }
                bool flag = byte.TryParse(str, out byte res);
                if (!flag)
                {
                    Console.WriteLine(excCnp);
                    continue;
                }
                return res;
            }
        }
        public static long ReadLong()
        {
            for ( ; ; )
            {
                Console.WriteLine(prompt);
                string str = Console.ReadLine();
                if (str == null)
                {
                    Console.WriteLine(excEof);
                    continue;
                }
                bool flag = long.TryParse(str, out long res);
                if (!flag)
                {
                    Console.WriteLine(excCnp);
                    continue;
                }
                return res;
            }
        }
        public static void Main()
        {
            Console.WriteLine("输入蛋数:");
            long eggs = ReadLong();
            Console.WriteLine("输入进度:");
            byte progress = ReadByte();
            Console.WriteLine("输入饲料:");
            long feed = ReadLong();
            string path = Path.Combine(
                AppDomain.CurrentDomain.BaseDirectory,
                "data.bin"
            );
            using (var stream = File.OpenWrite(path))
            {
                using (var writer = new BinaryWriter(stream))
                {
                    writer.Write(eggs);
                    writer.Write(progress);
                    writer.Write(feed);
                }
            }
            Console.WriteLine("数据文件 Patch 完成!");
        }
    }
}
