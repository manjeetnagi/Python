## 2. Introduction to the data ##

import pandas as pd
import matplotlib.pyplot as plt
reviews=pd.read_csv("fandango_scores.csv")
reviews.columns
norm_reviews=reviews[["FILM","RT_user_norm","Metacritic_user_nom","IMDB_norm","Fandango_Ratingvalue","Fandango_Stars"]]
norm_reviews[0:1]

## 4. Creating Bars ##

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
reviews=pd.read_csv("fandango_scores.csv")
norm_reviews=reviews[["RT_user_norm","Metacritic_user_nom","IMDB_norm","Fandango_Ratingvalue","Fandango_Stars"]]

bar_positions=np.arange(5)+0.75
print(bar_positions)
bar_heights=norm_reviews.iloc[0].values
print(bar_heights)
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.bar(bar_positions,bar_heights,width=0.5)
fig.show()

## 5. Aligning Axis Ticks And Labels ##

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
reviews=pd.read_csv("fandango_scores.csv")
col_list=["RT_user_norm","Metacritic_user_nom","IMDB_norm","Fandango_Ratingvalue","Fandango_Stars"]
norm_reviews=reviews[col_list]
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
bar_positions=np.arange(5)+0.75
bar_heights=norm_reviews.iloc[0].values
chart.bar(bar_positions, bar_heights,width=0.5)
chart.set_xticklabels(col_list,rotation=90)
chart.set_xticks([1,2,3,4,5])
chart.set_xlabel("Rating Source")
chart.set_ylabel("Average Rating")
chart.set_title("Average User Rating For Avengers: Age of Ultron (2015)")
fig.show()

## 6. Horizontal Bar Plot ##

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
reviews=pd.read_csv("fandango_scores.csv")
col_list=["RT_user_norm","Metacritic_user_nom","IMDB_norm","Fandango_Ratingvalue","Fandango_Stars"]
norm_reviews=reviews[col_list]
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
bar_heights=norm_reviews.iloc[0][col_list].values
bar_positions=arange(5)+0.75

chart.barh(bar_positions,bar_heights,height=0.5)

tick_positions=(1,2,3,4,5)

chart.set_yticks(tick_positions)
chart.set_yticklabels(col_list)

chart.set_ylabel("Rating Source")
chart.set_xlabel("Average Rating")
chart.set_title("Average User Rating For Avengers: Age of Ultron (2015)")

fig.show()


## 7. Scatter plot ##

import pandas as pd
import matplotlib.pyplot as plt
reviews=pd.read_csv("fandango_scores.csv")
col_list=["Fandango_Ratingvalue","RT_user_norm"]
r_subset=reviews[col_list]
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.scatter(r_subset["Fandango_Ratingvalue"],r_subset["RT_user_norm"])
chart.set_xlabel("Fandango")
chart.set_ylabel("Rotten Tomatoes")
fig.show()

## 8. Switching axes ##

import pandas as pd
import matplotlib.pyplot as plt
reviews=pd.read_csv("fandango_scores.csv")
col_list=["Fandango_Ratingvalue","RT_user_norm"]
r_subset=reviews[col_list]
fig=plt.figure()

chart1=fig.add_subplot(2,1,1)
chart1.scatter(r_subset["Fandango_Ratingvalue"],r_subset["RT_user_norm"])
chart1.set_xlabel("Fandango")
chart1.set_ylabel("Rotten Tomatoes")

chart2=fig.add_subplot(2,1,2)
chart2.scatter(r_subset["RT_user_norm"],r_subset["Fandango_Ratingvalue"])
chart2.set_ylabel("Fandango")
chart2.set_xlabel("Rotten Tomatoes")

fig.show()

## 9. Benchmarking correlation ##

import pandas as pd
import matplotlib.pyplot as plt
reviews=pd.read_csv("fandango_scores.csv")
col_list=["Fandango_Ratingvalue","RT_user_norm","Metacritic_user_nom","IMDB_norm"]
r_subset=reviews[col_list]
fig=plt.figure()

chart1=fig.add_subplot(3,1,1)
chart1.scatter(r_subset["Fandango_Ratingvalue"],r_subset["RT_user_norm"])
chart1.set_xlabel("Fandango")
chart1.set_ylabel("Rotten Tomatoes")
chart1.set_xlim(0,5)
chart1.set_ylim(0,5)

chart2=fig.add_subplot(3,1,2)
chart2.scatter(r_subset["Fandango_Ratingvalue"],r_subset["Metacritic_user_nom"])
chart2.set_xlabel("Fandango")
chart2.set_ylabel("Metacritic")
chart1.set_xlim(0,5)
chart1.set_ylim(0,5)

chart3=fig.add_subplot(3,1,3)
chart3.scatter(r_subset["Fandango_Ratingvalue"],r_subset["IMDB_norm"])
chart3.set_xlabel("Fandango")
chart3.set_ylabel("IMDB")
chart3.set_xlim(0,5)
chart3.set_ylim(0,5)

fig.show()
