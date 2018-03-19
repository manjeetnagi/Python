## 1. Probability basics ##

import pandas as pd
import numpy as np
flags=pd.read_csv("flags.csv")
most_bars_country=flags[flags["bars"]==(max(flags["bars"]))]["name"]
highest_population_country=flags[flags["population"]==(max(flags["population"]))]["name"]


## 2. Calculating probability ##

total_countries = flags.shape[0]

stripe_probability=flags[flags["stripes"]>1].shape[0]/flags.shape[0]
orange_probability=flags[flags["orange"]==1].shape[0]/flags.shape[0]

## 3. Conjunctive probabilities ##

ten_heads = .5 ** 10
hundred_heads = .5 ** 100


## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
first_flag=flags[flags["red"]>0].shape[0]
sec_flag=flags[flags["red"]>0].shape[0]-1
third_flag=flags[flags["red"]>0].shape[0]-2
deno1=flags.shape[0]
deno2=flags.shape[0]-1
deno3=flags.shape[0]-2
three_red=(first_flag*sec_flag*third_flag)/(deno1*deno2*deno3)


## 5. Disjunctive probability ##

import numpy as np

count=0
for each in np.arange(1,18001):
    if (each % 70) == 0:
        count+=1
seventy_prob=count/18000
count=0
for each in np.arange(1,18001):
    if (each % 100) == 0:
        count+=1
hundred_prob=count/18000
    


## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None
red=flags[(flags["red"]==1)].shape[0]
orange=flags[(flags["orange"]==1)].shape[0]
red_orange=flags[(flags["red"]==1) & (flags["orange"]==1) & (flags["colors"]>1)].shape[0]
red_or_orange=(red+orange-red_orange)/flags.shape[0]

stripes=flags[(flags["stripes"]>0)].shape[0]
bars=flags[(flags["bars"]>0)].shape[0]
stripes_bars=flags[(flags["stripes"]>0) & (flags["bars"]>0)].shape[0]
stripes_or_bars=(stripes+bars-stripes_bars)/flags.shape[0]


## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None
heads_or=1-((1/2)**3)