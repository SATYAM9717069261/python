def area(num1,num2=None):
    if num2 == None :
        print "area of circle is " + str( 3.14*num1*num1 )
    if num2 != None :
        print "Area of Rectangle is " + str( num1*num2 )

area(12)
area(12,13)
