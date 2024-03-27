#Write a Python program that takes a number between 1 and 12 as input and prints the corresponding month name.
months_dict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
i = int(input("Enter a number from 1 to 12: "))
for key,value in months_dict.items():
    if value == i:
        print(key)
        break