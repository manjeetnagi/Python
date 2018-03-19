## 2. Introduction to the Data ##

import pandas as pd
all_ages=pd.read_csv("all-ages.csv")
recent_grads=pd.read_csv("recent-grads.csv")
print(all_ages[0:4])
print(recent_grads[0:4])


## 3. Summarizing Major Categories ##

import pandas as pd
all_ages=pd.read_csv("all-ages.csv")
recent_grads=pd.read_csv("recent-grads.csv")
aa_cat_counts={}
rg_cat_counts={}
ages_cat=all_ages["Major_category"].unique()
for cat in ages_cat:
    aa_cat_counts[cat]=all_ages[all_ages["Major_category"]==cat]["Total"].sum()
grad_cat=recent_grads["Major_category"].unique()
for cat in grad_cat:
    rg_cat_counts[cat]=recent_grads[recent_grads["Major_category"]==cat]["Total"].sum()


## 4. Low-Wage Job Rates ##

import pandas as pd
all_ages=pd.read_csv("all-ages.csv")
recent_grads=pd.read_csv("recent-grads.csv")
low_wage_proportion=recent_grads["Low_wage_jobs"].sum()/recent_grads["Total"].sum()

## 5. Comparing Data Sets ##

import pandas as pd
all_ages=pd.read_csv("all-ages.csv")
recent_grads=pd.read_csv("recent-grads.csv")
uni_majors=recent_grads["Major"].unique()
rg_lower_count=0
for each_major in uni_majors:
    recent_grad_row=(recent_grads[recent_grads["Major"]==each_major]["Unemployment_rate"])
    all_ages_row=(all_ages[all_ages["Major"]==each_major]["Unemployment_rate"])
#    print(recent_grad_row.iloc[0])
#    print(all_ages_row.iloc[0])
    if recent_grad_row.iloc[0] < all_ages_row.iloc[0]:
        rg_lower_count+=1
#print(rg_lower_count)
#print(all_ages["PETROLEUM ENGINEERING"])
#print()