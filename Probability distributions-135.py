## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")
prob_over_5000=bikes[bikes["cnt"]>5000].shape[0]/bikes.shape[0]

## 4. Computing the distribution ##

import math
import numpy as np
from scipy.stats import binom
from scipy import linspace

def cal_prob(N,k,p,q):
    prob_comb1=(p**(k))*(q**(N-k))
    comb=math.factorial(N)/((math.factorial(k))*(math.factorial(N-k)))
    return(comb*prob_comb1)
p=0.39
q=1-p
N=30
k=0
outcome_probs=[]
for each in np.arange(0,31):
    k=each
    outcome_probs.append(cal_prob(N,k,p,q))
#print(outcome_probs)
# the approach below solves the same problem using the formulae given further down in the exercise
outcome_counts=linspace(0,30,31)
outcome_probs_1=binom.pmf(outcome_counts,30,0.39)
#print(outcome_probs_1)
mean=np.mean(outcome_probs)
mean1=N*p
print(mean, mean1)

## 5. Plotting the distribution ##

import matplotlib.pyplot as plt
import numpy as np
# The most likely number of days is between 10 and 15.
plt.bar(outcome_counts, outcome_probs)
plt.show()

## 6. Simplifying the computation ##

import scipy
import numpy as np
import pandas as pd
from scipy import linspace
from scipy.stats import binom
import matplotlib.pyplot as plt

outcome_counts=linspace(0,30,31)
dist=binom.pmf(outcome_counts,30,0.39)
bar_width=np.arange(31)
bar_hts=dist
plt.bar(bar_width, bar_hts)
print(outcome_counts)
print(dist)
events=[bar_hts][0]*[outcome_counts][0]
print(np.std(events))

## 8. Computing the mean of a probability distribution ##

dist_mean = 30*0.39

## 9. Computing the standard deviation ##

dist_stdev = (30*0.39*0.61)**(1/2)

## 10. A different plot ##

# Enter your answer here.
outcome_counts = linspace(0,10,11)
outcome_probs = binom.pmf(outcome_counts,10,0.39)
plt.bar(outcome_counts, outcome_probs)
plt.show()

outcome_counts = linspace(0,100,101)
outcome_probs = binom.pmf(outcome_counts,100,0.39)
plt.bar(outcome_counts, outcome_probs)
plt.show()

## 11. The normal distribution ##

# Create a range of numbers from 0 to 100, with 101 elements (each number has one entry).
outcome_counts = scipy.linspace(0,100,101)

# Create a probability mass function along the outcome_counts.
outcome_probs = binom.pmf(outcome_counts,100,0.39)

# Plot a line, not a bar chart.
plt.plot(outcome_counts, outcome_probs)
plt.show()

## 12. Cumulative density function ##

outcome_counts = linspace(0,30,31)
dist=binom.cdf(outcome_counts,30,0.39)
plt.plot(dist)

## 14. Faster way to calculate likelihood ##

left_16 = binom.cdf(16,30,0.39)
right_16 = 1-left_16