## 2. Introduction to the Data Set ##

import pandas as pd
data=pd.read_csv("train.csv")
#print(data.loc[0][["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]])
selected_data=data[["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]
titanic=selected_data.dropna()

## 3. Creating Histograms In Seaborn ##

import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(titanic["Age"])
plt.show()

## 4. Generating A Kernel Density Plot ##

import matplotlib.pyplot as plt
import seaborn as sns
sns.kdeplot(titanic["Age"], shade=True)
plt.xlabel("Age")
plt.show()

## 5. Modifying The Appearance Of The Plots ##

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")
sns.kdeplot(titanic["Age"], shade="white")
plt.xlabel("Age")
sns.despine(left=True, bottom=True)

## 6. Conditional Distributions Using A Single Condition ##

import matplotlib.pyplot as plt
import seaborn as sns
g=sns.FacetGrid(titanic,col="Pclass",size=6)
g.map(sns.kdeplot,"Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 7. Creating Conditional Plots Using Two Conditions ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 8. Creating Conditional Plots Using Three Conditions ##

g=sns.FacetGrid(titanic, col="Survived", row="Pclass",hue="Sex", size=3)
g.map(sns.kdeplot,"Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 9. Adding A Legend ##

g=sns.FacetGrid(titanic, col="Survived", row="Pclass",hue="Sex", size=3)
g.map(sns.kdeplot,"Age", shade=True)
g.add_legend()
sns.despine(left=True, bottom=True)
plt.show()