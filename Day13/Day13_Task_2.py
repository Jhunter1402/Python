import math
class MathOperations:
    PI = math.pi

    @staticmethod
    def addition(x, y):
        print("Sum of Two numbers: ", x + y)

    @staticmethod
    def subtraction(x, y):
        print("Subtraction of Two numbers: ", x - y)

    @staticmethod
    def multiplication(x, y):
        print("Multiplication of Two numbers: ", x * y)

    @staticmethod
    def division(x, y):
        try:
            print("Division of two numbers: ",x/y)
        except:
            print("Error: Can not Divide a number by Zero")

try:
    x = int (input("Enter First number: "))
    y = int(input("Enter Second Number: "))
    i = int(input("""Select a Arithmetic Operations For below list:
     1. Addition
     2. Subtraction
     3. Multiplication
     4. Division
     Enter Number: """))
    if i == 1:
        MathOperations.addition(x,y)
    elif i == 2:
        MathOperations.subtraction(x,y)
    elif i == 3:
        MathOperations.multiplication(x,y)
    elif i == 4:
        MathOperations.division(x,y)
    else:
        print("Select Operation properly")
except:
    print("Error: Can not enter string")
