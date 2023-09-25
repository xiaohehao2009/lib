.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe
.method static void Main(string[])
{
    .entrypoint
    .maxstack 2
    ldarg.0
    ldlen
    brfalse.s INIT
    ldarg.0
    ldc.i4.0
    ldelem.ref
    br.s OUTPUT
    INIT:
    ldstr "你好! Hello! こんにちは! 안녕하세요! bonjour. hallo. Привет."
    OUTPUT:
    call void [mscorlib] System.Console::WriteLine(string)
    ret
}