.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe

.namespace Test
{
    .class Program
    {
        .method static int64 GetPrime(int32)
        {
            .maxstack 3
            .locals init (
                [0] int64[], [1] int32, [2] int64, [3] int32
            )
            // arg --
            ldarg.0
            ldc.i4.1
            sub
            starg.s 0
            // arg == 0 ? return 2
            ldarg.0
            ldc.i4.0
            beq QUICK
            // arr = new long[arg]
            ldarg.0
            newarr int64
            stloc.0
            // arr[0] = 2
            ldloc.0
            ldc.i4.0
            ldc.i8 2
            stelem.i8
            // len = 1
            ldc.i4.1
            stloc.1
            // num = 3
            ldc.i8 3
            stloc.2
            // pos = 0
        // while true
        LOOP:
            // !(num % arr[pos]) ? goto FAIL
            ldloc.2
            ldloc.0
            ldloc.3
            ldelem.i8
            rem
            brfalse.s FAIL
            // pos ++
            ldloc.3
            ldc.i4.1
            add
            stloc.3
            // pos == len ? goto SUCC
            ldloc.3
            ldloc.1
            beq.s SUCC
            br.s LOOP
        FAIL:
            // pos = 0
            ldc.i4.0
            stloc.3
            // num += 2
            ldloc.2
            ldc.i8 2
            add
            stloc.2
            // goto LOOP
            br.s LOOP
        SUCC:
            // arg == len ? return num
            ldarg.0
            ldloc.1
            beq.s END
            // arr[len] = num
            ldloc.0
            ldloc.1
            ldloc.2
            stelem.i8
            // len ++
            ldloc.1
            ldc.i4.1
            add
            stloc.1
            // num += 2
            ldloc.2
            ldc.i8 2
            add
            stloc.2
            // pos = 0
            ldc.i4.0
            stloc.3
            // goto LOOP
            br.s LOOP
        END:
            ldloc.2
            ret
        QUICK:
            ldc.i8 2
            ret
        }
        .method static void Main(string[])
        {
            // 题目：求质数
            .entrypoint
            .maxstack 3
            .locals init ([0] int32)
        READ:
            ldstr "请输入一个 32 位整型数: "
            call void [mscorlib] System.Console::Write(string)
            call string [mscorlib] System.Console::ReadLine()
            ldloca.s 0
            call bool [mscorlib] System.Int32::TryParse(string, [out] int32&)
            brfalse.s FAIL
            ldloc.0
            brfalse.s FAIL
            ldloc.0
            ldc.i4.s 31
            shr.un
            brtrue.s FAIL
            br.s SUCC
        FAIL:
            ldstr "输入有误, 请重新输入"
            call void [mscorlib] System.Console::WriteLine(string)
            br.s READ
        SUCC:
            ldstr "第 {1} 个质数是 {0}"
            ldloc.0
            call int64 Test.Program::GetPrime(int32)
            box [mscorlib] System.Int64
            ldloc.0
            box [mscorlib] System.Int32
            call void [mscorlib]
                System.Console::WriteLine(string, object, object)
            ret
        }
    }
}
