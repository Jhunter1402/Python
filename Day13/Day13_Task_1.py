class FileUtility:
    @staticmethod
    def file_reading():
        file_name = input("Enter File Name: ")
        try:
            with open(file_name,"r") as file:
                data = file.read()
                print(data)
        except:
            print("Error: File Not Found")

    @staticmethod
    def file_writing():
        file_name = input("Enter File Name: ")
        with open(file_name,"w") as file:
            data = input("Enter Data: ")
            file.write(data)
        print("Data is inserted in to File")

    @staticmethod
    def file_copying():
        try:
            file_1 = input("Enter Source File: ")
            with open(file_1, "r") as file1:
                data = file1.read()
                file_2 = input("Enter Destination File: ")
                with open(file_2, "w") as file2:
                    file2.write(data)
            print("Copying the data is completed")

        except:
            print("Error: Source File Not Found")
try:
    op = int(input("""Operations:
    1. Reading data from a file.
    2. Writing data to a file
    3. Copying data from one file to another.
    Enter Operation you want to perform: """))
    if op == 1:
        FileUtility.file_reading()
    elif op == 2:
        FileUtility.file_writing()
    elif op == 3:
        FileUtility.file_copying()
    else:
        print("Enter correct Operation number")
except:
    print("Error: Can not Enter a String")
finally:
    print("File Utility Program Ended.")
