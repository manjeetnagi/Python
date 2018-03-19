## 1. Data Structures ##

import pandas as pd
fandango=pd.read_csv("fandango_score_comparison.csv")
print(fandango.head(2))


## 2. Integer Indexes ##

fandango = pd.read_csv('fandango_score_comparison.csv')
series_film=fandango["FILM"]
series_rt=fandango["RottenTomatoes"]
print(list(series_film.index))

## 3. Custom Indexes ##

from pandas import Series
film_names=list(series_film)
film_rt=list(series_rt)
series_custom=Series(film_rt,film_names)
print(series_custom["Avengers: Age of Ultron (2015)"])
print(series_custom.index)

## 4. Integer Index Preservation ##

fiveten=series_custom[5:11]

## 5. Reindexing ##

new_index=sorted(list(series_custom.index))
sorted_by_index=series_custom.reindex(index=new_index)
print(new_index)
print(sorted_by_index)


## 6. Sorting ##

sc2=series_custom.sort_index()
sc3=series_custom.sort_values()


## 7. Transforming Columns With Vectorized Operations ##

series_normalized=series_custom/20

## 8. Comparing and Filtering ##

criteria_one = series_custom > 50
criteria_two = series_custom < 75
both_criteria=series_custom[criteria_one & criteria_two]

## 9. Alignment ##

rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean=(rt_critics+rt_users)/2