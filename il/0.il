.assembly extern mscorlib { auto }
.assembly Test {}
.module Test.exe

.namespace Test
{
    .class Person extends [mscorlib] System.Object
    {
        .field private static int32 defaultBirthyear
        .field private int32 birthyear
        .field private string name
        .method private static void .cctor()
        {
            .maxstack 1
            ldc.i4 1500
            stsfld int32 Test.Person::defaultBirthyear
            ret
        }
        .method public instance void .ctor(int32, string)
        {
            .maxstack 2
            ldarg.0
            call instance void [mscorlib] System.Object::.ctor()
            ldarg.0
            ldarg.1
            stfld int32 Test.Person::birthyear
            ldarg.0
            ldarg.2
            stfld string Test.Person::name
            ret
        }
        .method public instance void .ctor(string)
        {
            .maxstack 2
            ldarg.0
            call instance void [mscorlib] System.Object::.ctor()
            ldarg.0
            ldsfld int32 Test.Person::defaultBirthyear
            stfld int32 Test.Person::birthyear
            ldarg.0
            ldarg.1
            stfld string Test.Person::name
            ret
        }
        .method public instance void Say()
        {
            /*
            System.Console.WriteLine(
                String.Concat(
                    new object[] {
                        "我出生于 ",
                        this.birthyear.ToString(),
                        " 年, 名字叫 ",
                        this.name
                    }
                )
            );
            */
            .maxstack 3
            .locals init ([0] string[])
            ldc.i4.4
            newarr string
            stloc.0
            ldloc.0
            ldc.i4.0
            ldstr "我出生于 "
            stelem.ref
            ldloc.0
            ldc.i4.1
            ldarg.0
            ldfld int32 Test.Person::birthyear
            call string [mscorlib] System.Convert::ToString(int32)
            stelem.ref
            ldloc.0
            ldc.i4.2
            ldstr " 年, 名字叫 "
            stelem.ref
            ldloc.0
            ldc.i4.3
            ldarg.0
            ldfld string Test.Person::name
            stelem.ref
            ldloc.0
            call string [mscorlib] System.String::Concat(object[])
            call void [mscorlib] System.Console::WriteLine(string)
            ret
        }
    }
    .method static void Main()
    {
        .entrypoint
        .maxstack 3
        ldc.i4 1000
        ldstr "AA"
        newobj instance void Test.Person::.ctor(int32, string)
        call instance void Test.Person::Say()
        ldstr "CC"
        newobj instance void Test.Person::.ctor(string)
        call instance void Test.Person::Say()
        ret
    }
}
