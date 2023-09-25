.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe

.namespace Test
{
    .class abstract beforefieldinit Program
    {
        .method private static hidebysig specialname void Main() il managed
        {
            .entrypoint
            .maxstack 0
            ret
        }
    }
}
