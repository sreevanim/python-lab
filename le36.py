class circle:
    def area(self,r):
        print("Area of circle is :",22/7*r*r)
    def perimeter(self,r):
        print("The perimeter of circle is :",2*22/7*r)
c=circle()
r=int(input("Enter radius of circle:"))
circle.area(c,r)
c.perimeter(r)
