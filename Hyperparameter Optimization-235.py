## 1. Recap ##

import pandas as pd
train_df=pd.read_csv("dc_airbnb_train.csv")
test_df=pd.read_csv("dc_airbnb_test.csv")

## 2. Hyperparameter optimization ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
hyper_params=[1,2,3,4,5]
col_list=["accommodates","bedrooms","bathrooms","number_of_reviews"]
mse_values=[]
for each in hyper_params:
    knn=KNeighborsRegressor(n_neighbors=each, algorithm="brute")
    knn.fit(train_df[col_list],train_df["price"])
    test_df["predictions"]=knn.predict(test_df[col_list])
    mse_values.append(mean_squared_error(test_df["predictions"],test_df["price"]))
    
    


## 3. Expanding grid search ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
hyper_params=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
col_list=["accommodates","bedrooms","bathrooms","number_of_reviews"]
mse_values=[]
for each in hyper_params:
    knn=KNeighborsRegressor(n_neighbors=each, algorithm="brute")
    knn.fit(train_df[col_list],train_df["price"])
    test_df["predictions"]=knn.predict(test_df[col_list])
    mse_values.append(mean_squared_error(test_df["predictions"],test_df["price"]))
print(mse_values)

## 4. Visualizing hyperparameter values ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

hyper_params=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
col_list=["accommodates","bedrooms","bathrooms","number_of_reviews"]
mse_values=[]
for each in hyper_params:
    knn=KNeighborsRegressor(n_neighbors=each, algorithm="brute")
    knn.fit(train_df[col_list],train_df["price"])
    test_df["predictions"]=knn.predict(test_df[col_list])
    mse_values.append(mean_squared_error(test_df["predictions"],test_df["price"]))
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.scatter(hyper_params,mse_values)
plt.show()

## 5. Varying features and hyperparameters ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
print(train_df.columns)

hyper_params=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
col_list=["accommodates","bedrooms","bathrooms","beds","minimum_nights","maximum_nights","number_of_reviews"]
mse_values=[]
for each in hyper_params:
    knn=KNeighborsRegressor(n_neighbors=each, algorithm="brute")
    knn.fit(train_df[col_list],train_df["price"])
    test_df["predictions"]=knn.predict(test_df[col_list])
    mse_values.append(mean_squared_error(test_df["predictions"],test_df["price"]))
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.scatter(hyper_params,mse_values)
plt.show()

## 6. Practice the workflow ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
hyper_params=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
two_col_list=["accommodates","bathrooms"]
mse_values=[]
for each in hyper_params:
    knn=KNeighborsRegressor(n_neighbors=each, algorithm="brute")
    knn.fit(train_df[two_col_list],train_df["price"])
    test_df["predictions"]=knn.predict(test_df[two_col_list])
    mse_values.append(mean_squared_error(test_df["predictions"],test_df["price"]))
lowest_mse=mse_values[0]
two_hyp_mse={}
i=0
index=0
for i,each in enumerate(mse_values):
    if each<lowest_mse:
          lowest_mse=each     
          index=i
two_hyp_mse[index+1]=lowest_mse
        
three_col_list=["accommodates","bathrooms","bedrooms"]
mse_values=[]
i=0        
for each in hyper_params:
    knn=KNeighborsRegressor(n_neighbors=each, algorithm="brute")
    knn.fit(train_df[three_col_list],train_df["price"])
    test_df["predictions"]=knn.predict(test_df[three_col_list])
    mse_values.append(mean_squared_error(test_df["predictions"],test_df["price"]))
lowest_mse=mse_values[0]
three_hyp_mse={}
i=0
index=0
for i,each in enumerate(mse_values):
    if each<lowest_mse:
          lowest_mse=each     
          index=i
three_hyp_mse[index+1]=lowest_mse

        
