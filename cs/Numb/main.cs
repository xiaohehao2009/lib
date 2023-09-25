using System;
using System.IO;
using System.Numerics;
using System.Text;
using System.Collections.Generic;

namespace Numb
{
    static class Conv
    {
        private static char[] ConvTable = new char[]
        {
            '0', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
        };
        private static Dictionary<char, byte>
            ConvDict = new Dictionary<char, byte>()
        {
            {'0', 0}, {'1', 1}, {'2', 2}, {'3', 3},
            {'4', 4}, {'5', 5}, {'6', 6}, {'7', 7},
            {'8', 8}, {'9', 9}, {'A', 10}, {'B', 11},
            {'C', 12}, {'D', 13}, {'E', 14}, {'F', 15},
            {'a', 10}, {'b', 11}, {'c', 12}, {'d', 13},
            {'e', 14}, {'f', 15}
        };
        public static unsafe void
            ToHexString(byte[] bytes, int size, char[] res)
        {
            unsafe
            {
                fixed (char* table = ConvTable)
                fixed (char* arr = res)
                fixed (byte* input = bytes)
                {
                    for (int i = 0; i < size; i++)
                    {
                        *(arr + (i << 1)) =
                            *(table + (*(input + i) >> 4));
                        *(arr + ((i << 1) | 1)) =
                            *(table + (*(input + i) & 0b1111));
                    }
                }
            }
        }
        public static unsafe bool ToBytes(char[] str, int size, byte[] res)
        {
            unsafe
            {
                fixed (byte* arr = res)
                fixed (char* input = str)
                {
                    for (int i = 0; i < size; i += 2)
                    {
                        if (!ConvDict.TryGetValue(
                            *(input + i), out byte first
                        ))
                        {
                            return false;
                        }
                        if (!ConvDict.TryGetValue(
                            *(input + (i | 1)), out byte last
                        ))
                        {
                            return false;
                        }
                        *(arr + (i >> 1)) = (byte)((first << 4) | last);
                    }
                }
            }
            return true;
        }
    }
    static class Program
    {
        public const string file = "numb";
        public const byte MagicNumber = 60;
        public const int ChunkSize = 32 * 1024;
        public static string FilePath
        {
            get =>
            Path.Combine(
                AppDomain.CurrentDomain.BaseDirectory, file
            );
        }
        public static void Create(string path)
        {
            File.Create(path).Dispose();
            Console.Write("已创建文件 ");
            Console.ForegroundColor = ConsoleColor.Blue;
            Console.WriteLine(file);
            Console.ResetColor();
        }
        public static int GetOption()
        {
            while (true)
            {
                Console.Write(
                    "输入选项 (a/字节转数字, " +
                    "b/数字转字节, c/加密, d/解密" +
                    ", e/比特颠倒): "
                );
                char ch = Console.ReadKey().KeyChar;
                Console.WriteLine();
                if (ch == 'a' || ch == 'A') return 0;
                if (ch == 'b' || ch == 'B') return 1;
                if (ch == 'c' || ch == 'C') return 2;
                if (ch == 'd' || ch == 'D') return 3;
                if (ch == 'e' || ch == 'E') return 4;
                Console.WriteLine("输入有误!");
            }
        }
        private static string GetTempFile()
        {
            string tmp;
            do
            {
                tmp = Path.GetRandomFileName();
            }
            while (File.Exists(tmp));
            Console.Write("使用临时文件 ");
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine(tmp);
            Console.ResetColor();
            return Path.Combine(AppDomain.CurrentDomain.BaseDirectory, tmp);
        }
        private static void Backup(string path)
        {
            string newPath = $"{path}_bak";
            for (int id = 1; File.Exists(newPath); id++)
            {
                if (id > 0xffff)
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"对 {path} 的备份失败!");
                    Console.ResetColor();
                    return;
                }
                newPath = $"{path}_bak{id:X4}";
            }
            File.Copy(path, newPath);
            Console.Write("文件 ");
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.Write(path);
            Console.ResetColor();
            Console.Write(" 已备份至 ");
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine(newPath);
            Console.ResetColor();
        }
        private static void FinishUp(string path, string tmp)
        {
            File.Delete(path);
            File.Move(tmp, path);
            Console.WriteLine("临时文件替换完毕!");
        }
        public static void Bytes2Numb(string path)
        {
            Backup(path);
            string tmp = GetTempFile();
            var buffer = new byte[ChunkSize];
            var chars = new char[ChunkSize * 2];
            using (var reader = new BinaryReader(File.OpenRead(path)))
            using (var writer = new StreamWriter(tmp))
            {
                while (true)
                {
                    int size = reader.Read(buffer, 0, ChunkSize);
                    if (size == 0) break;
                    Conv.ToHexString(buffer, size, chars);
                    writer.Write(chars, 0, size << 1);
                }
            }
            FinishUp(path, tmp);
            Console.WriteLine("字节转数字完毕!");
        }
        public static void Numb2Bytes(string path)
        {
            Backup(path);
            string tmp = GetTempFile();
            var buffer = new char[ChunkSize];
            var bytes = new byte[ChunkSize >> 1];
            using (var reader = new StreamReader(path))
            using (var writer = new BinaryWriter(File.OpenWrite(tmp)))
            {
                while (true)
                {
                    int size = reader.Read(buffer, 0, ChunkSize);
                    if (size == 0) break;
                    if (!Conv.ToBytes(buffer, size, bytes))
                    {
                        Console.WriteLine("文件格式错误!\n数字转字节失败!");
                        return;
                    }
                    writer.Write(bytes, 0, size >> 1);
                }
            }
            FinishUp(path, tmp);
            Console.WriteLine("数字转字节完毕!");
        }
        public static unsafe void Encrypt(string path)
        {
            Backup(path);
            string tmp = GetTempFile();
            byte[] bytes = new byte[ChunkSize];
            using (var reader = new BinaryReader(File.OpenRead(path)))
            using (var writer = new BinaryWriter(File.OpenWrite(tmp)))
            {
                fixed (byte* arr = bytes)
                {
                    while (true)
                    {
                        int size = reader.Read(bytes, 0, ChunkSize);
                        if (size == 0) break;
                        for (int i = 0; i < size; i++)
                        {
                            *(arr + i) = (byte)(
                                (*(arr + i) << 2) |
                                (*(arr + i) >> 6)
                            );
                            *(arr + i) ^= MagicNumber;
                            *(arr + i) = (byte)(
                                (*(arr + i) << 3) |
                                (*(arr + i) >> 5)
                            );
                        }
                        writer.Write(bytes, 0, size);
                    }
                }
            }
            FinishUp(path, tmp);
            Console.WriteLine("加密完毕!");
        }
        public static unsafe void Decrypt(string path)
        {
            Backup(path);
            string tmp = GetTempFile();
            byte[] bytes = new byte[ChunkSize];
            using (var reader = new BinaryReader(File.OpenRead(path)))
            using (var writer = new BinaryWriter(File.OpenWrite(tmp)))
            {
                fixed (byte* arr = bytes)
                {
                    while (true)
                    {
                        int size = reader.Read(bytes, 0, ChunkSize);
                        if (size == 0) break;
                        for (int i = 0; i < size; i++)
                        {
                            *(arr + i) = (byte)(
                                (*(arr + i) << 5) |
                                (*(arr + i) >> 3)
                            );
                            *(arr + i) ^= MagicNumber;
                            *(arr + i) = (byte)(
                                (*(arr + i) << 6) |
                                (*(arr + i) >> 2)
                            );
                        }
                        writer.Write(bytes, 0, size);
                    }
                }
            }
            FinishUp(path, tmp);
            Console.WriteLine("解密完毕!");
        }
        public static unsafe void BitReverse(string path)
        {
            Backup(path);
            string tmp = GetTempFile();
            byte[] bytes = new byte[ChunkSize];
            using (var reader = new BinaryReader(File.OpenRead(path)))
            using (var writer = new BinaryWriter(File.OpenWrite(tmp)))
            {
                fixed (byte* arr = bytes)
                {
                    while (true)
                    {
                        int size = reader.Read(bytes, 0, ChunkSize);
                        if (size == 0) break;
                        for (int i = 0; i < size; i++)
                        {
                            *(arr + i) = (byte)(
                                (bytes[i] << 4) | (bytes[i] >> 4)
                            );
                            *(arr + i) = (byte)(
                                ((byte)(*(arr + i) & 0b00110011) << 2) |
                                ((byte)(bytes[i] & 0b11001100) >> 2)
                            );
                            *(arr + i) = (byte)(
                                ((byte)(*(arr + i) & 0b01010101) << 1) |
                                ((byte)(*(arr + i) & 0b10101010) >> 1)
                            );
                        }
                         writer.Write(bytes, 0, size);
                    }
                }
            }
            FinishUp(path, tmp);
            Console.WriteLine("比特颠倒完毕!");
        }
        public static void Main()
        {
            string path = FilePath;
            if (!File.Exists(path))
            {
                Create(path);
                return;
            }
            int flag = GetOption();
            if (flag == 0) Bytes2Numb(path);
            else if (flag == 1) Numb2Bytes(path);
            else if (flag == 2) Encrypt(path);
            else if (flag == 3) Decrypt(path);
            else if (flag == 4) BitReverse(path);
            else throw new NotImplementedException(
                $"选项: 序号 {flag}"
            );
        }
    }
}
