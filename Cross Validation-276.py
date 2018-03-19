## 1. Introduction ##

import pandas as pd
import numpy as np
dc_listings=pd.read_csv("dc_airbnb.csv")
new_index=np.random.permutation(dc_listings.index)
dc_listings=dc_listings.reindex(new_index)
dc_listings["price"]=dc_listings["price"].str.replace(",","").str.replace("$","").astype(float)
split_one=dc_listings.iloc[0:1862]
split_two=dc_listings.iloc[1862:]

## 2. Holdout Validation ##

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

dc_listings=pd.read_csv("dc_airbnb.csv")
new_index=np.random.permutation(dc_listings.index)
dc_listings=dc_listings.reindex(new_index)
dc_listings["price"]=dc_listings["price"].str.replace(",","").str.replace("$","").astype(float)
split_one=dc_listings.iloc[0:1862]
split_two=dc_listings.iloc[1862:]

col_list=["accommodates"]

knn=KNeighborsRegressor(algorithm="auto")
knn.fit(split_one[col_list],split_one["price"])
predict=knn.predict(split_two[col_list])
iteration_one_rmse=mean_squared_error(predict,split_two["price"])**(1/2)
print(iteration_one_rmse)

knn=KNeighborsRegressor(algorithm="auto")
knn.fit(split_two[col_list],split_two["price"])
predict=knn.predict(split_one[col_list])
iteration_two_rmse=mean_squared_error(predict,split_one["price"])**(1/2)
print(iteration_two_rmse)
avg_rmse=(iteration_one_rmse+iteration_two_rmse)/2



## 3. K-Fold Cross Validation ##

import numpy as np
import pandas as pd
dc_listings.set_value(dc_listings.index[0:744],"fold",1)
dc_listings.set_value(dc_listings.index[744:1488],"fold",2)
dc_listings.set_value(dc_listings.index[1488:2232],"fold",3)
dc_listings.set_value(dc_listings.index[2232:2976],"fold",4)
dc_listings.set_value(dc_listings.index[2976:3723],"fold",5)
print(dc_listings.index[0:10])
print(dc_listings.iloc[0:10].index)




## 4. First iteration ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
col_list=["accommodates"]
knn=KNeighborsRegressor()
knn.fit(dc_listings[dc_listings["fold"]!=1][col_list],dc_listings[dc_listings["fold"]!=1]["price"])
predict=knn.predict(dc_listings[dc_listings["fold"]==1][col_list])
iteration_one_rmse=mean_squared_error(predict,dc_listings[dc_listings["fold"]==1]["price"])**(1/2)


## 5. Function for training models ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
rmse_list=[]
def train_and_validate(df,k):
    for each in np.arange(1,k+1):
        col_list=["accommodates"]
        knn=KNeighborsRegressor()
        fit_parm1=df[df["fold"]!=each][col_list]
        fit_parm2=df[df["fold"]!=each]["price"]
        knn.fit(fit_parm1,fit_parm2)
        pred_parm=df[df["fold"]==each][col_list]
        predict=knn.predict(pred_parm)
        rmse=mean_squared_error(predict,df[df["fold"]==each]["price"])**(1/2)
        rmse_list.append(rmse)
    return(rmse_list)

rmses=train_and_validate(dc_listings,5)
avg_rmse=np.mean(rmses)

## 6. Performing K-Fold Cross Validation Using Scikit-Learn ##

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import KFold,cross_val_score


kf=KFold(5,shuffle=True,random_state=1)
knn=KNeighborsRegressor()
mses=cross_val_score(knn,dc_listings[["accommodates"]],dc_listings["price"] ,scoring="neg_mean_squared_error", cv=kf)
mses=(np.abs(mses))**(1/2)
avg_rmse=np.mean(mses)