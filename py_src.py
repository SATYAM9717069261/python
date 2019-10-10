class student:
    def __init__(sel):
        sel.mark={i:raw_input(i+"->") for i in raw_input().split() }

    def print_detail(sel):
        print sel.mark

Studen_t=raw_input("Enter Student name=> ")
Student=Studen_t
Student=student()
print "Student name=> " , Studen_t 
Student.print_detail()
