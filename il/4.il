.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe

.namespace Test
{
    .class Program extends [mscorlib] System.Object
    {
        .method public static string GetMessage(int32)
        {
            .maxstack 4
            .locals init ([0] [mscorlib] System.Int32[], [1] int32)
            ldarg.0
            ldarg.0
            add
            stloc.1
            ldc.i4.4
            newarr [mscorlib] System.Object
            stloc.0

            ldloc.0
            ldc.i4.0
            ldarg.0
            box [mscorlib] System.Int32
            stelem.ref

            ldloc.0
            ldc.i4.1
            ldarg.0
            box [mscorlib] System.Int32
            stelem.ref

            ldloc.0
            ldc.i4.2
            ldloc.1
            box [mscorlib] System.Int32
            stelem.ref

            ldloc.0
            ldc.i4.3
            ldloc.1
            ldloc.1
            add
            box [mscorlib] System.Int32
            stelem.ref

            ldstr "{0} 只青蛙 {1} 张嘴, {2} 只眼睛 {3} 条腿"
            ldloc.0
            call string [mscorlib] System.String::Format(string, object[])
            ret
        }
        .method public static void Main(string[])
        {
            .entrypoint
            .maxstack 2
            .locals init ([0] int32, [1] int32)
            ldarg.0
            ldlen
            brfalse.s INIT
            ldarg.0
            ldc.i4.0
            ldelem.ref
            ldloca.s 0
            call bool [mscorlib] System.Int32::TryParse(string, [out] int32&)
            brtrue.s OUTPUT
        INIT:
            ldstr "没有合适的输入, 自动设置为从 1 开始"
            call void [mscorlib] System.Console::WriteLine(string)
            ldc.i4.1
            stloc.0
        OUTPUT:
            ldloc.0
            ldc.i4.s 60
            bge FAIL
            ldloc.0
            stloc.1
        LOOP:
            ldloc.1
            call string Test.Program::GetMessage(int32)
            call void [mscorlib] System.Console::WriteLine(string)
            ldloc.1
            ldc.i4.1
            add
            stloc.1
            ldloc.1
            ldc.i4.s 60
            bgt RETURN
            br.s LOOP
        RETURN:
            ldstr "程序结束"
            call void [mscorlib] System.Console::WriteLine(string)
            ret
            FAIL:
            ldstr "你输入的数字太大了 (>=60): "
            ldloc.0
            box [mscorlib] System.Int32
            call string [mscorlib] System.String::Concat(object, object)
            call void [mscorlib] System.Console::WriteLine(string)
            ret
        }
    }
}
