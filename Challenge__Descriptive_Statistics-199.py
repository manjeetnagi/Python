## 1. Introduction ##

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")
fig=plt.figure(figsize=(5,12))
chart1=fig.add_subplot(4,1,1)
chart2=fig.add_subplot(4,1,2)
chart3=fig.add_subplot(4,1,3)
chart4=fig.add_subplot(4,1,4)
chart1.set_xlim(0,5.0)
chart2.set_xlim(0,5.0)
chart3.set_xlim(0,5.0)
chart4.set_xlim(0,5.0)
#chart1.hist(movie_reviews["RT_user_norm"])
movie_reviews["RT_user_norm"].hist(ax=chart1)
movie_reviews["Metacritic_user_nom"].hist(ax=chart2)
movie_reviews["Fandango_Ratingvalue"].hist(ax=chart3)
movie_reviews["IMDB_norm"].hist(ax=chart4)
#chart2.hist(movie_reviews["Metacritic_user_nom"])
#chart3.hist(movie_reviews["Fandango_Ratingvalue"])
#chart4.hist(movie_reviews["IMDB_norm"])
fig.show()


## 2. Mean ##

def calc_mean(series):
    return (series.mean())

col_list=["RT_user_norm", "Metacritic_user_nom", "Fandango_Ratingvalue", "IMDB_norm"]
user_reviews=movie_reviews[col_list]
rt_mean=user_reviews.apply(calc_mean, axis=0)[0]
mc_mean=user_reviews.apply(calc_mean, axis=0)[1]
fg_mean=user_reviews.apply(calc_mean, axis=0)[2]
id_mean=user_reviews.apply(calc_mean, axis=0)[3]



## 3. Variance and standard deviation ##

import numpy as np
def calc_variance(series):
    return(np.var(series))

rt_var=calc_variance(movie_reviews["RT_user_norm"])
rt_stdev=rt_var**(1/2)
mc_var=calc_variance(movie_reviews["Metacritic_user_nom"])
mc_stdev=mc_var**(1/2)
fg_var=calc_variance(movie_reviews["Fandango_Ratingvalue"])
fg_stdev=fg_var**(1/2)
id_var=calc_variance(movie_reviews["IMDB_norm"])
id_stdev=id_var**(1/2)



## 4. Scatter plots ##

import matplotlib.pyplot as plt
fig=plt.figure(figsize=(4,8))
chart1=fig.add_subplot(3,1,1)
chart2=fig.add_subplot(3,1,2)
chart3=fig.add_subplot(3,1,3)
chart1.set_xlim(0,5.0)
chart2.set_xlim(0,5.0)
chart3.set_xlim(0,5.0)
chart1.scatter(movie_reviews["RT_user_norm"],movie_reviews["Fandango_Ratingvalue"])
chart2.scatter(movie_reviews["Metacritic_user_nom"],movie_reviews["Fandango_Ratingvalue"])
chart3.scatter(movie_reviews["IMDB_norm"],movie_reviews["Fandango_Ratingvalue"])
fig.show()

## 5. Covariance ##

import numpy

def calc_covar(series1,series2):
    return(numpy.cov(series1,series2))

rt_fg_covar=calc_covar(movie_reviews["RT_user_norm"],movie_reviews["Fandango_Ratingvalue"] )
mc_fg_covar=calc_covar(movie_reviews["Metacritic_user_nom"],movie_reviews["Fandango_Ratingvalue"])
id_fg_covar=calc_covar(movie_reviews["IMDB_norm"],movie_reviews["Fandango_Ratingvalue"])
    

## 6. Correlation ##

import numpy as np
def calc_variance(series):
    return(np.var(series))

def calc_covariance(series1, series2):
    return(np.cov(series1, series2))
    
def calc_correlation(series1, series2):
    den=((calc_variance(series1))**(1/2))*((calc_variance(series2))**(1/2))
    nume=calc_covariance(series1,series2)
    return(nume/den)

rt_fg_corr=calc_correlation(movie_reviews["RT_user_norm"],movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr=calc_correlation(movie_reviews["Metacritic_user_nom"],movie_reviews["Fandango_Ratingvalue"])
id_fg_corr=calc_correlation(movie_reviews["IMDB_norm"],movie_reviews["Fandango_Ratingvalue"])

