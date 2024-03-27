from calculator import add,sub,mul,div
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
        add(x,y)
    elif i == 2:
        sub(x,y)
    elif i == 3:
        mul(x,y)
    elif i == 4:
        div(x,y)
    else:
        print("Select Operation properly")
except:
    print("Error: Can not enter string")