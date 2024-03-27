data = "This is a new file."

try:
    with open("newfile.txt", "x") as file:
        file.write(data)
        print("Data has been written to new_file.txt")
except FileExistsError:
    print("Error: File Exists")
