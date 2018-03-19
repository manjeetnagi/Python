## 2. The Mean as the Center ##

# Make a list of values
values = [2, 4, 5, -1, 0, 10, 8, 9]
import numpy as np
values_median=np.median(values)
median_difference_sum=0
for each in values:
    median_difference_sum=median_difference_sum+each-values_median
print(median_difference_sum)

## 3. Finding Variance ##

import pandas as pd
import numpy as np
df=pd.read_csv("nba_2013.csv")
mean=np.mean(df["pts"])
num=len(df["pts"])

top=0
for each in df["pts"]:
    top=top+((each-mean)**2)
#point_variance=top/num
point_variance=np.var(df["pts"])

## 4. Understanding the Order of Operations ##

# You may be wondering why multiplication and division are on the same level.
# It doesn't matter whether we do the multiplication or division first; the answer here will always be the same.
# In this case, we need to think of division as multiplication by a fraction. Otherwise, we'll be dividing more than we want to.
# Create a formula
a = 5 * 5 / 2
# Multiply by 1/2 instead of dividing by 2. The result is the same (2/2 == 2 * 1/2).
a_subbed = 5 * 5 * 1/2
a_mul_first = 25 * 1/2
a_div_first = 5 * 2.5
print(a_mul_first == a_div_first)

# The same is true for subtraction and addition.
# In this case, we need to convert subtraction into adding a negative number. If we don't we'll end up subtracting more than we expect.
b = 10 - 8 + 5
# Add -8 instead of subtracting 8.
b_subbed = 10 + -8 + 5
b_sub_first = 2 + 5
b_add_first = 10 + -3
print(b_sub_first == b_add_first)
c = (10 * 2) + 5
d = (3 - 1) /( 2 * 2)


## 5. Using Parentheses to Change the Order of Operations ##

a = 50 * 50 - 10 / 5
a_paren = 50 * (50 - 10) / 5
# If we put multiple operations inside parentheses, the interpreter will use the order of operations to determine the sequence in which it should execute them.
a_paren = 50 * (50 - 10 / 5)

b = 10 * (10 + 100)
c = (8 - 6) * 100

## 6. Fractional Powers ##

a = 5 ** 2
# Raise to the fourth power
b = 10 ** 4

# Take the square root ( 3 * 3 == 9, so the answer is 3)
c = 9 ** (1/2)

# Take the cube root (4 * 4 * 4 == 64, so 4 is the cube root)
d = 64 ** (1/3)
e = 11 ** 5
f = 10000 ** (1/4)

## 7. Calculating Standard Deviation ##

# We've already loaded the NBA stats into the nba_stats variable.
import numpy as np
def std_dev(ser):
    lent=len(ser)
    jod=sum(ser)
    mean=jod/lent
    top=0
    for each in ser:
        top=top+((each-mean)**2)
    return((top/lent)**(1/2))

mp_dev=std_dev(nba_stats["mp"])
ast_dev=std_dev(nba_stats["ast"])
mp_dev=np.std(nba_stats["mp"])
ast_dev=np.std(nba_stats["ast"])


## 8. Finding Standard Deviation Distance ##

import matplotlib.pyplot as plt

mean = nba_stats["pf"].mean()
std_dev = nba_stats["pf"].std()
total_distance = nba_stats["pf"][0] - mean
standard_deviation_distance = total_distance / std_dev

point_10_std= (nba_stats["pf"][9]-mean)/std_dev
point_100_std = (nba_stats["pf"][99]-mean)/std_dev

## 9. Working with the Normal Distribution ##

import numpy as np
import matplotlib.pyplot as plt
# The norm module has a pdf function (pdf stands for probability density function)
from scipy.stats import norm

# The arange function generates a numpy vector
# The vector below will start at -1, and go up to, but not including 1
# It will proceed in "steps" of .01.  So the first element will be -1, the second -.99, the third -.98, all the way up to .99.
points = np.arange(-1, 1, 0.01)

# The norm.pdf function will take the points vector and convert it into a probability vector
# Each element in the vector will correspond to the normal distribution (earlier elements and later element smaller, peak in the center)
# The distribution will be centered on 0, and will have a standard devation of .3
probabilities = norm.pdf(points, 0, .3)

# Plot the points values on the x-axis and the corresponding probabilities on the y-axis
# See the bell curve?
plt.plot(points, probabilities)
plt.show()

## 10. Normal Distribution Deviation ##

# Housefly wing lengths in millimeters
import numpy as np
wing_lengths = [36, 37, 38, 38, 39, 39, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 51, 51, 51, 51, 52, 52, 53, 53, 54, 55]


def std_dev(ser):
    lent=len(ser)
    jod=sum(ser)
    mean=jod/lent
    top=0
    for each in ser:
        top=top+((each-mean)**2)
    return((top/lent)**(1/2))

std_dev=std_dev(wing_lengths)
mean=sum(wing_lengths)/len(wing_lengths)
dist_list=[]
for each in wing_lengths:
    dist_list.append(abs(each-mean)/std_dev)

within_one_percentage=0
within_two_percentage=0
within_three_percentage=0
for each in dist_list:
    if each < 1:
        within_one_percentage+=1
    if each <2:
        within_two_percentage+=1
    if each <3:
        within_three_percentage+=1
within_one_percentage=within_one_percentage/len(dist_list)
within_two_percentage=within_two_percentage/len(dist_list)
within_three_percentage=within_three_percentage/len(dist_list)
    

## 11. Using Scatterplots to Plot Correlations ##

import matplotlib.pyplot as plt
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.scatter(nba_stats["stl"], nba_stats["pf"])


## 12. Measuring Correlation with Pearson's r ##

from scipy.stats import pearsonr

r_fta_pts,p_value1=pearsonr(nba_stats["fta"], nba_stats["pts"])
r_stl_pf,p_value2=pearsonr(nba_stats["stl"], nba_stats["pf"])
print(r_fta_pts,p_value1)
print(r_stl_pf,p_value2)


## 13. Calculate Covariance ##

# We've already loaded the nba_stats variable.
def cal_covar(row1,row2):

    lent1=len(row1)
    print(lent1)
    mean1=sum(row1)/lent1
    lent2=len(row2)
    mean2=sum(row2)/lent2
    print(lent2)
    for_range=range(lent1)
    print(for_range)
    out_sum=0
    for each in for_range:
        out_sum=out_sum+(row1[each]-mean1)*(row2[each]-mean2)
    return(out_sum/lent1)

    
cov_stl_pf=cal_covar(nba_stats["stl"], nba_stats["pf"])
cov_fta_pts=cal_covar(nba_stats["fta"], nba_stats["pts"])

## 14. Calculate Correlation With the std() Method ##

from numpy import cov
# We've already loaded the nba_stats variable for you.
r_fta_blk=cov(nba_stats["fta"],nba_stats["blk"])[0,1]/((nba_stats["fta"].std())*(nba_stats["blk"].std()))
r_ast_stl=cov(nba_stats["ast"],nba_stats["stl"])[0,1]/((nba_stats["ast"].std())*(nba_stats["stl"].std()))
