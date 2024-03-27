import csv
from tabulate import tabulate
with open("data.csv","r") as c_data:
    reader = csv.DictReader(c_data)
    data = [row for row in reader]
    print(tabulate(data,headers="keys",tablefmt="simple"))
