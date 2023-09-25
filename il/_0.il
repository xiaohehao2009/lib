.assembly extern mscorlib { auto }
.assembly HelloWorld {}
.module HelloWorld.exe

.namespace HelloWorld
{
    .method static void Do()
    {
        .maxstack 2
        .locals init ([0] int64)
        ldstr "输入一个64位整型数字: "
        call void [mscorlib] System.Console::Write(string)
        call string [mscorlib] System.Console::ReadLine()
        ldloca.s 0
        call bool [mscorlib] System.Int64::TryParse(string, [out] int64&)
        brfalse.s FAIL
        ldstr "你输入了: "
        call void [mscorlib] System.Console::Write(string)
        ldloc.s 0
        call void [mscorlib] System.Console::WriteLine(int64)
        ret
        FAIL:
        ldstr "不是一个64位整型数字!"
        call void [mscorlib] System.Console::WriteLine(string)
        ret
    }
    .method static void Main()
    {
        .entrypoint
        .maxstack 1
        ldstr "一个用 MSIL 开发的程序:"
        call void [mscorlib] System.Console::WriteLine(string)
        call void Do()
        ret
    }
}
