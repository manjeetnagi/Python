## 4. Determining the Column to Split On ##

import math
import numpy as np

def calc_entropy(ser):
    ser_entropy=0
    unique_val=ser.unique()
    for each in unique_val:
        count_each=ser[ser==each]
        total_rows=ser.shape[0]
        prob=count_each.shape[0]/total_rows
        ser_entropy+=prob*math.log(prob,2)
    ser_entropy=-1*ser_entropy
    return(ser_entropy)

def calc_partitions(full_df,feature):
    parts={}
    divider=np.median(full_df[feature])
#    print(divider)
    parts[1]=full_df[full_df[feature]<=divider]
    parts[2]=full_df[full_df[feature]>divider]
    return(parts)


def find_best_column(full_df,feature_col_list,target_col):
    init_entropy=calc_entropy(full_df[target_col])
#    print(init_entropy)
    information_gains=[]
    for feature in feature_col_list:
#        print("2")
        parts=calc_partitions(full_df,feature)

        new_entropy=0
        
        for key,df_part in parts.items():
#            print("3")
            len_1=len(df_part)
            len_2=len(full_df)
            new_entropy+=(len_1/len_2)*calc_entropy(df_part[target_col])
        information_gains.append(init_entropy-new_entropy)
#    print(information_gains)
    highest_gain_value=information_gains[0]
    highest_gain_feature=feature_col_list[0]
#    print(highest_gain_value,highest_gain)
    for index,feature in enumerate(feature_col_list):
        
        if information_gains[index]>highest_gain_value :
#            print(information_gains[index],highest_gain_value)
            highest_gain_feature=feature_col_list[index]
            highest_gain_value=information_gains[index]
#            print(highest_gain,highest_gain_value)
    return(highest_gain_feature)

col_list=["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]


income_split=find_best_column(income,col_list,"high_income")

## 5. Creating a Simple Recursive Algorithm ##

import math
import numpy as np

def calc_entropy(ser):
    ser_entropy=0
    unique_val=ser.unique()
    for each in unique_val:
        count_each=ser[ser==each]
        total_rows=ser.shape[0]
        prob=count_each.shape[0]/total_rows
        ser_entropy+=prob*math.log(prob,2)
    ser_entropy=-1*ser_entropy
    return(ser_entropy)

def calc_partitions(full_df,feature):
    parts={}
    divider=np.median(full_df[feature])
#    print(divider)
    parts[1]=full_df[full_df[feature]<=divider]
    parts[2]=full_df[full_df[feature]>divider]
    return(parts)


def find_best_column(full_df,feature_col_list,target_col):
    init_entropy=calc_entropy(full_df[target_col])
#    print(init_entropy)
    information_gains=[]
    for feature in feature_col_list:
#        print("2")
        parts=calc_partitions(full_df,feature)

        new_entropy=0
        
        for key,df_part in parts.items():
#            print("3")
            len_1=len(df_part)
            len_2=len(full_df)
            new_entropy+=(len_1/len_2)*calc_entropy(df_part[target_col])
        information_gains.append(init_entropy-new_entropy)
#    print(information_gains)
    highest_gain_value=information_gains[0]
    highest_gain_feature=feature_col_list[0]
#    print(highest_gain_value,highest_gain)
    for index,feature in enumerate(feature_col_list):
        
        if information_gains[index]>highest_gain_value :
#            print(information_gains[index],highest_gain_value)
            highest_gain_feature=feature_col_list[index]
            highest_gain_value=information_gains[index]
#            print(highest_gain,highest_gain_value)
    return(highest_gain_feature)

#static_col_list=["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"


def ye_func(current_df,current_col_list,target_col):
    best_col=find_best_column(current_df,current_col_list,target_col)
    
    median=np.median(current_df[best_col],axis=0)
    
#    print(median)

    left_branch=current_df[current_df[best_col]<=median]
    if len(left_branch[target_col].unique())>1:
        ye_func(left_branch,current_col_list,target_col)
    else:
        append_list(left_branch[target_col])
    
    right_branch=current_df[current_df[best_col]>median]
    if len(right_branch[target_col].unique())>1:
        ye_func(right_branch,current_col_list,target_col)
    else:
        append_list(right_branch[target_col])
          

def append_list(branch):
    if branch.iloc[0]==0:
        for each in np.arange(len(branch)):
                label_0s.append(0)
    if branch.iloc[0]==1:
        for each in np.arange(len(branch)):
                label_1s.append(1)
    

    
data = pandas.DataFrame([
    [0,20,0],
    [0,60,2],
    [0,40,1],
    [1,25,1],
    [1,35,2],
    [1,55,1]
    ])
label_1s=[]
label_0s=[]
data.columns = ["high_income", "age", "marital_status"]
static_col_list=["age","marital_status"]

ye_func(data,static_col_list,"high_income")
print(label_0s)
print(label_1s)


## 7. Storing the Tree ##

import math
import numpy as np

def calc_entropy(ser):
    ser_entropy=0
    unique_val=ser.unique()
    for each in unique_val:
        count_each=ser[ser==each]
        total_rows=ser.shape[0]
        prob=count_each.shape[0]/total_rows
        ser_entropy+=prob*math.log(prob,2)
    ser_entropy=-1*ser_entropy
    return(ser_entropy)

def calc_partitions(full_df,feature):
    parts={}
    divider=np.median(full_df[feature])
#    print(divider)
    parts[1]=full_df[full_df[feature]<=divider]
    parts[2]=full_df[full_df[feature]>divider]
    return(parts)


def find_best_column(full_df,feature_col_list,target_col):
    init_entropy=calc_entropy(full_df[target_col])
#    print(init_entropy)
    information_gains=[]
    for feature in feature_col_list:
#        print("2")
        parts=calc_partitions(full_df,feature)

        new_entropy=0
        
        for key,df_part in parts.items():
#            print("3")
            len_1=len(df_part)
            len_2=len(full_df)
            new_entropy+=(len_1/len_2)*calc_entropy(df_part[target_col])
        information_gains.append(init_entropy-new_entropy)
#    print(information_gains)
    highest_gain_value=information_gains[0]
    highest_gain_feature=feature_col_list[0]
#    print(highest_gain_value,highest_gain)
    for index,feature in enumerate(feature_col_list):
        
        if information_gains[index]>highest_gain_value :
#            print(information_gains[index],highest_gain_value)
            highest_gain_feature=feature_col_list[index]
            highest_gain_value=information_gains[index]
#            print(highest_gain,highest_gain_value)
    return(highest_gain_feature)

#static_col_list=["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"

def ye_func(current_df,current_col_list,target_col,tree,num):

    best_col=find_best_column(current_df,current_col_list,target_col)
    median=np.median(current_df[best_col])
    left_branch=current_df[current_df[best_col] <= median]
    right_branch=current_df[current_df[best_col] > median]
    split_dict = [["left", left_branch], ["right", right_branch]] 

    tree["number"]=num 
    tree["column"]=best_col
    tree["median"]=median
    num=num+1

    
    for name, branch in split_dict:
        tree[name]={}
        
        if len(branch[target_col].unique())>1:
            num=ye_func(branch,current_col_list,target_col,tree[name],num)
        else:

            append_list(branch[target_col])
            tree[name]["label"]=branch[target_col].iloc[0]
            tree[name]["number"]=num
            num=num+1
    return(num)
    
    
    
            
def append_list(branch):
    if branch.iloc[0]==0:
        for each in np.arange(len(branch)):
                label_0s.append(0)
    if branch.iloc[0]==1:
        for each in np.arange(len(branch)):
                label_1s.append(1)

          
data = pandas.DataFrame([
    [0,20,0],
    [0,60,2],
    [0,40,1],
    [1,25,1],
    [1,35,2],
    [1,55,1]
    ])
label_1s=[]
label_0s=[]
data.columns = ["high_income", "age", "marital_status"]
static_col_list=["age","marital_status"]
tree={}
num=1

ye_func(data,static_col_list,"high_income",tree,num)
print(label_0s)
print(label_1s)
print(sorted(tree))
tree0={'column': 'age',
 'left': {'column': 'age',
  'left': {'column': 'age',
   'left': {'label': 0, 'number': 4},
   'median': 22.5,
   'number': 3,
   'right': {'label': 1, 'number': 5}},
  'median': 25.0,
  'number': 2,
  'right': {'label': 1, 'number': 6}},
 'median': 37.5,
 'number': 1,
 'right': {'column': 'age',
  'left': {'column': 'age',
   'left': {'label': 0, 'number': 9},
   'median': 47.5,
   'number': 8,
   'right': {'label': 1, 'number': 10}},
  'median': 55.0,
  'number': 7,
  'right': {'label': 0, 'number': 11}}}
print(tree0==tree)

## 8. Printing Labels for a More Attractive Tree ##

import math
import numpy as np

def calc_entropy(ser):
    ser_entropy=0
    unique_val=ser.unique()
    for each in unique_val:
        count_each=ser[ser==each]
        total_rows=ser.shape[0]
        prob=count_each.shape[0]/total_rows
        ser_entropy+=prob*math.log(prob,2)
    ser_entropy=-1*ser_entropy
    return(ser_entropy)

def calc_partitions(full_df,feature):
    parts={}
    divider=np.median(full_df[feature])
#    print(divider)
    parts[1]=full_df[full_df[feature]<=divider]
    parts[2]=full_df[full_df[feature]>divider]
    return(parts)


def find_best_column(full_df,feature_col_list,target_col):
    init_entropy=calc_entropy(full_df[target_col])
#    print(init_entropy)
    information_gains=[]
    for feature in feature_col_list:
#        print("2")
        parts=calc_partitions(full_df,feature)

        new_entropy=0
        
        for key,df_part in parts.items():
#            print("3")
            len_1=len(df_part)
            len_2=len(full_df)
            new_entropy+=(len_1/len_2)*calc_entropy(df_part[target_col])
        information_gains.append(init_entropy-new_entropy)
#    print(information_gains)
    highest_gain_value=information_gains[0]
    highest_gain_feature=feature_col_list[0]
#    print(highest_gain_value,highest_gain)
    for index,feature in enumerate(feature_col_list):
        
        if information_gains[index]>highest_gain_value :
#            print(information_gains[index],highest_gain_value)
            highest_gain_feature=feature_col_list[index]
            highest_gain_value=information_gains[index]
#            print(highest_gain,highest_gain_value)
    return(highest_gain_feature)

#static_col_list=["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"

def ye_func(current_df,current_col_list,target_col,tree,num):

    best_col=find_best_column(current_df,current_col_list,target_col)
    median=np.median(current_df[best_col])
    left_branch=current_df[current_df[best_col] <= median]
    right_branch=current_df[current_df[best_col] > median]
    split_dict = [["left", left_branch], ["right", right_branch]] 

    tree["number"]=num 
    tree["column"]=best_col
    tree["median"]=median
    num=num+1

    
    for name, branch in split_dict:
        tree[name]={}
        
        if len(branch[target_col].unique())>1:
            num=ye_func(branch,current_col_list,target_col,tree[name],num)
        else:

            append_list(branch[target_col])
            tree[name]["label"]=branch[target_col].iloc[0]
            tree[name]["number"]=num
            num=num+1
    return(num)
    
    
    
            
def append_list(branch):
    if branch.iloc[0]==0:
        for each in np.arange(len(branch)):
                label_0s.append(0)
    if branch.iloc[0]==1:
        for each in np.arange(len(branch)):
                label_1s.append(1)

def print_node(tree,depth):
    
    for key,value in tree.items():
        if type(value)==dict:
#            depth=depth+1
            print_node(value,depth)
            
        else:
            
            if key=="label":
                depth=depth+1
                print(("    "*(depth)),"Leaf: Label", value)
            if key=="median":
                depth=depth+1
                print(("    "*(depth)),"age > ", value)

          
data = pandas.DataFrame([
    [0,20,0],
    [0,60,2],
    [0,40,1],
    [1,25,1],
    [1,35,2],
    [1,55,1]
    ])
label_1s=[]
label_0s=[]
data.columns = ["high_income", "age", "marital_status"]
static_col_list=["age","marital_status"]
tree={}
num=1

ye_func(data,static_col_list,"high_income",tree,num)
depth=0
print_node(tree, depth)

## 10. Making Predictions Automatically ##

import math
import numpy as np

def calc_entropy(ser):
    ser_entropy=0
    unique_val=ser.unique()
    for each in unique_val:
        count_each=ser[ser==each]
        total_rows=ser.shape[0]
        prob=count_each.shape[0]/total_rows
        ser_entropy+=prob*math.log(prob,2)
    ser_entropy=-1*ser_entropy
    return(ser_entropy)

def calc_partitions(full_df,feature):
    parts={}
    divider=np.median(full_df[feature])
#    print(divider)
    parts[1]=full_df[full_df[feature]<=divider]
    parts[2]=full_df[full_df[feature]>divider]
    return(parts)


def find_best_column(full_df,feature_col_list,target_col):
    init_entropy=calc_entropy(full_df[target_col])
#    print(init_entropy)
    information_gains=[]
    for feature in feature_col_list:
#        print("2")
        parts=calc_partitions(full_df,feature)

        new_entropy=0
        
        for key,df_part in parts.items():
#            print("3")
            len_1=len(df_part)
            len_2=len(full_df)
            new_entropy+=(len_1/len_2)*calc_entropy(df_part[target_col])
        information_gains.append(init_entropy-new_entropy)
#    print(information_gains)
    highest_gain_value=information_gains[0]
    highest_gain_feature=feature_col_list[0]
#    print(highest_gain_value,highest_gain)
    for index,feature in enumerate(feature_col_list):
        
        if information_gains[index]>highest_gain_value :
#            print(information_gains[index],highest_gain_value)
            highest_gain_feature=feature_col_list[index]
            highest_gain_value=information_gains[index]
#            print(highest_gain,highest_gain_value)
    return(highest_gain_feature)

#static_col_list=["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"

def ye_func(current_df,current_col_list,target_col,tree,num):

    best_col=find_best_column(current_df,current_col_list,target_col)
    median=np.median(current_df[best_col])
    left_branch=current_df[current_df[best_col] <= median]
    right_branch=current_df[current_df[best_col] > median]
    split_dict = [["left", left_branch], ["right", right_branch]] 

    tree["number"]=num 
    tree["column"]=best_col
    tree["median"]=median
    num=num+1

    
    for name, branch in split_dict:
        tree[name]={}
        
        if len(branch[target_col].unique())>1:
            num=ye_func(branch,current_col_list,target_col,tree[name],num)
        else:

            append_list(branch[target_col])
            tree[name]["label"]=branch[target_col].iloc[0]
            tree[name]["number"]=num
            num=num+1
    return(num)
    
    
    
            
def append_list(branch):
    if branch.iloc[0]==0:
        for each in np.arange(len(branch)):
                label_0s.append(0)
    if branch.iloc[0]==1:
        for each in np.arange(len(branch)):
                label_1s.append(1)

def print_node(tree,depth):
    
    for key,value in tree.items():
        if type(value)==dict:
#            depth=depth+1
            print_node(value,depth)
            
        else:
            
            if key=="label":
                depth=depth+1
                print(("    "*(depth)),"Leaf: Label", value)
            if key=="median":
                depth=depth+1
                print(("    "*(depth)),"age > ", value)

          
data = pandas.DataFrame([
    [0,20,0],
    [0,60,2],
    [0,40,1],
    [1,25,1],
    [1,35,2],
    [1,55,1]
    ])
label_1s=[]
label_0s=[]
data.columns = ["high_income", "age", "marital_status"]
static_col_list=["age","marital_status"]
tree={}
num=1

ye_func(data,static_col_list,"high_income",tree,num)
depth=0

def predict(tree,row):
    if "label" in tree:
        return tree["label"]
    column=tree["column"]
    median=tree["median"]
    if row[column] <= median:
        return predict(tree["left"],row)
    else:
        return predict(tree["right"],row)
print(predict(tree,data.iloc[0]))
    
    
    
    
    
    



## 11. Making Multiple Predictions ##

import math
import numpy as np
import pandas

def calc_entropy(ser):
    ser_entropy=0
    unique_val=ser.unique()
    for each in unique_val:
        count_each=ser[ser==each]
        total_rows=ser.shape[0]
        prob=count_each.shape[0]/total_rows
        ser_entropy+=prob*math.log(prob,2)
    ser_entropy=-1*ser_entropy
    return(ser_entropy)

def calc_partitions(full_df,feature):
    parts={}
    divider=np.median(full_df[feature])
#    print(divider)
    parts[1]=full_df[full_df[feature]<=divider]
    parts[2]=full_df[full_df[feature]>divider]
    return(parts)


def find_best_column(full_df,feature_col_list,target_col):
    init_entropy=calc_entropy(full_df[target_col])
#    print(init_entropy)
    information_gains=[]
    for feature in feature_col_list:
#        print("2")
        parts=calc_partitions(full_df,feature)

        new_entropy=0
        
        for key,df_part in parts.items():
#            print("3")
            len_1=len(df_part)
            len_2=len(full_df)
            new_entropy+=(len_1/len_2)*calc_entropy(df_part[target_col])
        information_gains.append(init_entropy-new_entropy)
#    print(information_gains)
    highest_gain_value=information_gains[0]
    highest_gain_feature=feature_col_list[0]
#    print(highest_gain_value,highest_gain)
    for index,feature in enumerate(feature_col_list):
        
        if information_gains[index]>highest_gain_value :
#            print(information_gains[index],highest_gain_value)
            highest_gain_feature=feature_col_list[index]
            highest_gain_value=information_gains[index]
#            print(highest_gain,highest_gain_value)
    return(highest_gain_feature)

#static_col_list=["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"

def ye_func(current_df,current_col_list,target_col,tree,num):

    best_col=find_best_column(current_df,current_col_list,target_col)
    median=np.median(current_df[best_col])
    left_branch=current_df[current_df[best_col] <= median]
    right_branch=current_df[current_df[best_col] > median]
    split_dict = [["left", left_branch], ["right", right_branch]] 

    tree["number"]=num 
    tree["column"]=best_col
    tree["median"]=median
    num=num+1

    
    for name, branch in split_dict:
        tree[name]={}
        
        if len(branch[target_col].unique())>1:
            num=ye_func(branch,current_col_list,target_col,tree[name],num)
        else:

            append_list(branch[target_col])
            tree[name]["label"]=branch[target_col].iloc[0]
            tree[name]["number"]=num
            num=num+1
    return(num)
    
    
    
            
def append_list(branch):
    if branch.iloc[0]==0:
        for each in np.arange(len(branch)):
                label_0s.append(0)
    if branch.iloc[0]==1:
        for each in np.arange(len(branch)):
                label_1s.append(1)

def print_node(tree,depth):
    
    for key,value in tree.items():
        if type(value)==dict:
#            depth=depth+1
            print_node(value,depth)
            
        else:
            
            if key=="label":
                depth=depth+1
                print(("    "*(depth)),"Leaf: Label", value)
            if key=="median":
                depth=depth+1
                print(("    "*(depth)),"age > ", value)

          
data = pandas.DataFrame([
    [0,20,0],
    [0,60,2],
    [0,40,1],
    [1,25,1],
    [1,35,2],
    [1,55,1]
    ])
label_1s=[]
label_0s=[]
data.columns = ["high_income", "age", "marital_status"]
static_col_list=["age","marital_status"]
tree={}
num=1

ye_func(data,static_col_list,"high_income",tree,num)
depth=0

def predict(tree,row):
    if "label" in tree:
        return tree["label"]
    column=tree["column"]
    median=tree["median"]
    if row[column] <= median:
        return predict(tree["left"],row)
    else:
        return predict(tree["right"],row)
    
def batch_predict(tree, df):
    return df.apply(lambda x: predict(tree, x), axis=1)

new_data = pandas.DataFrame([
    [40,0],
    [20,2],
    [80,1],
    [15,1],
    [27,2],
    [38,1]
    ])
new_data.columns = ["age", "marital_status"]

predictions = batch_predict(tree, new_data)
    
    
    
    

