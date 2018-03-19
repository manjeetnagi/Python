## 1. Recap ##

import pandas as pd
import numpy as np
np.random.seed(1)

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
print(dc_listings.info())

## 2. Removing features ##

col_list=["accommodates","bedrooms","bathrooms","beds","price","cleaning_fee","security_deposit","minimum_nights","maximum_nights","number_of_reviews",
]
dc_listings=dc_listings[col_list]

## 3. Handling missing values ##

col_list=["accommodates","bedrooms","bathrooms","beds","price","minimum_nights","maximum_nights","number_of_reviews",
]
dc_listings=dc_listings[col_list]
dc_listings=dc_listings.dropna(axis=0, how="any")

## 4. Normalize columns ##

normalized_listings=(dc_listings-dc_listings.mean())/(dc_listings.std())
normalized_listings["price"]=dc_listings["price"]

## 5. Euclidean distance for multivariate case ##

from scipy.spatial import distance
first_row=normalized_listings.iloc[0][["accommodates", "bathrooms"]]
print(first_row)
fifth_row=normalized_listings.iloc[4][["accommodates", "bathrooms"]]
print(fifth_row)
first_fifth_distance=distance.euclidean(fifth_row,first_row)

## 7. Fitting a model and making predictions ##

from sklearn.neighbors import KNeighborsRegressor

train_df=normalized_listings.iloc[0:2792]
test_df=normalized_listings.iloc[2792:]
knn=KNeighborsRegressor(n_neighbors=5, algorithm="brute")
knn.fit(train_df[["accommodates","bathrooms"]],train_df["price"])
predictions=knn.predict(test_df[["accommodates","bathrooms"]])

## 8. Calculating MSE using Scikit-Learn ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn import metrics
import numpy as np

train_df=normalized_listings.iloc[0:2792]
test_df=normalized_listings.iloc[2792:]
knn=KNeighborsRegressor(n_neighbors=5, algorithm="brute")
knn.fit(train_df[["accommodates","bathrooms"]],train_df["price"])
predictions=knn.predict(test_df[["accommodates","bathrooms"]])
two_features_mse=metrics.mean_squared_error(predictions, test_df["price"])
two_features_rmse=(two_features_mse)**(1/2)

## 9. Using more features ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn import metrics
import numpy as np
col_list=["accommodates","bedrooms","bathrooms","number_of_reviews"]
train_df=normalized_listings.iloc[0:2792]
test_df=normalized_listings.iloc[2792:]
knn=KNeighborsRegressor(n_neighbors=5, algorithm="brute")
knn.fit(train_df[col_list],train_df["price"])
four_predictions=knn.predict(test_df[col_list])
four_mse=metrics.mean_squared_error(four_predictions, test_df["price"])
four_rmse=(four_mse)**(1/2)

## 10. Using all features ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn import metrics
import numpy as np
col_list=["accommodates","bedrooms","bathrooms", "beds", "minimum_nights", "maximum_nights","number_of_reviews"]
train_df=normalized_listings.iloc[0:2792]
test_df=normalized_listings.iloc[2792:]
knn=KNeighborsRegressor(n_neighbors=5, algorithm="brute")
knn.fit(train_df[col_list],train_df["price"])
all_features_predictions=knn.predict(test_df[col_list])
all_features_mse=metrics.mean_squared_error(all_features_predictions, test_df["price"])
all_features_rmse=(all_features_mse)**(1/2)