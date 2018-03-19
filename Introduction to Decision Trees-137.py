## 2. Overview of the Data Set ##

import pandas

income = pandas.read_csv("income.csv", index_col=False)
print(income.head(5))

## 3. Converting Categorical Variables ##

# Convert a single column from text categories to numbers
col = pandas.Categorical.from_array(income["workclass"])
income["workclass"] = col.codes

col=pandas.Categorical.from_array(income["education"])
income["education"]=col.codes

col=pandas.Categorical.from_array(income["marital_status"])
income["marital_status"]=col.codes

col=pandas.Categorical.from_array(income["occupation"])
income["occupation"]=col.codes

col=pandas.Categorical.from_array(income["relationship"])
income["relationship"]=col.codes

col=pandas.Categorical.from_array(income["race"])
income["race"]=col.codes

col=pandas.Categorical.from_array(income["sex"])
income["sex"]=col.codes

col=pandas.Categorical.from_array(income["native_country"])
income["native_country"]=col.codes

col=pandas.Categorical.from_array(income["high_income"])
income["high_income"]=col.codes



## 5. Creating Splits ##

private_incomes=income[income["workclass"]==4]
public_incomes=income[income["workclass"]!=4]

## 9. Overview of Data Set Entropy ##

import math

col=income["high_income"]

unique_val=col.unique()
print(unique_val)

income_entropy=0

for each in unique_val:
    count_col=col[col==each]
    total_rows=col.shape[0]
    prob=count_col.shape[0]/total_rows
    print(prob)
    income_entropy+=prob*math.log(prob,2)
income_entropy=-1*income_entropy
    
    



#entropy = -(2/5 * math.log(2/5, 2) + 3/5 * math.log(3/5, 2))
#print(entropy)
#prob_0 = income[income["high_income"] == 0].shape[0] / income.shape[0]
#prob_1 = income[income["high_income"] == 1].shape[0] / income.shape[0]
#income_entropy = -(prob_0 * math.log(prob_0, 2) + prob_1 * math.log(prob_1, 2))

## 11. Information Gain ##

import math
import numpy as np

def calc_entropy(ser):
    income_entropy=0
    unique_val=ser.unique()
    for each in unique_val:
        count_each=ser[ser==each]
        total_rows=ser.shape[0]
        prob=count_each.shape[0]/total_rows
        income_entropy+=prob*math.log(prob,2)
    income_entropy=-1*income_entropy
    return(income_entropy)

def calc_partitions(df,col2):
    parts={}
    divider=np.median(df[col2])
    print(divider)
    parts[1]=df[df[col2]<=divider]
    parts[2]=df[df[col2]>divider]
    return(parts)
    


init_entropy=calc_entropy(income["high_income"])

parts=calc_partitions(income,"age")

new_entropy=0
for key,df in parts.items():
    len_1=len(df)
    len_2=len(income)
    new_entropy+=(len_1/len_2)*calc_entropy(df["high_income"])
age_information_gain=init_entropy-new_entropy





## 12. Finding the Best Split ##

import math
import numpy as np

def calc_entropy(ser):
    income_entropy=0
    unique_val=ser.unique()
    for each in unique_val:
        count_each=ser[ser==each]
        total_rows=ser.shape[0]
        prob=count_each.shape[0]/total_rows
        income_entropy+=prob*math.log(prob,2)
    income_entropy=-1*income_entropy
    return(income_entropy)

def calc_partitions(df,col2):
    parts={}
    divider=np.median(df[col2])
#    print(divider)
    parts[1]=df[df[col2]<=divider]
    parts[2]=df[df[col2]>divider]
    return(parts)
    


init_entropy=calc_entropy(income["high_income"])

col_list=["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

information_gains=[]

for col in col_list:
    parts=calc_partitions(income,col)

    new_entropy=0
    for key,df in parts.items():
        len_1=len(df)
        len_2=len(income)
        new_entropy+=(len_1/len_2)*calc_entropy(df["high_income"])
    information_gains.append(init_entropy-new_entropy)
#print(information_gains)
highest_gain_value=information_gains[0]
highest_gain=col_list[0]
print(highest_gain_value,highest_gain)
for index,item in enumerate(col_list):
    print(index,item)
    if information_gains[index]>highest_gain_value:
        print(information_gains[index],highest_gain_value)
        highest_gain=col_list[index]
        highest_gain_value=information_gains[index]
 


