## 1. Shared Indexes ##

import pandas as pd
fandango=pandas.read_csv("fandango_score_comparison.csv")
print(fandango.head(2))
print(fandango.index)

## 2. Using Integer Indexes to Select Rows ##

fandango = pd.read_csv('fandango_score_comparison.csv')

## 3. Using Custom Indexes ##

import pandas as pd
fandango = pd.read_csv('fandango_score_comparison.csv')
fandango_films=fandango.set_index("FILM",drop=False, inplace=False)
print(fandango_films.loc["Do You Believe? (2015)"])

## 4. Using a Custom Index for Selection ##

best_movies_ever=fandango_films.loc[["The Lazarus Effect (2015)","Gett: The Trial of Viviane Amsalem (2015)","Mr. Holmes (2015)"]]

## 5. Apply() Logic Over the Columns in a Dataframe ##

import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))

print(deviations)

## 6. Apply() Logic Over Columns: Practice ##

def halve_each(col):
    return(col/2)
halved_df=float_df.apply(halve_each)
print(halved_df)

## 7. Apply() Over Dataframe Rows ##

sub_set=float_df[["RT_user_norm","Metacritic_user_nom"]]
rt_mt_means=sub_set.apply(lambda x: np.mean(x), axis=1)