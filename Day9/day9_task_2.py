#  Write a python program which randomly prints numbers from range 1 to 500
print("""Enter 1 for Odd numbers and 2 for Even numbers from 1 to 500""")
i = int(input("Number: "))
if i == 1:
    print("Odd numbers from 1 to 500: ")
else:
    print("Even numbers from 1 to 500: ")
while i <= 500:
    print(i)
    i += 2
