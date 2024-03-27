import csv
with open("data.csv","a") as csv_file:
    name=input("Enter Name: ")
    age=input("Enter Age: ")
    email=input("Enter Email: ")
    data=""
    data=data+name+","+age+","+email+"\n"
    csv_file.write(data)
    print("Data is Entred to File")