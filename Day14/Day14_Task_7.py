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

def function(func, x, y):
    func(x, y)
try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    function(add, x, y)
    function(sub, x, y)
    function(mul, x, y)
    function(div, x, y)
except:
    print("Error: Only 'int' value for both x and y")

