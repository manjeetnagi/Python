## 1. Missing Values ##

import pandas as pd
data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]
print(train.shape)
numerical_train=train.select_dtypes(include=["int","float"])
numerical_train=numerical_train.drop(["PID","Year Built", "Year Remod/Add", "Garage Yr Blt", "Mo Sold", "Yr Sold"], axis=1)
null_series=(numerical_train.isnull().sum())
full_cols_series=null_series[null_series.values==0]


## 2. Correlating Feature Columns With Target Column ##

import pandas as pd
train_subset = train[full_cols_series.index]
sorted_corrs=abs(train_subset.corr().loc["SalePrice"]).sort_values()
print(sorted_corrs)


## 3. Correlation Matrix Heatmap ##

import seaborn as sns
import matplotlib.pyplot as plt

strong_corrs=sorted_corrs[sorted_corrs>0.3]
corrmat=train_subset[strong_corrs.index].corr()
print(corrmat)
sns.heatmap(corrmat)



## 4. Train And Test Model ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'


clean_test=test[final_corr_cols.index].dropna()
lr=LinearRegression()
lr.fit(train[features],train["SalePrice"])
predict_train=lr.predict(train[features])
predict_test=lr.predict(clean_test[features])
train_rmse=mean_squared_error(predict_train,train["SalePrice"])**(1/2)
test_rmse=mean_squared_error(predict_test,clean_test["SalePrice"])**(1/2)


#from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_error
#import numpy as np

## 5. Removing Low Variance Features ##

for each in features:
    min=train[each].min()
    max=train[each].max()
    train[each]=(train[each]-min)/(max-min)

sorted_vars=train[features].var().sort_values()


## 6. Final Model ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
print(sorted_vars)
features=['Wood Deck SF',  'Fireplaces', 'Full Bath',
       '1st Flr SF', 'Garage Area', 'Gr Liv Area', 'Overall Qual']

lr=LinearRegression()
lr.fit(train[features],train["SalePrice"])
predict_train=lr.predict(train[features])
train_rmse_2=mean_squared_error(predict_train,train["SalePrice"])**(1/2)
test_cols=['Wood Deck SF',  'Fireplaces', 'Full Bath',
       '1st Flr SF', 'Garage Area', 'Gr Liv Area', 'Overall Qual',"SalePrice"]
test=test[test_cols].dropna()
print(test.shape)
predict_test=lr.predict(test[features])
test_rmse_2=mean_squared_error(predict_test,test["SalePrice"])**(1/2)

