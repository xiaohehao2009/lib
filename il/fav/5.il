.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe

.namespace Test
{
    .class abstract beforefieldinit Program
    {
        .method private static specialname int64[] GetArray() il managed
        {
            .maxstack 3
            .locals init ([0] string[], [1] int64[], [2] int32, [3] int64)
        START:
            ldstr "输入数组:"
            call void [mscorlib] System.Console::WriteLine(string)
            call string [mscorlib] System.Console::ReadLine()
            dup
            ldnull
            beq.s PREFAIL
            ldc.i4.s 0x20 // Space
            ldc.i4.1
            call instance string[] [mscorlib] System.String::Split(
                char,
                valuetype [mscorlib] System.StringSplitOptions
            )
            stloc.0
            ldloc.0
            ldlen
            dup
            brfalse.s PREFAIL2
            newarr int64
            stloc.1
            ldloc.0
            ldlen
            ldc.i4.1
            sub
            stloc.2
        LOOP:
            ldloc.0
            ldloc.2
            ldelem.ref
            ldloca.s 3
            call bool [mscorlib] System.Int64::TryParse(string, [out] int64&)
            brfalse.s FAIL
            ldloc.1
            ldloc.2
            ldloc.3
            stelem.i8
            ldloc.2
            brfalse.s END
            ldloc.2
            ldc.i4.1
            sub
            stloc.2
            br.s LOOP
        PREFAIL:
            pop
            ldstr "输入错误 (string [mscorlib] System.Console::ReadLine() 返回 null), 可能是你的输入为 Ctrl+D 或你的输入设备出现了问题。"
            call void [mscorlib] System.Console::WriteLine(string)
            br.s START
        PREFAIL2:
            pop
            ldstr "输入错误: 你没有输入一个正确格式的字符串。"
            call void [mscorlib] System.Console::WriteLine(string)
            br.s START
        FAIL:
            ldstr "不是一个正确的数字: "
            ldloc.0
            ldloc.2
            ldelem.ref
            call string [mscorlib] System.String::Concat(string, string)
            call void [mscorlib] System.Console::WriteLine(string)
            br.s START
        END:
            ldloc.1
            ret
        }
        .method private static specialname void SortArray(int64[]) il managed
        {
            .maxstack 6
            .locals init ([0] int32, [1] int32, [2] int32)
            // max = length - 1
            ldarg.0
            ldlen
            ldc.i4.1
            sub
            stloc.2
            // i = 0
            ldc.i4.0
            stloc.0
        LOOP:
            // if i == max break
            ldloc.0
            ldloc.2
            beq.s END
            // j = max
            ldloc.2
            stloc.1
        LOOP2:
            // if i == j break
            ldloc.1
            ldloc.0
            beq.s ENDLOOP2
            // if (arr[j] >= arr[--j]) continue
            ldarg.0
            ldloc.1
            ldelem.i8
            ldarg.0
            ldloc.1
            ldc.i4.1
            sub
            stloc.1
            ldloc.1
            ldelem.i8
            bge.s LOOP2
            // swap
            // arr[j] = arr[j] ^ arr[j+1]
            ldarg.0
            ldloc.1
            ldarg.0
            ldloc.1
            ldelem.i8
            ldarg.0
            ldloc.1
            ldc.i4.1
            add
            ldelem.i8
            xor
            stelem.i8
            // arr[j+1] = arr[j] ^ arr[j+1]
            ldarg.0
            ldloc.1
            ldc.i4.1
            add
            ldarg.0
            ldloc.1
            ldelem.i8
            ldarg.0
            ldloc.1
            ldc.i4.1
            add
            ldelem.i8
            xor
            stelem.i8
            // arr[j] = arr[j] ^ arr[j+1]
            ldarg.0
            ldloc.1
            ldarg.0
            ldloc.1
            ldelem.i8
            ldarg.0
            ldloc.1
            ldc.i4.1
            add
            ldelem.i8
            xor
            stelem.i8
            br.s LOOP2
        ENDLOOP2:
            // i ++
            ldloc.0
            ldc.i4.1
            add
            stloc.0
            br.s LOOP
        END:
            ret
        }
        .method private static specialname void PutArray(int64[]) il managed
        {
            .maxstack 3
            ldstr "排序完毕:\n"
            ldc.i4.s 0x20 // Space
            ldarg.0
            call string [mscorlib] System.String::Join<int64>(
                char, class [mscorlib]
                System.Collections.Generic.IEnumerable`1<!!0>
            )
            call string [mscorlib] System.String::Concat(string, string)
            call void [mscorlib] System.Console::WriteLine(string)
            ret
        }
        .method private static hidebysig specialname void Main() il managed
        {
            // 题目: 冒泡排序
            .entrypoint
            .maxstack 2
            call int64[] Test.Program::GetArray()
            dup
            call void Test.Program::SortArray(int64[])
            call void Test.Program::PutArray(int64[])
            ret
        }
    }
}