import json
import pandas as pd
with open("data.json","r") as jsonfile:
    data=json.load(jsonfile)
    df = pd.json_normalize(data)
    print(df)