# Write a Python program that takes a password as input and checks its strength based on the following criteria:
# weak (less than 6 characters),
# medium (6 to 10 characters),
# strong (more than 10 characters with a mix of uppercase, lowercase, digits, and special characters)
while True:
    passwd = input("Enter a Password: ")
    l = len(passwd)
    if l < 6:
        print("Entered Password is Weak")
    elif l <=10:
        print("Entered Password is Medium ")
    elif l > 10:
        upper = any(char.isupper() for char in passwd)
        lower = any(char.islower() for char in passwd)
        num = any(char.isnumeric() for char in passwd)
        special = """~`!@#$%^&*()_+-={[}]"|:;'<,>.?/\\"""
        spec = any(char in special for char in passwd)
        if upper and lower and num and spec:
            print("Entred Password is Strong")
            break
        else:
            print("Entred Password must contain at least one uppercase, lowercase, digits, and special characters")


