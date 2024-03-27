# Write a Python program that takes three numbers as input and prints out the largest among them
i = int(input("Enter First Number: "))
j = int(input("Enter First Number: "))
k = int(input("Enter First Number: "))
if i>j and i>k:
    print( i , "is Lagrest Number")
elif j>i and j>k:
    print( j , "is Lagrest Number")
else:
    print( k , "is Lagrest Number")