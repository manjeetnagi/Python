## 2. Frequency Distribution ##

fandango_distribution=norm_reviews["Fandango_Ratingvalue"].value_counts().sort_index()
imdb_distribution=norm_reviews["IMDB_norm"].value_counts().sort_index()



## 4. Histogram In Matplotlib ##

import matplotlib.pyplot as plt
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.hist(norm_reviews["Fandango_Ratingvalue"], range=(0,5))
fig.show()

## 5. Comparing histograms ##

import matplotlib.pyplot as plt
fig=plt.figure()
chart1=fig.add_subplot(5,1,1)
chart1.hist(norm_reviews["Fandango_Ratingvalue"],bins=20,range=(0,5))
chart1.set_title("Distribution of Fandango Ratings")
chart1.set_ylim(0,50)

chart2=fig.add_subplot(5,1,2)
chart2.hist(norm_reviews["RT_user_norm"],bins=20,range=(0,5))
chart2.set_title("Distribution of Rotten Tomatoes Ratings")
chart2.set_ylim(0,50)

chart3=fig.add_subplot(5,1,3)
chart3.hist(norm_reviews["Metacritic_user_nom"],bins=20,range=(0,5))
chart3.set_title("Distribution of Metacritic Ratings")
chart3.set_ylim(0,50)

chart4=fig.add_subplot(5,1,4)
chart4.hist(norm_reviews["Metacritic_user_nom"],bins=20,range=(0,5))
chart4.set_title("Distribution of Metacritic Ratings")
chart4.set_ylim(0,50)

chart5=fig.add_subplot(5,1,5)
chart5.hist(norm_reviews["IMDB_norm"],bins=20,range=(0,5))
chart5.set_title("Distribution of IMDB Ratings")
chart5.set_ylim(0,50)

fig.show()

## 7. Box Plot ##

import matplotlib.pyplot as plt
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.boxplot(norm_reviews["RT_user_norm"])
chart.set_ylim(0,5)
chart.set_xticks([1])
chart.set_xticklabels(["Rotten Tomatoes"])
fig.show()

## 8. Multiple Box Plots ##

import matplotlib.pyplot as plt






num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.boxplot(norm_reviews[num_cols].values)
chart.set_xticks([1,2,3,4])
chart.set_xticklabels(num_cols,rotation=90)
chart.set_ylim(0,5)
fig.show()