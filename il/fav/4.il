.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe

.namespace Test
{
    .class abstract beforefieldinit Program
    {
        .method private static specialname uint64 GetFactorial
            (int8) il managed
        {
            .maxstack 3
            .locals init ([0] int8)
            ldarg.0
            ldc.i4.1
            shr
            brfalse.s QUICK
            ldc.i4.2
            stloc.0
            ldc.i8 1
        LOOP:
            ldloc.0
            conv.u8
            mul
            ldloc.0
            ldarg.0
            beq.s END
            ldloc.0
            ldc.i4.1
            add
            stloc.0
            br.s LOOP
        END:
            ret
        QUICK:
            ldc.i8 1
            ret
        }
        .method private static hidebysig specialname void Main() il managed
        {
            // 题目: 求阶乘
            .entrypoint
            .maxstack 2
            .locals init ([0] int8, [1] uint64)
        START:
            ldstr "输入数字: "
            call void [mscorlib] System.Console::Write(string)
            call string [mscorlib] System.Console::ReadLine()
            ldloca.s 0
            call bool [mscorlib] System.SByte::TryParse(string, [out] int8&)
            brfalse.s FAIL
            ldloc.0
            ldc.i4.7
            shr
            brtrue.s FAIL
            ldloc.0
            call uint64 Test.Program::GetFactorial(int8)
            stloc.1
            ldloca.s 0
            call instance string [mscorlib] System.SByte::ToString()
            ldstr " 的阶乘是 "
            call string [mscorlib] System.String::Concat(string, string)
            ldloca.s 1
            call instance string [mscorlib] System.UInt64::ToString()
            call string [mscorlib] System.String::Concat(string, string)
            call void [mscorlib] System.Console::WriteLine(string)
            ret
        FAIL:
            ldstr "输入有误, 请重新输入"
            call void [mscorlib] System.Console::WriteLine(string)
            br.s START
        }
    }
}
