import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("./Airbnb.csv")
label = df["price"]
data = df.iloc[:, 0:6]
train_data, valid_data, train_label, valid_label = train_test_split(data, label)

model = LinearRegression()
model.fit(train_data, train_label)

result = model.predict(valid_data)
score = mean_squared_error(result, valid_label) ** (1/2)
print(score)