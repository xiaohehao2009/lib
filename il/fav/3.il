.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe

.namespace Test
{
    .class abstract beforefieldinit Program
    {
        .method private static string GetString(string)
            cil managed
        {
            .maxstack 4
            ldc.i4.s 0x20
            ldarg.0
            ldc.i4.s 0x20
            ldc.i4.0
            call instance string[] [mscorlib] System.String::Split(char,
                valuetype [mscorlib] System.StringSplitOptions)
            dup
            call void [mscorlib] System.Array::Reverse(
                [mscorlib] System.Array)
            call string [mscorlib] System.String::Join(char, string[])
            ret
        }
        .method private static hidebysig specialname void Main() cil managed
        {
            // 题目: 单词逆序输出
            .entrypoint
            .maxstack 2
            ldstr "输入句子: "
            call void [mscorlib] System.Console::Write(string)
            call string [mscorlib] System.Console::ReadLine()
            call string Test.Program::GetString(string)
            call void [mscorlib] System.Console::WriteLine(string)
            ret
        }
    }
}