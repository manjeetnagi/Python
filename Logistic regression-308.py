## 2. Introduction to the data ##

import pandas as pd
import matplotlib.pyplot as plt
adm=pd.read_csv("admissions.csv")
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
x=adm["gpa"]
y=adm["admit"]
chart.scatter(x,y)
plt.show()

## 5. Training a logistic regression model ##

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
adm=pd.read_csv("admissions.csv")

f=adm[["gpa"]]
t=adm["admit"]
print(f.shape)
print(t.shape)
logistic_model=LogisticRegression()
logistic_model.fit(f,t)


## 6. Plotting probabilities ##

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
adm=pd.read_csv("admissions.csv")

f=adm[["gpa"]]
t=adm["admit"]
#print(f.shape)
#print(t.shape)
logistic_model=LogisticRegression()
logistic_model.fit(f,t)
pred_probs=logistic_model.predict_proba(adm[["gpa"]])
print(adm[["gpa"]].shape)
print(pred_probs.shape)
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.scatter(adm[["gpa"]], pred_probs[:,1])
plt.show()

## 7. Predict labels ##

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
adm=pd.read_csv("admissions.csv")

f=adm[["gpa"]]
t=adm["admit"]
logistic_model=LogisticRegression()
logistic_model.fit(f,t)
fitted_labels=logistic_model.predict(adm[["gpa"]])
print(fitted_labels[0:10])
