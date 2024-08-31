import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./amazon.csv")

print(df)
print(df.head(10))  # by default it provides 5
print(df.tail())
print(df.columns.values)

df.plot()
plt.show()
