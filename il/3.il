.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe

.namespace Test
{
    .method static void Main()
    {
        .maxstack 4
        .entrypoint
        .locals init ([0] float64)
        ldc.r8 0
        ldc.r8 0
        stloc.0

    LOOP:
        ldc.r8 1
        ldloc.0
        ldloc.0
        mul
        sub
        call float64 [mscorlib] System.Math::Sqrt(float64)
        add
        ldloc.0
        ldc.r8 0.5e-7
        add
        stloc.0
        ldloc.0
        ldc.r8 1
        bgt END
        br.s LOOP

    END:
        ldc.r8 2e-7
        mul
        call void [mscorlib] System.Console::WriteLine(float64)
        ret
    }
}