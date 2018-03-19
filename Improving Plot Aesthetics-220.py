## 3. Introduction To The Data ##

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("percent-bachelors-degrees-women-usa.csv")
x_values=data["Year"]
y_values=data["Biology"]
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.plot(x_values,y_values)
fig.show()

## 4. Visualizing The Gender Gap ##

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("percent-bachelors-degrees-women-usa.csv")
x_values=data["Year"]
y_values_women=data["Biology"]
y_values_men=100-data["Biology"]

fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.plot(x_values,y_values_women,color="blue",label="Women")
chart.plot(x_values,y_values_men,color="green",label="Men")
chart.set_title("Percentage of Biology Degrees Awarded By Gender")
chart.legend(loc="upper_right")
fig.show()

## 6. Hiding Tick Marks ##

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("percent-bachelors-degrees-women-usa.csv")
x_values=data["Year"]
y_values_women=data["Biology"]
y_values_men=100-data["Biology"]

fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.plot(x_values,y_values_women,color="blue",label="Women")
chart.plot(x_values,y_values_men,color="green",label="Men")
chart.tick_params(bottom="off",top="off", left="off", right="off")
chart.set_title("Percentage of Biology Degrees Awarded By Gender")
chart.legend(loc="upper right")
fig.show()


## 7. Hiding Spines ##

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("percent-bachelors-degrees-women-usa.csv")
x_values=data["Year"]
y_values_women=data["Biology"]
y_values_men=100-data["Biology"]

fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.plot(x_values,y_values_women,color="blue",label="Women")
chart.plot(x_values,y_values_men,color="green",label="Men")
chart.tick_params(bottom="off",top="off", left="off", right="off")
chart.set_title("Percentage of Biology Degrees Awarded By Gender")
chart.legend(loc="upper right")
chart.spines["right"].set_visible(False)
chart.spines["left"].set_visible(False)
chart.spines["top"].set_visible(False)
chart.spines["bottom"].set_visible(False)
fig.show()

## 8. Comparing Gender Gap Across Degree Categories ##

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("percent-bachelors-degrees-women-usa.csv")

major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']


sp=[0,1,2,3]

fig=plt.figure(figsize=(12,12))

for each in sp:
    chart=fig.add_subplot(2,2,each+1)
    x_values=data["Year"]
    y_values_women=data[major_cats[each]]
    chart.plot(x_values,y_values_women,color="blue")
    y_values_men=100-data[major_cats[each]]
    chart.plot(x_values,y_values_men,color="green")
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
    
