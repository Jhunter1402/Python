import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self,r):
        self.r=r

    def area(self):
        return math.pi * self.r**2

    def perimeter(self):
        return 2 * math.pi * self.r

class Rectangle(Shape):

    def __init__(self,l,w):
        self.l=l
        self.w=w

    def area(self):
        return self.l * self.w

    def perimeter(self):
        return 2 * (self.l + self.w)

class Triangle(Shape):

    def __init__(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3

    def area(self):
        s=(self.s1 + self.s2 + self.s3)/2
        return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)

r = int(input("Enter Radius of a circle: "))
circle=Circle(r)
print("Area of Circle: ", circle.area())
print("Perimeter of Circle: ", circle.perimeter())

l = int(input("Enter Length of Rectangle: "))
w = int(input("Enter Width of Rectangle: "))
rect = Rectangle(l,w)
print("Area of Rectangle: ", rect.area())
print("Perimeter of Rectangle: ", rect.perimeter())

s = int(input("Enter side of a square: "))
sq = Square(s)
print("Area of Square: ", sq.area())
print("Perimeter of Square: ", sq.perimeter())

s1 = int(input("Enter side 1 of a Triangle: "))
s2 = int(input("Enter side 2 of a Triangle: "))
s3 = int(input("Enter side 3 of a Triangle: "))
tri = Triangle(s1,s2,s3)
print("Area of Triangle: ", tri.area())
print("Perimeter of Triangle: ", tri.perimeter())