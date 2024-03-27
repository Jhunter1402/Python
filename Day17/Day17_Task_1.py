import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
col = ['A', 'B', "C", "D"]
df = pd.DataFrame(np.random.randint(0, 100, size=(3, 4)), columns=col)
print(df)
new_row = np.array([[23, 24, 25, 35]])
new_df = pd.DataFrame(new_row, columns=df.columns)
df = df._append(new_df, ignore_index=True)
print(df)
df = df.drop([0])
print(df)
print(df.plot(kind='pie', subplots=True))
plt.show()
