## 2. Calculating expected values ##

males_over50k=0.669*0.241*32561
males_under50k=0.669*0.759*32561
females_over50k=0.331*0.241*32561
females_under50k=0.331*0.759*32561


## 3. Calculating chi-squared ##

chisq_gender_income=((5249.8-6662)**2/5249.8)+(((2597.4-1179)**2)/2597.4)+(((16533.5-15128)**2)/16533.5)+(((8180.3-9592)**2)/8180.3)

## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare
observed=np.array([6662,1179,15128,9592])
expected=np.array([5249.8,2597.4,16533.5, 8180.3])
chisquare_value, pvalue_gender_income=chisquare(observed, expected)
print(pvalue_gender_income)

## 5. Cross tables ##

import pandas as pd
table=pd.crosstab(income["sex"], [income["race"]])
print(table)

## 6. Finding expected values ##

import pandas as pd
from scipy.stats import chi2_contingency

chi_value, pvalue_gender_race, df,expected=chi2_contingency(pd.crosstab(income["sex"],[income["race"]]))