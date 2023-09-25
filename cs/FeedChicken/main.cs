using System;
using System.IO;

namespace FeedChicken
{
    struct FeedData
    {
        public long eggs;
        public byte progress;
        public long feed;
        public FeedData(long eggs, byte progress, long feed)
        {
            this.eggs = eggs;
            this.progress = progress;
            this.feed = feed;
        }
    }
    static class DataAccess
    {
        public const string fileName = "data.bin";
        public static string FilePath
        {
            get
            {
                return Path.Combine(
                    AppDomain.CurrentDomain.BaseDirectory,
                    fileName
                );
            }
        }
        public static int DataSize
        {
            get => sizeof(long) * 2 + sizeof(byte);
        }
        public static FeedData ReadData()
        {
            var path = FilePath;
            if (!File.Exists(path))
            {
                Logger.Log($"数据文件 {fileName} 不存在");
                return new FeedData();
            }
            using (var stream = File.OpenRead(path))
            {
                if (stream.Length != DataSize)
                {
                    Logger.Warn(
                        $"数据文件 {fileName} 长度错误, " +
                        $"应有 {DataSize} 字节"
                    );
                    return new FeedData();
                }
                Logger.Log($"数据文件 {fileName} 已存在");
                using (var reader = new BinaryReader(stream))
                {
                    return new FeedData(
                        reader.ReadInt64(),
                        reader.ReadByte(),
                        reader.ReadInt64()
                    );
                }
            }
        }

        public static void WriteData(FeedData data)
        {
            var path = FilePath;
            using (var file = File.OpenWrite(path))
            {
                using (var writer = new BinaryWriter(file))
                {
                    Logger.Log($"开始向 {fileName} 写入数据");
                    writer.Write(data.eggs);
                    writer.Write(data.progress);
                    writer.Write(data.feed);
                    Logger.Log($"数据写入完毕");
                }
            }
        }
    }
    enum DebugLevel
    {
        Debug = 0,
        Logged = 1,
        Normal = 2
    }
    static class Logger
    {
        public static DebugLevel level = DebugLevel.Debug;
        private static void Print<T>(T message, ConsoleColor color)
        {
            var backup = Console.ForegroundColor;
            Console.ForegroundColor = color;
            Console.WriteLine(message);
            Console.ForegroundColor = backup;
        }
        private static void PrintInline<T>(T message, ConsoleColor color)
        {
            var backup = Console.ForegroundColor;
            Console.ForegroundColor = color;
            Console.Write(message);
            Console.ForegroundColor = backup;
        }
        public static void Warn<T>(T message)
        {
            if (level <= DebugLevel.Debug)
            {
                PrintInline("[警告] ", ConsoleColor.Red);
                Console.WriteLine(message);
            }
        }
        public static void Log<T>(T message)
        {
            if (level <= DebugLevel.Logged)
            {
                PrintInline("[日志] ", ConsoleColor.Green);
                Console.WriteLine(message);
            }
        }
        public static void Info<T>(T message)
        {
            if (level <= DebugLevel.Normal)
            {
                Console.WriteLine(message);
            }
        }
        public static void Info<T>(T message, bool newline)
        {
            if (level <= DebugLevel.Normal)
            {
                if (newline) Console.WriteLine(message);
                else Console.Write(message);
            }
        }
        public static void Info<T>(T message, ConsoleColor color)
        {
            if (level <= DebugLevel.Normal)
            {
                Print(message, color);
            }
        }
        public static void Info<T>(
            T message, ConsoleColor color, bool newline
        )
        {
            if (level <= DebugLevel.Normal)
            {
                if (newline) Print(message, color);
                else PrintInline(message, color);
            }
        }
    }
    static class Program
    {
        public static void PrintHelper()
        {
            Logger.Info("按键 <", false);
            Logger.Info('Q', ConsoleColor.Blue, false);
            Logger.Info("> 喂食, 按键 <", false);
            Logger.Info('W', ConsoleColor.Blue, false);
            Logger.Info("> 获得饲料, 按键 <", false);
            Logger.Info('E', ConsoleColor.Blue, false);
            Logger.Info("> 退出");
        }
        public static void PrintInfo(FeedData data)
        {
            Logger.Info("蛋数: ", false);
            Logger.Info(data.eggs, ConsoleColor.Green, false);
            Logger.Info(" 进度: ", false);
            Logger.Info(data.progress, ConsoleColor.Green, false);
            Logger.Info(" 饲料数: ", false);
            Logger.Info(data.feed, ConsoleColor.Green);
        }
        public static void DoLayEgg(ref FeedData data)
        {
            Logger.Info("进度已满, 获得蛋 ", false);
            Logger.Info('1', ConsoleColor.Green, false);
            Logger.Info(" 个!");
            data.progress -= 100;
            data.eggs++;
        }
        public static void DoFeed(ref FeedData data)
        {
            if (data.feed < 100)
            {
                Logger.Info("饲料不足!");
                return;
            }
            Logger.Info("消耗饲料 ", false);
            Logger.Info("100", ConsoleColor.Green, false);
            Logger.Info(" 克!");
            data.feed -= 100;
            data.progress++;
            if (data.progress >= 100)
            {
                DoLayEgg(ref data);
            }
        }
        public static void DoPrice(ref FeedData data)
        {
            Logger.Info("获得饲料 ", false);
            Logger.Info("100", ConsoleColor.Green, false);
            Logger.Info(" 克!");
            data.feed += 100;
        }
        public static bool ProcessKey(char key, ref FeedData data)
        {
            if (key == 'q' || key == 'Q')
            {
                DoFeed(ref data);
                PrintInfo(data);
                return false;
            }
            else if (key == 'w' || key == 'W')
            {
                DoPrice(ref data);
                PrintInfo(data);
                return false;
            }
            else if (key == 'e' || key == 'E')
            {
                return true;
            }
            return false;
        }
        public static void Main()
        {
            Console.TreatControlCAsInput = true;
            var data = DataAccess.ReadData();
            Logger.Log("程序开始!");
            PrintHelper();
            PrintInfo(data);
            for ( ; ; )
            {
                char ch = Console.ReadKey(true).KeyChar;
                if (ProcessKey(ch, ref data)) break;
            }
            Logger.Log("程序结束!");
            DataAccess.WriteData(data);
        }
    }
}
