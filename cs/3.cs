using System;

namespace Test
{
    interface IPrinter
    {
        void Println(string message);
    }
    class Printer : IPrinter
    {
        public void Println(string message)
        {
            Console.WriteLine(message);
        }
    }

    class MessageGetter
    {
        private const string message = "Hello, World!";

        public string GetMessage()
        {
            return message;
        }
    }

    class Program
    {
        private static void Main(string[] args)
        {
            MessageGetter messageGetter = new MessageGetter();
            string message = messageGetter.GetMessage();
            Printer printer = new Printer();
            printer.Println(message);
        }
    }
}
