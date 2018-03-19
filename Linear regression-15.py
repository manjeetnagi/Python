## 2. Drawing lines ##

import matplotlib.pyplot as plt
import numpy as np

x = np.asarray([0, 1, 2, 3, 4, 5])
y=x-1
fig=plt.figure()
chart1=fig.add_subplot(1,1,1)
chart1.plot(x,y)
plt.show()
y=x+1
fig=plt.figure()
chart1=fig.add_subplot(1,1,1)
chart1.plot(x,y)
plt.show()

## 3. Working with slope ##

import matplotlib.pyplot as plt
import numpy as np

x = np.asarray([0, 1, 2, 3, 4, 5])
# Let's set the slope of the line to 2.
y=x-4*x
fig=plt.figure()
chart1=fig.add_subplot(1,1,1)
chart1.plot(x,y)
plt.show()
y=x/2
fig=plt.figure()
chart1=fig.add_subplot(1,1,1)
chart1.plot(x,y)
plt.show()
y=-2*x
fig=plt.figure()
chart1=fig.add_subplot(1,1,1)
chart1.plot(x,y)
plt.show()

## 4. Starting out with linear regression ##

# The wine quality data is loaded into wine_quality
from numpy import cov

slope_density=np.cov(wine_quality["quality"],wine_quality["density"])/np.var(wine_quality["density"])

## 5. Finishing linear regression ##

from numpy import cov

# This function will take in two columns of data, and return the slope of the linear regression line.
mean_quality=np.mean(wine_quality["quality"])
mean_density=np.mean(wine_quality["density"])
slope_density=np.cov(wine_quality["quality"],wine_quality["density"])/np.var(wine_quality["density"])
intercept_density=mean_quality-(slope_density*mean_density)


## 6. Making predictions ##

from numpy import cov

def calc_m(density, quality):
    nume=np.cov(quality,density)[0,1]
    den=np.var(density)
    m=nume/den
    return(m)

def calc_c(density, quality):
    y_bar=np.mean(quality)
    
    m=calc_m(density,quality)
    
    x_bar=np.mean(density)
    
    return(y_bar-(m*x_bar))

def predict_relan(density, quality):
    m=calc_m(density, quality)
    c=calc_c(density, quality)
    return(m,c)    

return_tuple=predict_relan(wine_quality["density"],wine_quality["quality"])
predicted_quality=(wine_quality["density"]*return_tuple[0])+return_tuple[1]

## 7. Finding error ##

from scipy.stats import linregress

# We've seen the r_value before -- we'll get to what p_value and stderr_slope are soon -- for now, don't worry about them.
#slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])

slope, intercept, r_value, p_vale, stderr_slope=linregress(wine_quality["density"],wine_quality["quality"])
predicted_quality=(slope*wine_quality["density"])+intercept
rss=((predicted_quality-wine_quality["density"])**2)


## 8. Standard error ##

from scipy.stats import linregress
import numpy as np

# We can do our linear regression
# Sadly, the stderr_slope isn't the standard error, but it is the standard error of the slope fitting only
# We'll need to calculate the standard error of the equation ourselves
slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])

predicted_y = np.asarray([slope * x + intercept for x in wine_quality["density"]])
residuals = (wine_quality["quality"] - predicted_y) ** 2
rss = sum(residuals)
stderr = (rss / ((len(wine_quality["quality"]) - 2))) ** .5

def within_percentage(y, predicted_y, stderr, error_count):
    within = stderr * error_count

    differences = abs(predicted_y - y)
    lower_differences = [d for d in differences if d <= within]
    within_count = len(lower_differences)
    return within_count / len(y)

within_one = within_percentage(wine_quality["quality"], predicted_y, stderr, 1)
within_two = within_percentage(wine_quality["quality"], predicted_y, stderr, 2)
within_three = within_percentage(wine_quality["quality"], predicted_y, stderr, 3)