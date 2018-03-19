## 3. Setting Line Color Using RGB ##

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("percent-bachelors-degrees-women-usa.csv")

major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']


sp=[0,1,2,3]

fig=plt.figure(figsize=(12,12))

women_color=(0/255,107/255,164/255)
men_color=(255/255,128/255,14/255)

for each in sp:
    chart=fig.add_subplot(2,2,each+1)
    x_values=data["Year"]
    y_values_women=data[major_cats[each]]
    chart.plot(x_values,y_values_women,c=women_color)
    y_values_men=100-data[major_cats[each]]
    chart.plot(x_values,y_values_men,c=men_color)
    chart.set_title(major_cats[each])
    chart.set_xlim(1968,2011)
    chart.set_ylim(0,100)
    chart.spines["right"].set_visible(False)
    chart.spines["left"].set_visible(False)
    chart.spines["top"].set_visible(False)
    chart.spines["bottom"].set_visible(False)
    chart.tick_params(bottom="off",top="off", left="off", right="off")
    if each==3:
        chart.legend(loc="upper right")
fig.show()

## 4. Setting Line Width ##

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("percent-bachelors-degrees-women-usa.csv")

major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']


sp=[0,1,2,3]

fig=plt.figure(figsize=(12,12))

women_color=(0/255,107/255,164/255)
men_color=(255/255,128/255,14/255)

for each in sp:
    chart=fig.add_subplot(2,2,each+1)
    x_values=data["Year"]
    y_values_women=data[major_cats[each]]
    chart.plot(x_values,y_values_women,c=women_color,linewidth=3)
    y_values_men=100-data[major_cats[each]]
    chart.plot(x_values,y_values_men,c=men_color,linewidth=3)
    chart.set_title(major_cats[each])
    chart.set_xlim(1968,2011)
    chart.set_ylim(0,100)
    chart.spines["right"].set_visible(False)
    chart.spines["left"].set_visible(False)
    chart.spines["top"].set_visible(False)
    chart.spines["bottom"].set_visible(False)
    chart.tick_params(bottom="off",top="off", left="off", right="off")
    if each==3:
        chart.legend(loc="upper right")
fig.show()

## 5. Improve the Layout and Ordering ##

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("percent-bachelors-degrees-women-usa.csv")

major_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']

sp=[0,1,2,3,4,5]

fig=plt.figure(figsize=(18,3))

women_color=(0/255,107/255,164/255)
men_color=(255/255,128/255,14/255)

for each in sp:
    chart=fig.add_subplot(1,6,each+1)
    x_values=data["Year"]
    y_values_women=data[major_cats[each]]
    chart.plot(x_values,y_values_women,c=women_color,linewidth=3)
    y_values_men=100-data[major_cats[each]]
    chart.plot(x_values,y_values_men,c=men_color,linewidth=3)
    chart.set_title(major_cats[each])
    chart.set_xlim(1968,2011)
    chart.set_ylim(0,100)
    chart.spines["right"].set_visible(False)
    chart.spines["left"].set_visible(False)
    chart.spines["top"].set_visible(False)
    chart.spines["bottom"].set_visible(False)
    chart.tick_params(bottom="off",top="off", left="off", right="off")
    if each==3:
        chart.legend(loc="upper right")
fig.show()

## 7. Annotating in Matplotlib ##

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("percent-bachelors-degrees-women-usa.csv")

major_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']

sp=[0,1,2,3,4,5]

fig=plt.figure(figsize=(18,3))

women_color=(0/255,107/255,164/255)
men_color=(255/255,128/255,14/255)

for each in sp:
    chart=fig.add_subplot(1,6,each+1)
    x_values=data["Year"]
    y_values_women=data[major_cats[each]]
    chart.plot(x_values,y_values_women,c=women_color,linewidth=3)
    y_values_men=100-data[major_cats[each]]
    chart.plot(x_values,y_values_men,c=men_color,linewidth=3)
    chart.set_title(major_cats[each])
    chart.set_xlim(1968,2011)
    chart.set_ylim(0,100)
    chart.spines["right"].set_visible(False)
    chart.spines["left"].set_visible(False)
    chart.spines["top"].set_visible(False)
    chart.spines["bottom"].set_visible(False)
    chart.tick_params(bottom="off",top="off", left="off", right="off")
#    if each==3:
#        chart.legend(loc="upper right")
    if each==0:
        chart.text(2005,87,"Men")
        chart.text(2002,8,"Women")
    if each==5:
        chart.text(2005,62,"Men")
        chart.text(2001,35,"Women")
fig.show()