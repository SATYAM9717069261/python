class Person:
    def __init__(self):
        self.name="Satyam"
        self.salary=1000

    def display(self):
        print(self.name)
        print(self.salary)

class Student(Person):
    def __init__(self):
        self.mid_nam="mandal"
        super().__init__()
    def display(self):
        print("Name => " + self.name +self.mid_nam)
        print("Salary => ",self.salary)

Emp1=Person()
Emp1.display()

Student1=Student()
Student1.display()

for i in dir(Person):
    print(i)
