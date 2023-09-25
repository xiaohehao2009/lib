.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe

.namespace Test
{
    .class abstract beforefieldinit Program
    {
        .method private static specialname void ReadData
            ([out] int8&, [out] uint64&) il managed
        {
            .maxstack 3
            .locals init ([0] string[], [1] int8, [2] uint64)
        START:
            ldstr "输入两个数字, 第一个数字是纸张最初厚度, 第二个数字是纸张最后厚度: "
            call void [mscorlib] System.Console::WriteLine(string)
            call string [mscorlib] System.Console::ReadLine()
            dup
            ldnull
            beq.s FAIL1
            ldc.i4.s 0x20
            ldc.i4.1
            call instance string[] [mscorlib] System.String::Split(
                char, valuetype [mscorlib] System.StringSplitOptions
            )
            stloc.0
            ldloc.0
            ldlen
            ldc.i4.2
            ceq
            brfalse.s FAIL2
            ldloc.0
            ldc.i4.0
            ldelem.ref
            ldloca.s 1
            call bool [mscorlib] System.SByte::TryParse(string, [out] int8&)
            brfalse.s FAIL3
            ldloc.1
            brfalse.s FAIL3
            ldloc.1
            ldc.i4.7
            shr
            brtrue.s FAIL3
            ldloc.0
            ldc.i4.1
            ldelem.ref
            ldloca.s 2
            call bool [mscorlib] System.UInt64::
                TryParse(string, [out] uint64&)
            brfalse.s FAIL4
            ldloc.2
            brfalse.s FAIL4
            br.s END
        FAIL1:
            pop
            ldstr "I/O 错误, 请检查你的输入设备或尝试重新输入"
            call void [mscorlib] System.Console::WriteLine(string)
            br.s START
        FAIL2:
            ldstr "格式有误"
            call void [mscorlib] System.Console::WriteLine(string)
            br.s START
        FAIL3:
            ldstr "无法识别为 int8 类型或不是正数: "
            ldloc.0
            ldc.i4.0
            ldelem.ref
            call string [mscorlib] System.String::Concat(string, string)
            call void [mscorlib] System.Console::WriteLine(string)
            br.s START
        FAIL4:
            ldstr "无法识别为 uint64 类型或不是正数: "
            ldloc.0
            ldc.i4.1
            ldelem.ref
            call string [mscorlib] System.String::Concat(string, string)
            call void [mscorlib] System.Console::WriteLine(string)
            br START
        END:
            ldarg.0
            ldloc.1
            stind.i1
            ldarg.1
            ldloc.2
            stind.i8
            ret
        }
        .method private static specialname int8 GetResult(int8, uint64)
        {
            .maxstack 3
            .locals init ([0] int8)
            ldarg.0
            conv.u8
            dup
            ldarg.1
            bge.un.s QUICK0
            ldc.i4.1
            stloc.0
        LOOP:
            ldc.i4.1
            shl
            dup
            ldarg.1
            bge.un.s END
            ldloc.0
            ldc.i4.1
            add
            stloc.0
            br.s LOOP
        END:
            pop
            ldloc.0
            ret
        QUICK0:
            pop
            ldc.i4.0
            ret
        }
        .method private static hidebysig specialname void Main() il managed
        {
            // 题目: 纸张对折
            .entrypoint
            .maxstack 3
            .locals init ([0] int8, [1] uint64)
            ldstr "需要对折的次数: "
            ldloca.s 0
            ldloca.s 1
            call void Test.Program::ReadData([out] int8&, [out] uint64&)
            ldloc.0
            ldloc.1
            call int8 Test.Program::GetResult(int8, uint64)
            call string [mscorlib] System.Convert::ToString(int8)
            call string [mscorlib] System.String::Concat(string, string)
            call void [mscorlib] System.Console::WriteLine(string)
            ret
        }
    }
}