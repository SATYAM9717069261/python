class Exp3:
    name='Satyam'
    salary=10000

    def show(sel):
        print sel.name
        print sel.salary
e1=Exp3()
print getattr(e1,'name')
print hasattr(e1,'name')
print setattr(e1,'name','Satyam Mandal')
print getattr(e1,'name')
print delattr(e1,'salary')
print hasattr(e1,'salary')
