.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe
.method static void Main() cil managed
{
    .maxstack 1
    ldstr "Test!"
    call void [mscorlib] System.Console::WriteLine(string)
    ldc.i4.2
    pop
    ret .entrypoint
}