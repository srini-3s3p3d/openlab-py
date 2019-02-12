import pandas as pd
data=pd.read_csv("house-price-prediction-train.csv")
print(data)

data.head()

X=data["LotArea"]
Y=data["SalePrice"]
print(X)
print(Y)

import matplotlib.pyplot as plt
plt.plot(X,Y)
plt.show()
