## 3. Exploring the Data ##

import pandas as pd
avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
true_avengers=avengers[avengers["Year"]>=1960]

## 5. Consolidating Deaths ##

def death_count(row):
    col_list=["Death1","Death2","Death3","Death4","Death5"]
    count=0
    for c in col_list:
        if row[c]=="YES":
            count+=1
    return(count)
        

true_avengers["Deaths"]=true_avengers.apply(death_count, axis=1)

## 6. Verifying Years Since Joining ##

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def time_lapse(row):
    if (row["Years since joining"]==(2015-row["Year"])):
        return(1)
    else:
        return(0)

true_avengers["joined_accuracy_count"]=true_avengers.apply(time_lapse, axis=1)
joined_accuracy_count=true_avengers["joined_accuracy_count"].sum()
print(joined_accuracy_count)
