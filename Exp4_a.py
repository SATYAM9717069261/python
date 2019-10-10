class Person:
    def store(sel):
        sel.name=raw_input("Enter your name=> ");
        sel.age=input("Enter age => ")
    def print1(sel):
        print "Name : " + sel.name;
        print "Age : " + str(sel.age);
class Student(Person):
    def __init__(sel):
        sel.store();
        print "Enter Subject Name with Space => ";
        sel.marks={i:raw_input(i+"-> ") for i in raw_input().split() }
    def print2(sel):
        sel.print1();
        print "Marks are \n" + str( sel.marks );

Student1=Student();
Student1.print2();
