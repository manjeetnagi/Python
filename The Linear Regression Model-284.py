## 2. Introduction To The Data ##

import pandas as pd
data=pd.read_csv("AmesHousing.txt", delimiter="\t")
train=data[0:1460]
test=data[1460:]
train.info()
target="SalePrice"


## 3. Simple Linear Regression ##

import matplotlib.pyplot as plt
# For prettier plots.
import seaborn
data=pd.read_csv("AmesHousing.txt", delimiter="\t")
train=data[0:1460]
test=data[1460:]
#train.info()
target="SalePrice"
fig=plt.figure(figsize=(7,15))
chart1=fig.add_subplot(3,1,1)
chart2=fig.add_subplot(3,1,2)
chart3=fig.add_subplot(3,1,3)
train.plot(x="Garage Area", y="SalePrice", ax=chart1,kind="scatter")
train.plot(x="Gr Liv Area", y="SalePrice", ax=chart2,kind="scatter")
train.plot(x="Overall Cond", y="SalePrice", ax=chart3,kind="scatter")
plt.show

## 5. Using Scikit-Learn To Train And Predict ##

from sklearn.linear_model import LinearRegression

lr=LinearRegression()
lr.fit(train["Gr Liv Area"].values.reshape(-1,1),train["SalePrice"].values.reshape(-1,1))
a1=lr.coef_[0]
a0=lr.intercept_[0]



## 6. Making Predictions ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
lr=LinearRegression()
lr.fit(train["Gr Liv Area"].values.reshape(-1,1),train["SalePrice"].values.reshape(-1,1))
a1=lr.coef_[0]
a0=lr.intercept_[0]
predict_train=lr.predict(train["Gr Liv Area"].values.reshape(-1,1))
predict_test=lr.predict(test["Gr Liv Area"].values.reshape(-1,1))
train_rmse=mean_squared_error(predict_train,train["SalePrice"])**(1/2)
test_rmse=mean_squared_error(predict_test,test["SalePrice"])**(1/2)

## 7. Multiple Linear Regression ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
cols = ['Overall Cond', 'Gr Liv Area']
lr=LinearRegression()
lr.fit(train[cols],train["SalePrice"])
predict_train=lr.predict(train[cols])
predict_test=lr.predict(test[cols])
train_rmse_2=mean_squared_error(predict_train,train["SalePrice"])**(1/2)
test_rmse_2=mean_squared_error(predict_test,test["SalePrice"])**(1/2)
