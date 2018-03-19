## 1. Testing quality of predictions ##

import pandas as pd
import numpy as np
dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
train_df = dc_listings.iloc[0:2792]
test_df = dc_listings.iloc[2792:]

def predict_price(new_listing):
    temp_df = train_df.copy()
    ## Complete the function.
    temp_df["distance"]=abs(new_listing-temp_df["accommodates"])
    temp_df=temp_df.sort_values("distance")
#    print(temp_df.iloc[0:5]["distance"].mean()) #.mean()
    return(temp_df.iloc[0:5]["price"].mean())
test_df["predicted_price"] = test_df["accommodates"].apply(predict_price)
#print(predicted_price)


## 2. Error Metrics ##

import numpy as np
mae=np.absolute(test_df["predicted_price"]-test_df["price"])

## 3. Mean Squared Error ##

import numpy as np
mse=(test_df["predicted_price"]-test_df["price"])**2/len(test_df["predicted_price"])

## 4. Training another model ##

import pandas as pd
import numpy as np
dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
train_df = dc_listings.iloc[0:2792]
test_df = dc_listings.iloc[2792:]

def predict_price(new_listing):
    temp_df = train_df.copy()
    ## Complete the function.
    temp_df["distance"]=abs(new_listing-temp_df["bathrooms"])
    temp_df=temp_df.sort_values("distance")
#    print(temp_df.iloc[0:5]["distance"].mean()) #.mean()
    return(temp_df.iloc[0:5]["price"].mean())
test_df["predicted_price"] = test_df["bathrooms"].apply(predict_price)
mse=(test_df["predicted_price"]-test_df["price"])**2/len(test_df["predicted_price"])


## 5. Root Mean Squared Error ##

import pandas as pd
import numpy as np
dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
train_df = dc_listings.iloc[0:2792]
test_df = dc_listings.iloc[2792:]

def predict_price(new_listing):
    temp_df = train_df.copy()
    ## Complete the function.
    temp_df["distance"]=abs(new_listing-temp_df["bathrooms"])
    temp_df=temp_df.sort_values("distance")
#    print(temp_df.iloc[0:5]["distance"].mean()) #.mean()
    return(temp_df.iloc[0:5]["price"].mean())
test_df["predicted_price"] = test_df["bathrooms"].apply(predict_price)
mse=(test_df["predicted_price"]-test_df["price"])**2/len(test_df["predicted_price"])
rmse=np.sqrt(mse)


## 6. Comparing MAE and RMSE ##

errors_one = pd.Series([5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10])
errors_two = pd.Series([5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 1000])
mae_one = errors_one.sum()/len(errors_one)
rmse_one = np.sqrt((errors_one**2).sum()/len(errors_one))
print(mae_one)
print(rmse_one)

mae_two = errors_two.sum()/len(errors_two)
rmse_two = np.sqrt((errors_two**2).sum()/len(errors_two))
print(mae_two)
print(rmse_two)