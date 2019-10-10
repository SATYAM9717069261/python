class class1:
    def data1(sel):
        sel.a=10;
class class2():
    def data2(sel):
        sel.b = 20;

class multi_inher(class1,class2):
    def data3(sel):
        sel.data1();
        sel.data2();
        sel.result=sel.a+sel.b
    def out(sel):
        print "Result => " + str(sel.result)

Student1=multi_inher();
Student1.data3();
Student1.out();
