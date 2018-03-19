## 1. Introduction to Kaggle ##

import pandas as pd

test = pd.read_csv("test.csv")
test_shape = test.shape
train = pd.read_csv("train.csv")
train_shape = train.shape

## 2. Exploring the Data ##

import matplotlib.pyplot as plt
import numpy as np

ClassPivot=train.pivot_table(index="Pclass", values="Survived")
print(type(ClassPivot))
print(ClassPivot.shape)
print(ClassPivot)
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
#ClassPivot.plot.bar()
bar_ht=ClassPivot.values
bar_w=0.5

bar_p=np.arange(ClassPivot.shape[0])+0.75
chart.bar(bar_p,bar_ht,bar_w)
chart.set_xticks(ClassPivot.index)
plt.show()
#print(bar_ht)
#print(bar_w)

## 3. Exploring and Converting the Age Column ##

def process_age(df,cut_points,cut_labels):
    df["Age"]=df["Age"].fillna(-0.5)
    df["Age_categories"]=pd.cut(df["Age"],cut_points,labels=cut_labels)
    return(df)

cut_points=[-1,0,5,12,18,35,60,100]
cut_labels=["Missing","Infant","Child","Teenager","Young Adult","Adult","Senior"]

train=process_age(train,cut_points,cut_labels)
test=process_age(test,cut_points,cut_labels)
train_age_pivot=train.pivot_table(index="Age_categories",values="Survived")
print(train_age_pivot.index)
#train.plot.bar(list(train_age_pivot.index),train_age_pivot.values)
train_age_pivot.plot.bar()

## 4. Preparing our Data for Machine Learning ##

def dummy_func(df,col):
    dummies=pd.get_dummies(df[col],prefix=col)
    df=pd.concat([df,dummies],axis=1)
    return(df)

train=dummy_func(train,"Pclass")
test=dummy_func(test,"Pclass")

train=dummy_func(train,"Sex")
test=dummy_func(test,"Sex")

train=dummy_func(train,"Age_categories")
test=dummy_func(test,"Age_categories")



## 5. Creating Our First Machine Learning Model ##

columns = ['Pclass_1', 'Pclass_2', 'Pclass_3', 'Sex_female', 'Sex_male',
       'Age_categories_Missing','Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior']

from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()
lr.fit(train[columns],train["Survived"])

## 6. Splitting Our Training Data ##

holdout=test
from sklearn.model_selection import train_test_split

columns = ['Pclass_1', 'Pclass_2', 'Pclass_3', 'Sex_female', 'Sex_male',
       'Age_categories_Missing','Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior']

train_X,test_X,train_y,test_y=train_test_split(train[columns],train["Survived"],test_size=0.2, random_state=0)

## 7. Making Predictions and Measuring their Accuracy ##

from sklearn.metrics import accuracy_score

lr.fit(train_X,train_y)
predictions=lr.predict(test_X)
accuracy=accuracy_score(test_y,predictions)

## 8. Using Cross Validation for More Accurate Error Measurement ##

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
import numpy as np

lr=LogisticRegression()
scores=cross_val_score(lr,all_X,all_y,cv=10)
#print(scores)
accuracy=np.mean(scores)


## 9. Making Predictions on Unseen Data ##

columns = ['Pclass_1', 'Pclass_2', 'Pclass_3', 'Sex_female', 'Sex_male',
       'Age_categories_Missing','Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior']
lr = LogisticRegression()
lr.fit(all_X,all_y)
holdout_predictions = lr.predict(holdout[columns])

## 10. Creating a Submission File ##

holdout_ids = holdout["PassengerId"]
submission_df = {"PassengerId": holdout_ids,
                 "Survived": holdout_predictions}
submission = pd.DataFrame(submission_df)

submission.to_csv("submission.csv",index=False)