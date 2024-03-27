with open("source.txt","r") as file1:
    print("Source File Opened")
    contect = file1.read()
    with open("destination.txt","w") as file2:
        print("Destination File Opened")
        file2.write("This is Destination file \n")
        file2.write(contect)
    print("Destination File Colose")
print("Source File Closed")