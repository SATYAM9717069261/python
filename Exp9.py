class Exp9:
    counter =1;
    def __init__(self):
        self.name=raw_input("Enter name => ");
        self.age=raw_input("Enter age => ");
        Exp9.counter+=1;
Student1=Exp9()
Student2=Exp9()
print "Total Student "+ str(Exp9.counter-1);
