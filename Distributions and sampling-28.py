## 1. Exploring the data ##

# The first 5 rows of the data.
import pandas as pd
df=pd.read_csv("us_income.csv")
lowest_income_county_df=df[df["median_income"]<=min(df["median_income"])]
lowest_income_county=lowest_income_county_df["county"]
df1=df[df["pop_over_25"]>500000]
lowest_income_high_pop_county=df1[df1["median_income"]<=min(df1["median_income"])]["county"]


## 2. Random numbers ##

import random
import numpy as np
# Returns a random integer between the numbers 0 and 10, inclusive.
num = random.randint(0, 10)
print(num)

# Generate a sequence of 10 random numbers between the values of 0 and 10.
random_sequence = [random.randint(0, 10) for _ in range(10)]

# Sometimes, when we generate a random sequence, we want it to be the same sequence whenever the program is run.
# An example is when you use random numbers to select a subset of the data, and you want other people
# looking at the same data to get the same subset.
# We can ensure this by setting a random seed.
# A random seed is an integer that is used to "seed" a random number generator.
# After a random seed is set, the numbers generated after will follow the same sequence.
random.seed(10)
print([random.randint(0,10) for _ in range(5)])
random.seed(10)
# Same sequence as above.
print([random.randint(0,10) for _ in range(5)])
random.seed(11)
# Different seed means different sequence.
print([random.randint(0,10) for _ in range(5)])
random.seed(20)
new_sequence=([random.randint(0,10) for a in range(10)])
print(new_sequence)

## 3. Selecting items from a list ##

# Let's say that we have some data on how much shoppers spend in a store.
shopping = [300, 200, 100, 600, 20]

# We want to sample the data, and only select 4 elements.

random.seed(2)
shopping_sample = random.sample(shopping, 3)

# 4 random items from the shopping list.
print(shopping_sample)

## 4. Population vs sample ##

import matplotlib.pyplot as plt

# A function that returns the result of a die roll.
def roll():
    return random.randint(1, 6)

random.seed(1)
small_sample = [roll() for _ in range(10)]

# Plot a histogram with 6 bins (1 for each possible outcome of the die roll)
plt.hist(small_sample, 6)
plt.show()
random.seed(1)
medium_sample = [roll() for _ in range(100)]

plt.hist(medium_sample, 6)
plt.show()

random.seed(1)
large_sample = [roll() for _ in range(10000)]

plt.hist(large_sample, 6)
plt.show()

## 5. Finding the right sample size ##

def probability_of_one(num_trials, num_rolls):
    """
    This function will take in the number of trials, and the number of rolls per trial.
    Then it will conduct each trial, and record the probability of rolling a one.
    """
    probabilities = []
    for i in range(num_trials):
        die_rolls = [roll() for _ in range(num_rolls)]
        one_prob = len([d for d in die_rolls if d==1]) / num_rolls
        probabilities.append(one_prob)
    return probabilities

random.seed(1)
small_sample = probability_of_one(300, 50)
plt.hist(small_sample, 20)
plt.ylim(0,70)
plt.xlim(0,0.4)
plt.show()
random.seed(1)
medium_sample = probability_of_one(300, 100)
plt.hist(medium_sample, 20)
plt.ylim(0,70)
plt.xlim(0,0.4)
plt.show()

random.seed(1)
large_sample = probability_of_one(300, 1000)
plt.hist(large_sample, 20)
plt.ylim(0,70)
plt.xlim(0,0.4)
plt.show()

## 6. What are the odds? ##

import numpy

large_sample_std = numpy.std(large_sample)
large_sample_mean=numpy.mean(large_sample)
deviations_from_mean=(0.18-large_sample_mean)/large_sample_std
over_18_count=len([p for p in large_sample if p>= 0.18])

## 7. Sampling counties ##

import random
import numpy as np
import pandas as pd

x_values=[]
random.seed(1)
for each in range(1000):
    random_sample=random.sample(range(0,income.shape[0]),100)
    x_values.append(np.mean(income.iloc[random_sample]["median_income"]))
plt.hist(x_values, bins=20)
plt.show()

## 8. An experiment ##

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

mean_ratios=[]

for i in range(1000):
    random_sample=random.sample(range(0,income.shape[0]),100)
    nume=income.iloc[random_sample]["median_income_hs"]
    den=income.iloc[random_sample]["median_income_college"]
    item=nume/den
    mean_ratios.append(np.mean(item))
plt.hist(mean_ratios, bins=20)
plt.show()

## 9. Statistical significance ##

import numpy
import pandas
import random
count=0
for each in mean_ratios:
    if each>=0.675:
        count+=1
significance_value=count/len(mean_ratios)
