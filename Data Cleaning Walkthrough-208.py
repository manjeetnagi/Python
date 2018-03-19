## 4. Reading in the Data ##

import pandas as pd
ap_2010=pd.read_csv("schools/ap_2010.csv")
class_size=pd.read_csv("schools/class_size.csv")
demographics=pd.read_csv("schools/demographics.csv")
graduation=pd.read_csv("schools/graduation.csv")
hs_directory=pd.read_csv("schools/hs_directory.csv")
sat_results=pd.read_csv("schools/sat_results.csv")

data = {"ap_2010":ap_2010,
       "class_size":class_size,
"demographics":demographics,
"graduation":graduation,
"hs_directory":hs_directory,
"sat_results":sat_results}

## 5. Exploring the SAT Data ##

data["sat_results"].head()

## 6. Exploring the Remaining Data ##

for index, item in data.items():
    print(item.head())


## 8. Reading in the Survey Data ##

import pandas as pd
all_survey=pandas.read_csv("schools/survey_all.txt", delimiter="\t", encoding="windows=1252")
d75_survey=pandas.read_csv("schools/survey_d75.txt", delimiter="\t", encoding="windows=1252")
survey=pd.concat([all_survey, d75_survey], axis=0)



## 9. Cleaning Up the Surveys ##

survey["DBN"]=survey["dbn"]
survey=survey[["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]]
data["survey"]=survey
data["survey"].shape

## 11. Inserting DBN Fields ##

import pandas as pd
data["hs_directory"]["DBN"]=data["hs_directory"]["dbn"]

def pad_csd(row):
    if len(str(row))==1:
        return("0"+str(row))
    if len(str(row))==2:
        return(str(row))

data["class_size"]["padded_csd"]=data["class_size"]["CSD"].apply(pad_csd)
#print(data["class_size"]["padded_csd"])
#print(data["class_size"]["SCHOOLCODE"])

data["class_size"]["DBN"]=data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]

## 12. Combining the SAT Scores ##

data["sat_results"]["SAT Math Avg. Score"]=pandas.to_numeric(data["sat_results"]["SAT Math Avg. Score"], errors="coerce")
data["sat_results"]["SAT Critical Reading Avg. Score"]=pandas.to_numeric(data["sat_results"]["SAT Critical Reading Avg. Score"], errors="coerce")
data["sat_results"]["SAT Writing Avg. Score"]=pandas.to_numeric(data["sat_results"]["SAT Writing Avg. Score"], errors="coerce")

data["sat_results"]["sat_score"]=data["sat_results"]["SAT Math Avg. Score"]+data["sat_results"]["SAT Critical Reading Avg. Score"]+data["sat_results"]["SAT Writing Avg. Score"]


## 13. Parsing Geographic Coordinates for Schools ##

import re

def ret_lat(row):
#    print((re.findall("\(.+\)$",row))[0].split(", ")[0].split("(")[1])
    return((re.findall("\(.+\)$",row))[0].split(", ")[0].split("(")[1])



data["hs_directory"]["lat"]=data["hs_directory"]["Location 1"].apply(ret_lat)

## 14. Extracting the Longitude ##

import re
import pandas as pd

def ret_lon(row):
#    print((re.findall("\(.+\)$",row))[0].split(", ")[1])#.split("(")[1])
    return((re.findall("\(.+\)$",row))[0].split(", ")[1].split(")")[0])



data["hs_directory"]["lon"]=data["hs_directory"]["Location 1"].apply(ret_lon)
data["hs_directory"]["lon"]=pd.to_numeric(data["hs_directory"]["lon"],errors="coerce")
data["hs_directory"]["lat"]=pd.to_numeric(data["hs_directory"]["lat"],errors="coerce")

