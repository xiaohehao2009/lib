using System;
using System.Reflection;

class Person
{
    private string name;
    private int birthYear;

    public Person(string name, int birthYear)
    {
        this.name = name;
        this.birthYear = birthYear;
    }
    public void Say()
    {
        Console.WriteLine($"Person {name}: {birthYear}");
    }
}

class Program
{
    private static void Main()
    {
        Type type = typeof(Person);
        Person ps = (Person)Activator.CreateInstance(type, "KK", 9999);
        ps.Say();
    }
}