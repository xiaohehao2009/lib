using System;
using HarmonyLib;
using System.Reflection;
class Program
{
    static void Main()
    {
        var harmony = new Harmony("com.me.test.harmonytest");
        harmony.PatchAll(Assembly.GetExecutingAssembly());
        Say();
    }
    static void Say()
    {
        Console.WriteLine("Hello, World!");
    }
}
[HarmonyPatch(typeof(Program), "Say")]
class Patch
{
    static void Prefix()
    {
        Console.WriteLine("Patch prefix");
    }
    static void Postfix()
    {
        Console.WriteLine("Patch postfix");
    }
}
