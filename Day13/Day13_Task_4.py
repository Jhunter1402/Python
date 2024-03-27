import math
class GeometryHelper:
    PI = math.pi
    standard_length = 1

    @staticmethod
    def circle_area(radius):
        print("Area of Circle: ", GeometryHelper.PI * radius**2)

    @staticmethod
    def circle_perimeter(radius):
        print("Perimeter Of Circle: ", 2 * GeometryHelper.PI * radius)

    @staticmethod
    def rectangle_area(length, width):
        print("Area of Rectangle: ", length * width)

    @staticmethod
    def rectangle_perimeter(length, width):
        print("Perimeter of Rectangle: ", 2 * (length + width))

    @staticmethod
    def triangle_area(side1,  side2, side3):
        s = (side1 + side2 + side3)/2
        print("Area of Triangle: ", (math.sqrt(s * (s - side1) * (s - side2) * (s - side3))))

    @staticmethod
    def triangle_perimeter(side1, side2, side3):
        print("Perimeter ", side1 + side2 + side3)



r = int(input("Enter Radius of a circle: "))
GeometryHelper.circle_area(r)
GeometryHelper.circle_perimeter(r)

l = int(input("Enter Length of Rectangle: "))
w = int(input("Enter Width of Rectangle: "))
GeometryHelper.rectangle_area(l, w)
GeometryHelper.rectangle_perimeter(l, w)


s1 = int(input("Enter side 1 of a Triangle: "))
s2 = int(input("Enter side 2 of a Triangle: "))
s3 = int(input("Enter side 3 of a Triangle: "))
GeometryHelper.triangle_area(s1, s2, s3)
GeometryHelper.triangle_perimeter(s1, s2, s3)