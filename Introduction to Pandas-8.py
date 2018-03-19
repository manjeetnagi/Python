## 3. Read in a CSV file ##

import pandas
food_info=pandas.read_csv("food_info.csv")
print(type(food_info))

## 4. Exploring the DataFrame ##

import pandas
food_info=pandas.read_csv("food_info.csv")
first_twenty=food_info.head(20)
#print(first_twenty)
print(food_info.shape)
#print(food_info.columns)
print(food_info.index)


## 7. Selecting a row ##

import pandas
food_info=pandas.read_csv("food_info.csv")
hundredth_row=food_info.loc[99]
print(hundredth_row)


## 8. Data types ##

print(food_info.dtypes)

## 9. Selecting multiple rows ##

import pandas
food_info=pandas.read_csv("food_info.csv")
num_rows=food_info.shape[0]
last_rows=food_info.loc[num_rows-5:num_rows-1]
print(type(food_info.shape))


## 10. Selecting individual columns ##

# Series object.
ndb_col = food_info["NDB_No"]
print(ndb_col)

# Display the type of the column to confirm it's a Series object.
print(type(ndb_col))
saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]

## 11. Selecting multiple columns by name ##

import pandas
food_info=pandas.read_csv("food_info.csv")
selenium_thiamin=food_info[["Selenium_(mcg)","Thiamin_(mg)"]]
print(selenium_thiamin)

## 12. Practice ##

import pandas
food_info=pandas.read_csv("food_info.csv")
col_list=food_info.columns.tolist()
gram_columns=[]
for col in col_list:
    if col.endswith("(g)"):
        gram_columns.append(col)
gram_df=food_info[gram_columns]
print(type(food_info.columns))
    
