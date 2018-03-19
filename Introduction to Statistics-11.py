## 1. Introduction to Scales ##

import pandas as pd
car_speeds = [10,20,30,50,20]
earthquake_intensities = [2,7,4,5,8]
mean_car_speed=sum(car_speeds)/len(car_speeds)
mean_earthquake_intensities=sum(earthquake_intensities)/len(earthquake_intensities)

## 2. Discrete and Continuous Scales ##

day_numbers = [1,2,3,4,5,6,7]
snail_crawl_length = [.5,2,5,10,1,.25,4]
cars_in_parking_lot = [5,6,4,2,1,7,8]

import matplotlib.pyplot as plt
plt.plot(day_numbers,snail_crawl_length)
plt.show()
plt.plot(day_numbers,cars_in_parking_lot)
plt.show()

## 3. Understanding Scale Starting Points ##

fahrenheit_degrees = [32, 64, 78, 102]
yearly_town_population = [100,102,103,110,105,120]

degrees_zero=[]

for each in fahrenheit_degrees:
    degrees_zero.append(each+459.67)
    
population_zero=yearly_town_population


## 4. Working With Ordinal Scales ##

# Results from our survey on how many cigarettes people smoke per day
survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]
master_list=["none", "a few", "some", "a lot"]
new_list=[]
for each in survey_responses:
    new_list.append(master_list.index(each))
print(new_list)
new_list=[master_list.index(each) for each in survey_responses]
average_smoking=sum(new_list)/len(new_list)



## 5. Grouping Values with Categorical Scales ##

# Let's say that these lists are both columns in a matrix.  Index 0 is the first row in both, and so on.
gender = ["male", "female", "female", "male", "male", "female"]
savings = [1200, 5000, 3400, 2400, 2800, 4100]
male_list=[]
female_list=[]
for each in savings:
    if gender[savings.index(each)]=="male":
        male_list.append(each)
    else:
        female_list.append(each)
male_savings=sum(male_list)/len(male_list)
female_savings=sum(female_list)/len(female_list)


    

## 6. Visualizing Counts with Frequency Histograms ##

# Let's say that we watch cars drive by and calculate average speed in miles per hour
average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed)
plt.show()

# Let's say we measure student test scores from 0-100
student_scores = [15, 80, 95, 100, 45, 75, 65]
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.hist(student_scores)
fig.show()
import numpy as np
print(np.mean(average_speed))
print(np.median(average_speed))
print(np.std(average_speed))
print(np.var(average_speed))


## 7. Aggregating Values with Histogram Bins ##

average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed, bins=6)
plt.show()

# As you can see, matplotlib groups the values in the list into the nearest bins.
# If we have fewer bins, each bin will have a higher count (because there will be fewer bins to group all of the values into).
# If there are more bins, the total for each one will decrease, because each one will contain fewer values.
plt.hist(average_speed, bins=2)
plt.show()

## 8. Measuring Data Skew ##

# We've already loaded in some numpy arrays. We'll make some plots with them.
# The arrays contain student test scores that are on a 0-100 scale.
import matplotlib.pyplot as plt

# See how there's a long slope to the left?
# The data is concentrated in the right part of the distribution, but some people also scored poorly.
# This plot has a negative skew.
plt.hist(test_scores_negative)
plt.show()

# This plot has a long slope to the right.
# Most students did poorly, but a few did really well.
# This plot has a positive skew.
plt.hist(test_scores_positive)
plt.show()

# This plot has no skew either way. Most of the values are in the center, and there is no long slope either way.
# It is an unskewed distribution.
plt.hist(test_scores_normal)
plt.show()


# We can test how skewed a distribution is using the skew function.
# A positive value means positive skew, a negative value means negative skew, and close to zero means no skew.
from scipy.stats import skew
positive_skew=skew(test_scores_positive)
negative_skew=skew(test_scores_negative)
no_skew=skew(test_scores_normal)



## 9. Checking for Outliers with Kurtosis ##

from scipy.stats import kurtosis
kurt_platy=kurtosis(test_scores_platy)
kurt_lepto=kurtosis(test_scores_lepto)
kurt_meso=kurtosis(test_scores_meso)

## 10. Modality ##

#from scipy.stats import modality
import matplotlib.pyplot as plt

fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.plot(test_scores_multi)
print(test_scores_multi)

## 11. Measures of Central Tendency ##

import matplotlib.pyplot as plt
# Let's put a line over our plot that shows the mean.
# This is the same histogram we plotted for skew a few screens ago.
print(type(test_scores_normal))
plt.hist(test_scores_normal)
# We can use the .mean() method of a numpy array to compute the mean.
mean_test_score = test_scores_normal.mean()
# The axvline function will plot a vertical line over an existing plot.
plt.axvline(mean_test_score)

# Now we can show the plot and clear the figure.
plt.show()

# When we plot test_scores_negative, which is a very negatively skewed distribution, we see that the small values on the left pull the mean in that direction.
# Very large and very small values can easily skew the mean.
# Very skewed distributions can make the mean misleading.
plt.hist(test_scores_negative)
plt.axvline(test_scores_negative.mean())

plt.show()

# We can do the same with the positive side.
# Notice how the very high values pull the mean to the right more than we would expect.
plt.hist(test_scores_positive)
plt.axvline(test_scores_positive.mean())
plt.show()
mean_normal=sum(test_scores_normal)/len(test_scores_normal)
mean_negative=sum(test_scores_negative)/len(test_scores_negative)
mean_positive=sum(test_scores_positive)/len(test_scores_positive)

## 12. Calculating the Median ##

import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.hist(test_scores_positive)
#mean=sum(test_scores_positive)/len(test_scores_positive)
mean=np.mean(test_scores_positive)
#lent=int(len(test_scores_positive)/2 )
#print(test_scores_positive[lent])
#med=(test_scores_positive[lent]+test_scores_positive[lent-1])/2
median=np.median(test_scores_positive)
chart.axvline(median, color="g")
chart.axvline(mean,color="r")
fig.show()

## 14. Removing Missing Data ##

import pandas as pd
file=pd.read_csv("titanic_survival.csv")
print(file.columns)
new_titanic_survival=titanic_survival.dropna(subset=["age","sex"])

## 15. Plotting Age ##

# We've loaded the clean version of the data into the variable new_titanic_survival
import matplotlib.pyplot as plt
import numpy
import pandas as pd
#mean=sum(new_titanic_survival["age"])/len(new_titanic_survival["age"])
#mid_index=int(len(new_titanic_survival)/2)
mean=numpy.mean(new_titanic_survival["age"])
median=numpy.median(new_titanic_survival["age"])
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.hist(new_titanic_survival["age"])
chart.axvline(mean, color="r")
chart.axvline(median, color="g")
fig.show()


## 16. Calculating Indexes for Age ##

import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis

mean_age=np.mean(new_titanic_survival["age"])
median_age=np.median(new_titanic_survival["age"])
skew_age=skew(new_titanic_survival["age"])
kurtosis_age=kurtosis(new_titanic_survival["age"])