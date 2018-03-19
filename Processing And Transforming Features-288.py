## 1. Introduction ##

import pandas as pd
import numpy as np

data=pd.read_csv("AmesHousing.txt",delimiter="\t" )

train=data[0:1460]
test=data[1460:]

train_null_counts=train.isnull().sum()
df_no_mv=train[train_null_counts[train_null_counts==0].index]

## 2. Categorical Features ##


#text_cols = df_no_mv.select_dtypes(include=['object']).columns
text_cols=(df_no_mv.select_dtypes(include=['object']).columns)
for each in text_cols:
    train[each]=train[each].astype('category')
print(train["Utilities"].cat.codes.value_counts())



#for col in text_cols:
#    print(col+":", len(train[col].unique()))

## 3. Dummy Coding ##

dummy_cols = pd.DataFrame()
for each in text_cols:
    col_dummies=pd.get_dummies(train[each])   
    train=pd.concat([train,col_dummies],axis=1)
    del train[each]

## 4. Transforming Improper Numerical Features ##

train["years_until_remod"]=train["Year Remod/Add"]-train["Year Built"]

## 5. Missing Values ##

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

train_null_count=train.isnull().sum()
df_missing_values=train[train_null_count[(train_null_count>0)&(train_null_count<584)].index]

## 6. Imputing Missing Values ##

float_cols=df_missing_values.select_dtypes(include=["float"])
print(float_cols.mean())
float_cols=float_cols.fillna(float_cols.mean())