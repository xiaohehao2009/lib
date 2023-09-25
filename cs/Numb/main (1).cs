using System;
using System.IO;
using System.Numerics;

namespace Numb
{
    class Program
    {
        public const string file = "numb";
        public const string prefix = "(RemovePrefix)";
        public const byte magicNumb = 60;
        public static string FilePath
        {
            get =>
                Path.Combine(
                    AppDomain.CurrentDomain.BaseDirectory,
                    file
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
        public static void Bytes2Numb(string path)
        {
            byte[] origin = File.ReadAllBytes(path);
            byte[] bytes = new byte[origin.Length + 1];
            origin.CopyTo(bytes, 1);
            bytes[0] = magicNumb;
            BigInteger numb = new BigInteger(
                (ReadOnlySpan<byte>)bytes, false, true
            );
            string res = prefix + numb.ToString();
            File.WriteAllText(path, res);
            Console.WriteLine("字节转数字完毕!");
        }
        public static void Numb2Bytes(string path)
        {
            string text = File.ReadAllText(path);
            bool flag = text.StartsWith(prefix);
            if (flag) text = text.Substring(prefix.Length);
            if (!BigInteger.TryParse(text, out BigInteger res))
            {
                Console.WriteLine(
                    $"解析失败: {path}, " +
                    "不是一个合法的 BigInteger 字面量"
                );
                return;
            }
            byte[] bytes = res.ToByteArray(false, true);
            if (flag && bytes.Length != 0 && bytes[0] == magicNumb)
            {
                byte[] array = new byte[bytes.Length - 1];
                Array.Copy(bytes, 1, array, 0, bytes.Length - 1);
                bytes = array;
            }
            File.WriteAllBytes(path, bytes);
            Console.WriteLine("数字转字节完毕!");
        }
        public static void Encrypt(string path)
        {
            byte[] bytes = File.ReadAllBytes(path);
            for (int i = 0; i < bytes.Length; i++)
            {
                bytes[i] = (byte)(255 - bytes[i]);
                bytes[i] ^= magicNumb;
                bytes[i] = (byte)((bytes[i] << 3) | (bytes[i] >> 5));
            }
            File.WriteAllBytes(path, bytes);
            Console.WriteLine("加密完毕!");
        }
        public static void Decrypt(string path)
        {
            byte[] bytes = File.ReadAllBytes(path);
            for (int i = 0; i < bytes.Length; i++)
            {
                bytes[i] = (byte)((bytes[i] << 5) | (bytes[i] >> 3));
                bytes[i] ^= magicNumb;
                bytes[i] = (byte)(255 - bytes[i]);
            }
            File.WriteAllBytes(path, bytes);
            Console.WriteLine("解密完毕!");
        }
        public static void BitReverse(string path)
        {
            byte[] bytes = File.ReadAllBytes(path);
            for (int i = 0; i < bytes.Length; i++)
            {
                bytes[i] = (byte)((bytes[i] << 4) | (bytes[i] >> 4));
                bytes[i] = (byte)(
                    ((byte)(bytes[i] & 0b00110011) << 2) |
                    ((byte)(bytes[i] & 0b11001100) >> 2)
                );
                bytes[i] = (byte)(
                    ((byte)(bytes[i] & 0b01010101) << 1) |
                    ((byte)(bytes[i] & 0b10101010) >> 1)
                );
            }
            File.WriteAllBytes(path, bytes);
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
