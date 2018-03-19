## 3. Condensing the Class Size Data Set ##

class_size=data["class_size"]
class_size=class_size[class_size["GRADE "]=="09-12"]
class_size=class_size[class_size["PROGRAM TYPE"]=="GEN ED"]
class_size[0:5]


## 5. Computing Average Class Sizes ##

import numpy as np
import pandas as pd
class_size=class_size.groupby("DBN").agg(np.mean)
class_size=class_size.reset_index()
data["class_size"]=class_size

## 7. Condensing the Demographics Data Set ##

data["demographics"]=data["demographics"][data["demographics"]["schoolyear"]==20112012]


## 9. Condensing the Graduation Data Set ##

data["graduation"]=data["graduation"][data["graduation"]["Cohort"]=="2006"]
data["graduation"]=data["graduation"][data["graduation"]["Demographic"]=="Total Cohort"]

## 10. Converting AP Test Scores ##

import pandas
ap_2010=data["ap_2010"]
cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
ap_2010["AP Test Takers "]=pandas.to_numeric(ap_2010["AP Test Takers "], errors="coerce")
ap_2010["Total Exams Taken"]=pandas.to_numeric(ap_2010["Total Exams Taken"], errors="coerce")
ap_2010["Number of Exams with scores 3 4 or 5"]=pandas.to_numeric(ap_2010["Number of Exams with scores 3 4 or 5"], errors="coerce")

## 12. Performing the Left Joins ##

import pandas as pd
combined = data["sat_results"]
combined=combined.merge(data["ap_2010"], how="left", on="DBN")
combined=combined.merge(data["graduation"], how="left", on="DBN")

## 13. Performing the Inner Joins ##

combined=combined.merge(class_size, how="inner", on="DBN")
combined=combined.merge(data["demographics"], how="inner", on="DBN")
combined=combined.merge(data["survey"], how="inner", on="DBN")
combined=combined.merge(data["hs_directory"], how="inner", on="DBN")


## 15. Filling in Missing Values ##

combined=combined.fillna(combined.mean())
combined=combined.fillna(0)

## 16. Adding a School District Column for Mapping ##

def first_two(row):
    return(row[0:2])
combined["school_dist"]=combined["DBN"].apply(first_two)
