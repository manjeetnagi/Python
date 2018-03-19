## 3. Bias-variance tradeoff ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

def train_and_test(cols):
    LR=LinearRegression()
    f=filtered_cars[cols].values.reshape(-1,1)
    t=filtered_cars["mpg"].values.reshape(-1,1)
    LR.fit(f,t)
    p=LR.predict(f)
    mse=(mean_squared_error(p,t))
    var=p.var()
    return(mse,var)
cyl_mse,cyl_var=train_and_test("cylinders")
weight_mse,weight_var=train_and_test("weight")

## 4. Multivariate models ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

def train_and_test(cols):
    LR=LinearRegression()
    f=filtered_cars[cols]#.values.reshape(-1,1)
    t=filtered_cars["mpg"]#.values.reshape(-1,1)
    LR.fit(f,t)
    p=LR.predict(f)
    mse=(mean_squared_error(p,t))
    var=p.var()
    return(mse,var)
cols=["cylinders", "displacement"]
two_mse,two_var=train_and_test(cols)

cols=["cylinders", "displacement","horsepower"]
three_mse,three_var=train_and_test(cols)

cols=["cylinders", "displacement","horsepower","weight"]
four_mse,four_var=train_and_test(cols)

cols=["cylinders", "displacement","horsepower","weight","acceleration"]
five_mse,five_var=train_and_test(cols)

cols=["cylinders", "displacement","horsepower","weight","acceleration","model year"]
six_mse,six_var=train_and_test(cols)

cols=["cylinders", "displacement","horsepower","weight","acceleration","model year","origin"]
seven_mse,seven_var=train_and_test(cols)



## 5. Cross validation ##

from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

def train_and_test(cols):
    
    kf=KFold(n=len(filtered_cars),n_folds=10,shuffle=True,random_state=3)
    mse_list=[]
    var_list=[]
    for train_index,test_index in kf:
        train=filtered_cars.iloc[train_index]
        test=filtered_cars.iloc[test_index]
        f_train=train[cols]
        f_test=test[cols]
        t_train=train["mpg"]
        t_test=test["mpg"]
        lr=LinearRegression()
        lr.fit(f_train,t_train)
        p=lr.predict(f_test)
        mse=mean_squared_error(p,t_test)
        var=p.var()
        mse_list.append(mse)
        var_list.append(var)
    
    return(np.mean(mse_list),np.mean(var_list))
cols=["cylinders", "displacement"]
two_mse,two_var=train_and_test(cols)

cols=["cylinders", "displacement","horsepower"]
three_mse,three_var=train_and_test(cols)

cols=["cylinders", "displacement","horsepower","weight"]
four_mse,four_var=train_and_test(cols)

cols=["cylinders", "displacement","horsepower","weight","acceleration"]
five_mse,five_var=train_and_test(cols)

cols=["cylinders", "displacement","horsepower","weight","acceleration","model year"]
six_mse,six_var=train_and_test(cols)

cols=["cylinders", "displacement","horsepower","weight","acceleration","model year","origin"]
seven_mse,seven_var=train_and_test(cols)





## 6. Plotting cross-validation error vs. cross-validation variance ##

# We've hidden the `train_and_cross_val` function to save space but you can still call the function!
import matplotlib.pyplot as plt
        
two_mse, two_var = train_and_cross_val(["cylinders", "displacement"])
three_mse, three_var = train_and_cross_val(["cylinders", "displacement", "horsepower"])
four_mse, four_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight"])
five_mse, five_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration"])
six_mse, six_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year"])
seven_mse, seven_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration","model year", "origin"])
plt.scatter([2,3,4,5,6,7], [two_mse, three_mse, four_mse, five_mse, six_mse, seven_mse], c='red')
plt.scatter([2,3,4,5,6,7], [two_var, three_var, four_var, five_var, six_var, seven_var], c='blue')
plt.show()