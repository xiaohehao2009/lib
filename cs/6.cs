using System;
using System.Reflection;
using System.Reflection.Emit;

namespace Test
{
    class Person
    {
        private string name;
        private int age;
        private int studyLevelNumber;

        private string StudyLevel
        {
            get
            {
                switch (studyLevelNumber)
                {
                    case 0:
                        return "文盲";
                    case 1:
                        return "小学";
                    case 2:
                        return "初中";
                    case 3:
                        return "高中";
                    case 4:
                        return "本科";
                    case 5:
                        return "博士";
                    default:
                        throw new ArgumentOutOfRangeException(
                            "Invalid studyLevelNumber value: " +
                            studyLevelNumber
                        );
                }
            }
        }

        public Person(string name, int age, int studyLevelNumber)
        {
            this.name = name;
            this.age = age;
            this.studyLevelNumber = studyLevelNumber;
        }
        public void ShowInfo()
        {
            Console.WriteLine(
                $"名字: {name}, 年龄: {age}, 学历: {StudyLevel}"
            );
        }
    }
    class Program
    {
        public delegate void StaticMethod<T>(Person instance, T param);
        public static StaticMethod<string> GetChangeName()
        {
            var dm = new DynamicMethod(
                "", null, new Type[] { typeof(Person), typeof(string) },
                typeof(Person)
            );
            var fi = typeof(Person).GetField(
                "name", BindingFlags.NonPublic | BindingFlags.Instance
            );
            var ilg = dm.GetILGenerator();
            ilg.Emit(OpCodes.Ldarg_0);
            ilg.Emit(OpCodes.Ldarg_1);
            ilg.Emit(OpCodes.Stfld, fi);
            ilg.Emit(OpCodes.Ret);
            return (StaticMethod<string>)
                dm.CreateDelegate(typeof(StaticMethod<string>));
        }
        public static StaticMethod<int> GetChangeAge()
        {
            var dm = new DynamicMethod(
                "", null, new Type[] { typeof(Person), typeof(int) },
                typeof(Person)
            );
            var fi = typeof(Person).GetField(
                "age", BindingFlags.NonPublic | BindingFlags.Instance
            );
            var ilg = dm.GetILGenerator();
            ilg.Emit(OpCodes.Ldarg_0);
            ilg.Emit(OpCodes.Ldarg_1);
            ilg.Emit(OpCodes.Stfld, fi);
            ilg.Emit(OpCodes.Ret);
            return (StaticMethod<int>)
                dm.CreateDelegate(typeof(StaticMethod<int>));
        }
        public static StaticMethod<int> GetChangeStudyLevel()
        {
            var dm = new DynamicMethod(
                "", null, new Type[] { typeof(Person), typeof(int) },
                typeof(Person)
            );
            var fi = typeof(Person).GetField(
                "studyLevelNumber",
                BindingFlags.NonPublic | BindingFlags.Instance
            );
            var ilg = dm.GetILGenerator();
            ilg.Emit(OpCodes.Ldarg_0);
            ilg.Emit(OpCodes.Ldarg_1);
            ilg.Emit(OpCodes.Stfld, fi);
            ilg.Emit(OpCodes.Ret);
            return (StaticMethod<int>)
                dm.CreateDelegate(typeof(StaticMethod<int>));
        }
        public static void Main()
        {
            var person = new Person("Peter", 20, 4);
            var chn = GetChangeName();
            var cha = GetChangeAge();
            var chs = GetChangeStudyLevel();
            person.ShowInfo();
            chn(person, "Tom");
            Console.WriteLine("改名");
            person.ShowInfo();
            cha(person, 21);
            Console.WriteLine("改年龄");
            person.ShowInfo();
            chs(person, 3);
            Console.WriteLine("改学历");
            person.ShowInfo();
            chn(person, "Peter");
            cha(person, 20);
            chs(person, 4);
            Console.WriteLine("改回去了!");
            person.ShowInfo();
        }
    }
}
