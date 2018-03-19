## 2. The dataset ##

import pandas as pd
votes=pd.read_csv("114_congress.csv")

## 3. Exploring the data ##

import pandas as pd
votes=pd.read_csv("114_congress.csv")
print(votes["party"].value_counts())
print(votes.mean())

## 4. Distance between Senators ##

from sklearn.metrics.pairwise import euclidean_distances

row_1=votes.iloc[0,3:]
row_3=votes.iloc[2,3:]
distance=euclidean_distances(row_3,row_1)



#print(euclidean_distances(votes.iloc[0,3:].reshape(1, -1), votes.iloc[1,3:].reshape(1, -1)))

## 6. Initial clustering ##

import pandas as pd
from sklearn.cluster import KMeans 

model=KMeans(n_clusters=2,random_state=1)
senator_distances=model.fit_transform(votes.iloc[:,3:])


## 7. Exploring the clusters ##

import pandas as pd
from sklearn.cluster import KMeans 

model=KMeans(n_clusters=2,random_state=1)
model.fit_transform(votes.iloc[:,3:])
labels=model.labels_
#votes[labels]=labels
pd.crosstab(labels,votes["party"])


## 8. Exploring Senators in the wrong cluster ##

import pandas as pd
from sklearn.cluster import KMeans 

model=KMeans(n_clusters=2,random_state=1)
model.fit_transform(votes.iloc[:,3:])
labels=model.labels_
print(type(labels))
votes["labels"]=labels
print(votes.shape)
democratic_outliers=votes[(votes["labels"]==1)&(votes["party"]=="D")]
democratic_outliers=democratic_outliers.drop(["labels"],axis=1)


## 9. Plotting out the clusters ##

plt.scatter(x=senator_distances[:,0], y=senator_distances[:,1], c=labels)
plt.show()

## 10. Finding the most extreme ##

extremism = (senator_distances ** 3).sum(axis=1)
votes["extremism"] = extremism
votes.sort_values("extremism", inplace=True, ascending=False)
print(votes.head(10))