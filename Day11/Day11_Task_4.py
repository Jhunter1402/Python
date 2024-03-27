user_input = input("Enter User Data: ")
with open("output.txt","x") as file:
    file.write(user_input)
    file.write("\n line2")