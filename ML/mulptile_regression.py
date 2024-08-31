import pandas as pd
from sklearn import linear_model

df = pd.read_csv("./amazon.csv")

# print(df.columns.values)
# print(df.dtypes)


def clean_price(price):
    price = price.replace('₹', '').replace(',', '')
    return float(price)


x = df[["actual_price", "discount_percentage"]]
y = df["discounted_price"]


regr = linear_model.LinearRegression()
regr.fit(x, y)

print(regr)


# print(df.head())
