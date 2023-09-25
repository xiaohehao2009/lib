.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe

.namespace Test
{
    .method static void Main()
    {
        .entrypoint
        .maxstack 2
        .locals init ([0] int32,
            [1] valuetype [mscorlib] System.ConsoleKeyInfo)
    START:
        call valuetype [mscorlib] System.ConsoleKeyInfo [mscorlib] System.Console::ReadKey()
        stloc.1
        ldloca.s 1
        call instance char [mscorlib] System.ConsoleKeyInfo::get_KeyChar()
        stloc.0
        ldloc.0
        ldc.i4.s 114
        beq END
        ldloc.0
        ldc.i4.s 82
        beq END
        ldstr "你输入了字符 "
        call void [mscorlib] System.Console::Write(string)
        ldloc.0
        call void [mscorlib] System.Console::WriteLine(int32)
        br.s START
    END:
        ldstr "程序终止"
        call void [mscorlib] System.Console::WriteLine(string)
        ret
    }
}
