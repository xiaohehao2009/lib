.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe

.namespace Test
{
    .class Program
    {
        .method static uint64 GetNumber(int16)
        {
            .maxstack 2
            .locals init ([0] uint64, [1] uint64, [2] int16)
            ldarg.0
            ldc.i4.3
            blt.s QUICK1
            ldc.i8 1
            stloc.0
            ldc.i8 1
            stloc.1
            ldc.i4.3
            stloc.2
        LOOP:
            // b = a + b
            // a = b - a
            //     |
            //     V
            // a1 = b0
            // b1 = a0 + b0
            ldloc.0
            ldloc.1
            add
            stloc.1
            ldloc.1
            ldloc.0
            sub
            stloc.0
            ldloc.2
            ldarg.0
            beq.s END
            ldloc.2
            ldc.i4.1
            add
            stloc.2
            br.s LOOP
        END:
            ldloc.1
            ret
        QUICK1:
            ldc.i8 1
            ret
        }
        .method static void Main()
        {
            // 题目: Fibonacci 数列
            .entrypoint
            .maxstack 3
            .locals init ([0] int16)
        START:
            ldstr "请输入数字: "
            call void [mscorlib] System.Console::Write(string)
            call string [mscorlib] System.Console::ReadLine()
            ldloca.s 0
            call bool [mscorlib] System.Int16::TryParse(string, [out] int16&)
            brfalse.s FAIL
            ldloc.0
            brfalse.s FAIL
            ldloc.0
            ldc.i4.s 15
            shr
            brtrue.s FAIL
            ldstr "结果为: {0}"
            ldloc.0
            call uint64 Test.Program::GetNumber(int16)
            box [mscorlib] System.UInt64
            call void [mscorlib] System.Console::WriteLine(string, object)
            ret
        FAIL:
            ldstr "输入有误 (过大或不为正整数)"
            call void [mscorlib] System.Console::WriteLine(string)
            br.s START
        }
    }
}
