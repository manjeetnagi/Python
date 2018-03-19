## 3. Tokenizing the Headlines ##

tokenized_headlines=[]
for each in submissions["headline"]:
#    print(each)
     tokenized_headlines.append(each.split(" "))

## 4. Preprocessing Tokens to Increase Accuracy ##

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []
for token in tokenized_headlines:
    token_list=[]
    for word in token:
        word=word.lower()
        for punc in punctuation:
            word=word.replace(punc,"")
        token_list.append(word)
    clean_tokenized.append(token_list)

## 5. Assembling a Matrix of Unique Words ##

import numpy as np
import pandas as pd
unique_tokens = []
single_tokens = []
for token in clean_tokenized:
    for word in token:
        if word not in unique_tokens:
            single_tokens.append(word)
        else:
            if word not in unique_tokens:
                unique_tokens.append(word)
counts=pd.DataFrame(0,index=np.arange(len(clean_tokenized)), columns=unique_tokens)
                

## 6. Counting Token Occurrences ##

# We've already loaded in clean_tokenized and counts
for i,token in enumerate(clean_tokenized):
    for word in token:
        if word in unique_tokens:
            counts.iloc[i][word]+=1

## 7. Removing Columns to Increase Accuracy ##

# We've already loaded in clean_tokenized and counts
# We've already loaded in clean_tokenized and counts
word_counts=counts.sum(axis=0)
counts=counts.loc[:,(word_counts >= 5) & (word_counts <= 100)]


## 9. Making Predictions With fit() ##

from sklearn.linear_model import LinearRegression

clf = LinearRegression()
from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

## 10. Calculating Prediction Error ##

mse = sum((predictions - y_test) ** 2) / len(predictions)