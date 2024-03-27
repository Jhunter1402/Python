def add(x,y):
    print("Addition of Two numbers is ", x+y)
def sub(x,y):
    print("Subtraction of Two numbers is ", x-y)
def mul(x,y):
    print("Multiplication of Two numbers is ", x*y)
def div(x,y):
    try:
        print("Division of Two numbers is ", x/y)
        return ZeroDivisionError
    except(ZeroDivisionError):
        print("Error: Can not divide a number with Zero")
