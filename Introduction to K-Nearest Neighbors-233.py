## 2. Introduction to the data ##

import pandas as pd
dc_listings=pd.read_csv("dc_airbnb.csv")
print(dc_listings.loc[0])

## 4. Euclidean distance ##

import numpy as np
import pandas as pd
dc_listings=pd.read_csv("dc_airbnb.csv")
first_distance=np.sqrt((dc_listings.loc[0]["accommodates"]-3)**2)


## 5. Calculate distance for all observations ##

import pandas as pd
import numpy as np
dc_listings=pd.read_csv("dc_airbnb.csv")

def cal_dist(dist):
    return(np.abs(dist-3))

dc_listings["distance"]=dc_listings["accommodates"].apply(cal_dist)


## 6. Randomizing, and sorting ##

import numpy as np
np.random.seed(1)
dc_listings=dc_listings.loc[np.random.permutation(dc_listings.shape[0])]
dc_listings=dc_listings.sort_values(by=["distance"])

## 7. Average price ##

mean_price=dc_listings["price"]=dc_listings["price"].str.replace(",","").str.replace("$","").astype(float)[0:5].mean()



## 8. Function to make predictions ##

# Brought along the changes we made to the `dc_listings` Dataframe.
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

def predict_price(new_listing):
    temp_df = dc_listings.copy()
    ## Complete the function.
    temp_df["distance"]=abs(new_listing-temp_df["accommodates"])
    temp_df=temp_df.sort_values("distance")
#    print(temp_df.iloc[0:5]["distance"].mean()) #.mean()
    return(temp_df.iloc[0:5]["price"].mean())
acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)