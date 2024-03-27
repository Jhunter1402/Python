import json
import yaml
import csv
import pandas as pd
from tabulate import tabulate
class ConfigParser():
    json_path = "test.json"
    yaml_path = "test.yaml"
    csv_path = "test.csv"

    @staticmethod
    def json_parsing(path = None):
        if path == None:
            file_path = ConfigParser.json_path
        else:
            file_path = path
        try:
            with open(file_path, "r") as jsonfile:
                data = json.load(jsonfile)
                df = pd.json_normalize(data)
                print(df)
        except:
            print("Error: File Not Found")

    @staticmethod
    def yaml_parsing(path=None):
        if path == None:
            file_path = ConfigParser.yaml_path
        else:
            file_path = path
        try:
            with open(file_path, "r") as yamlfile:
                data = yaml.safe_load(yamlfile)
                df = pd.DataFrame(data)
                pd.set_option('display.max_rows', None)
                pd.set_option('display.max_columns', None)
                print(df)
        except:
            print("Error: File Not Found")
    @staticmethod
    def csv_parsing(path=None):
        if path == None:
            file_path = ConfigParser.csv_path
        else:
            file_path = path
        try:
            with open(file_path, "r") as c_data:
                reader = csv.DictReader(c_data)
                data = [row for row in reader]
                print(tabulate(data, headers="keys", tablefmt="simple"))
        except:
            print("Error: File Not Found")

pt = input("Enter file name or path: ")
if len(pt) == 0:
    path = None
else:
    path = pt

print("""File Parsing Operation: 
1. json File
2. yaml File
3. csv File /n """)
i = int(input("Enter Operation Number: "))
if i == 1:
    ConfigParser.json_parsing(path)
elif i == 2:
    ConfigParser.yaml_parsing(path)
elif i == 3:
    ConfigParser.csv_parsing(path)
else:
    print("Enter Operation Number Properly.")

