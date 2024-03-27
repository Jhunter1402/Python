import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('onlinefoods.csv')
fig, ax_main = plt.subplots(figsize=(10, 5))
df.plot(ax=ax_main, x='Flavor', kind='line', figsize=(10, 5))
ax_main.set_xticks(range(len(df['Flavor'])))
ax_main.set_xticklabels(df['Flavor'], rotation=45)

plt.xlabel('Flavor')
plt.ylabel('Rating')
plt.title('Ice Cream Ratings')

plt.tight_layout()
plt.show()
