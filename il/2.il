.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe

.namespace Test
{
    .method static void Main()
    {
        .maxstack 3
        .entrypoint
        .locals init ([0] float64, [1] int32)
        ldc.r8 2.5
        ldc.r8 0.5
        stloc.0
        ldc.i4.3
        stloc.1
    LOOP:
        ldloc.0
        ldloc.1
        conv.r8
        div
        stloc.0
        ldloc.0
        add
        ldloc.1
        ldc.i4.s 20
        beq END
        ldloc.1
        ldc.i4.1
        add
        stloc.1
        br.s LOOP
    END:
        call void [mscorlib] System.Console::WriteLine(float64)
        ret
    }
}