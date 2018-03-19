## 2. Using Decision Trees With scikit-learn ##

from sklearn.tree import DecisionTreeClassifier

# A list of columns to train with
# We've already converted all columns to numeric
columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

# Instantiate the classifier
# Set random_state to 1 to make sure the results are consistent
clf = DecisionTreeClassifier(random_state=1)
clf.fit(income[columns],income["high_income"])
# We've already loaded the variable "income," which contains all of the income data

## 3. Splitting the Data into Train and Test Sets ##

import numpy as np
import math

numpy.random.seed(1)
new_index=np.random.permutation(income.index)
income=income.reindex(new_index)
train_max_row = math.floor(income.shape[0] * .8)
train=income.iloc[0:train_max_row]
test=income.iloc[train_max_row:]




#train_max_row = math.floor(income.shape[0] * .8)

## 4. Evaluating Error With AUC ##

from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier

clf=DecisionTreeClassifier(random_state=1)
clf.fit(train[columns], train["high_income"])
predictions = clf.predict(test[columns])
error=roc_auc_score(test["high_income"],predictions)
print(error)

## 5. Computing Error on the Training Set ##

from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier

clf.fit(train[columns],train["high_income"])
test_predictions=clf.predict(test[columns])
test_auc=roc_auc_score(test["high_income"],test_predictions)
train_predictions=clf.predict(train[columns])
train_auc=roc_auc_score(train["high_income"], train_predictions)
print(train_auc)

## 7. Reducing Overfitting With a Shallower Tree ##

from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier

clf=DecisionTreeClassifier(random_state=1,min_samples_split=13)
clf.fit(train[columns],train["high_income"])
train_auc=roc_auc_score(train["high_income"],clf.predict(train[columns]))
test_auc=roc_auc_score(test["high_income"],clf.predict(test[columns]))
print(train_auc,test_auc)



## 8. Tweaking Parameters to Adjust AUC ##

from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier

clf=DecisionTreeClassifier(random_state=1,min_samples_split=13, max_depth=7)
clf.fit(train[columns],train["high_income"])
train_auc=roc_auc_score(train["high_income"],clf.predict(train[columns]))
test_auc=roc_auc_score(test["high_income"],clf.predict(test[columns]))
print(train_auc,test_auc)

## 9. Tweaking Tree Depth to Adjust AUC ##

from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier

clf=DecisionTreeClassifier(random_state=1,min_samples_split=100, max_depth=2)
clf.fit(train[columns],train["high_income"])
train_auc=roc_auc_score(train["high_income"],clf.predict(train[columns]))
test_auc=roc_auc_score(test["high_income"],clf.predict(test[columns]))
print(train_auc,test_auc)

## 12. Exploring Decision Tree Variance ##

numpy.random.seed(1)

# Generate a column containing random numbers from 0 to 4
income["noise"] = numpy.random.randint(4, size=income.shape[0])

# Adjust "columns" to include the noise column
columns = ["noise", "age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

# Make new train and test sets
train_max_row = math.floor(income.shape[0] * .8)
train = income.iloc[:train_max_row]
test = income.iloc[train_max_row:]

# Initialize the classifier
clf = DecisionTreeClassifier(random_state=1)
clf.fit(train[columns], train["high_income"])
predictions = clf.predict(test[columns])
test_auc = roc_auc_score(test["high_income"], predictions)

train_predictions = clf.predict(train[columns])
train_auc = roc_auc_score(train["high_income"], train_predictions)

print(test_auc)
print(train_auc)