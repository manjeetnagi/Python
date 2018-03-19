## 2. Probability of renting bikes ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

probability_over_4000=bikes[bikes["cnt"]>4000].shape[0]/bikes.shape[0]

## 4. Calculating probabilities ##

# Enter your code here.
coin_1_prob=3/8

## 6. Calculating the number of combinations ##

sunny_1_combinations = 5

## 8. Finding the number of combinations ##

import math
combinations_8=math.factorial(10)/((math.factorial(8))*(math.factorial(2)))
combinations_9=math.factorial(10)/(math.factorial(9))*(math.factorial(1))

## 10. Calculating the probability of one combination ##

prob_combination_3 = (0.7**3)*(0.3**2)

## 12. Function to calculate the probability of a single combination ##

import math
prob_8=(0.6**8)*(0.4**2)*(math.factorial(10))/((math.factorial(2))*(math.factorial(8)))
prob_9=(0.6**9)*(0.4**1)*(math.factorial(10))/((math.factorial(1))*(math.factorial(9)))
prob_10=(0.6**10)*(0.4**0)*(math.factorial(10))/((math.factorial(1))*(math.factorial(10)))