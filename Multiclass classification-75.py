## 1. Introduction to the data ##

import pandas as pd
cars=pd.read_csv("auto.csv")
unique_regions=cars["origin"].unique()
print(unique_regions)
print(cars.head(5))

## 2. Dummy variables ##


dummy_year=pd.get_dummies(cars["year"], prefix="year")

dummy_cyl=pd.get_dummies(cars["cylinders"], prefix="cyl")

cars=pd.concat([cars,dummy_cyl,dummy_year], axis=1)
cars=cars.drop(["year","cylinders"], axis=1)

print(cars.columns)


## 3. Multiclass classification ##

shuffled_rows=np.random.permutation(cars.index)
shuffled_cars=cars.iloc[shuffled_rows]
print(len(shuffled_cars))
train=shuffled_cars[0:274]
test=shuffled_cars[274:]


## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression

unique_origins=cars["origin"].unique()
unique_origins=np.sort(unique_origins)

shuffled_rows=np.random.permutation(cars.index)
shuffled_cars=cars.iloc[shuffled_rows]

train=shuffled_cars[0:274]
test=shuffled_cars[274:]

features=['cyl_3', 'cyl_4', 'cyl_5', 'cyl_6', 'cyl_8', 'year_70', 'year_71',
       'year_72', 'year_73', 'year_74', 'year_75', 'year_76', 'year_77',
       'year_78', 'year_79', 'year_80', 'year_81', 'year_82']

models={}
for origin in unique_origins:
    target=(train["origin"]==origin)
    model=LogisticRegression()
    model.fit(train[features],train["origin"])
    models[origin]=model
    
    
    
    

## 5. Testing the models ##

from sklearn.linear_model import LogisticRegression

unique_origins=cars["origin"].unique()
unique_origins=np.sort(unique_origins)

shuffled_rows=np.random.permutation(cars.index)
shuffled_cars=cars.iloc[shuffled_rows]

train=shuffled_cars[0:274]
test=shuffled_cars[274:]

features=['cyl_3', 'cyl_4', 'cyl_5', 'cyl_6', 'cyl_8', 'year_70', 'year_71',
       'year_72', 'year_73', 'year_74', 'year_75', 'year_76', 'year_77',
       'year_78', 'year_79', 'year_80', 'year_81', 'year_82']

models={}
test_probs=pd.DataFrame()
print(type(test_probs))
for origin in unique_origins:
    target=(train["origin"]==origin)
    model=LogisticRegression()
    model.fit(train[features],target)
    testing_probs[origin]=model.predict_proba(test[features])[:,1]
    print(testing_probs)
    


## 6. Choose the origin ##

from sklearn.linear_model import LogisticRegression

unique_origins=cars["origin"].unique()
unique_origins=np.sort(unique_origins)

shuffled_rows=np.random.permutation(cars.index)
shuffled_cars=cars.iloc[shuffled_rows]

train=shuffled_cars[0:274]
test=shuffled_cars[274:]

features=['cyl_3', 'cyl_4', 'cyl_5', 'cyl_6', 'cyl_8', 'year_70', 'year_71',
       'year_72', 'year_73', 'year_74', 'year_75', 'year_76', 'year_77',
       'year_78', 'year_79', 'year_80', 'year_81', 'year_82']

models={}
test_probs=pd.DataFrame()
print(type(test_probs))
for origin in unique_origins:
    target=(train["origin"]==origin)
    model=LogisticRegression()
    model.fit(train[features],target)
    print(type(model.predict_proba(test[features])))
    testing_probs[origin]=model.predict_proba(test[features])[:,1]
#    print(testing_probs)
predicted_origins = testing_probs.idxmax(axis=1)
print(predicted_origins)
    
