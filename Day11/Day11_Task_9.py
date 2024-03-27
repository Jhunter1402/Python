import yaml
import pandas as pd
with open("data.yaml","r") as yamlfile:
    data = yaml.safe_load(yamlfile)
    df = pd.DataFrame(data)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    print(df)