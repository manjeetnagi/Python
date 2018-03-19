## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt

unrate=pd.read_csv("unrate.csv")
unrate["DATE"]=pd.to_datetime(unrate["DATE"])
x_values=unrate["DATE"][0:12]
y_values=unrate["VALUE"][0:12]
plt.plot(x_values,y_values)
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")

## 3. Matplotlib Classes ##

import matplotlib.pyplot as plt
fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
plt.show()

## 5. Adding Data ##

import pandas as pd
import matplotlib.pyplot as plt
unrate=pd.read_csv("unrate.csv")
unrate["DATE"]=pd.to_datetime(unrate["DATE"])
x_values=unrate[0:12]["DATE"]
y_values=unrate[0:12]["VALUE"]
fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
ax1.plot(x_values,y_values)
x_values2=unrate[12:24]["DATE"]
y_values2=unrate[12:24]["VALUE"]
ax2.plot(x_values2,y_values2)
fig.show()

## 6. Formatting And Spacing ##

import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("unrate.csv")
data["DATE"]=pd.to_datetime(data["DATE"])
x1_values=data["DATE"][0:12]
y1_values=data["VALUE"][0:12]
x2_values=data["DATE"][12:24]
y2_values=data["VALUE"][12:24]
fig=plt.figure(figsize=(12,5))
chrt1=fig.add_subplot(2,1,1)
chrt2=fig.add_subplot(2,1,2)
chrt1.plot(x1_values,y1_values)
chrt2.plot(x2_values,y2_values)
fig.show()

## 7. Comparing Across More Years ##

import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("unrate.csv")
data["DATE"]=pd.to_datetime(data["DATE"])
fig=plt.figure(figsize=(12,12))
chart1=fig.add_subplot(5,1,1)
chart2=fig.add_subplot(5,1,2)
chart3=fig.add_subplot(5,1,3)
chart4=fig.add_subplot(5,1,4)
chart5=fig.add_subplot(5,1,5)
x1_values=data["DATE"][0:12]
x2_values=data["DATE"][12:24]
x3_values=data["DATE"][24:36]
x4_values=data["DATE"][36:48]
x5_values=data["DATE"][48:60]
y1_values=data["VALUE"][0:12]
y2_values=data["VALUE"][12:24]
y3_values=data["VALUE"][24:36]
y4_values=data["VALUE"][36:48]
y5_values=data["VALUE"][48:60]
chart1.plot(x1_values,y1_values)
chart2.plot(x2_values,y2_values)
chart3.plot(x3_values,y3_values)
chart4.plot(x4_values,y4_values)
chart5.plot(x5_values,y5_values)
fig.show()

## 8. Overlaying Line Charts ##

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("unrate.csv")
data["DATE"]=pd.to_datetime(data["DATE"])
data["MONTH"]=data["DATE"].dt.month
fig=plt.figure(figsize=(6,3))
x1_values=data["MONTH"][0:12]
x2_values=data["MONTH"][12:24]
x3_values=data["MONTH"][24:36]
x4_values=data["MONTH"][36:48]
x5_values=data["MONTH"][48:60]
y1_values=data["VALUE"][0:12]
y2_values=data["VALUE"][12:24]
y3_values=data["VALUE"][24:36]
y4_values=data["VALUE"][36:48]
y5_values=data["VALUE"][48:60]
chart1=fig.add_subplot(1,1,1)
chart1.plot(x1_values,y1_values,color="red")
chart1.plot(x2_values,y2_values,color="blue")
fig.show()


## 9. Adding More Lines ##

import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("unrate.csv")
data["DATE"]=pd.to_datetime(data["DATE"])
data["MONTH"]=data["DATE"].dt.month
x1_values=data["MONTH"][0:12]
x2_values=data["MONTH"][12:24]
x3_values=data["MONTH"][24:36]
x4_values=data["MONTH"][36:48]
x5_values=data["MONTH"][48:60]
y1_values=data["VALUE"][0:12]
y2_values=data["VALUE"][12:24]
y3_values=data["VALUE"][24:36]
y4_values=data["VALUE"][36:48]
fig=plt.figure(figsize=(10,6))
chart=fig.add_subplot(1,1,1)
chart.plot(x1_values,y1_values,color="red")
chart.plot(x2_values,y2_values,color="blue")
chart.plot(x3_values,y3_values,color="green")
chart.plot(x4_values,y4_values,color="orange")
chart.plot(x5_values,y5_values,color="black")
fig.show()


## 10. Adding A Legend ##

import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("unrate.csv")
data["DATE"]=pd.to_datetime(data["DATE"])
data["MONTH"]=data["DATE"].dt.month
x1_values=data["MONTH"][0:12]
x2_values=data["MONTH"][12:24]
x3_values=data["MONTH"][24:36]
x4_values=data["MONTH"][36:48]
x5_values=data["MONTH"][48:60]
y1_values=data["VALUE"][0:12]
y2_values=data["VALUE"][12:24]
y3_values=data["VALUE"][24:36]
y4_values=data["VALUE"][36:48]
fig=plt.figure(figsize=(10,6))
chart=fig.add_subplot(1,1,1)
chart.plot(x1_values,y1_values,color="red",label="1948")
chart.plot(x2_values,y2_values,color="blue",label="1949")
chart.plot(x3_values,y3_values,color="green",label="1950")
chart.plot(x4_values,y4_values,color="orange",label="1951")
chart.plot(x5_values,y5_values,color="black",label="1952")
chart.legend(loc="lower right")
fig.show()


## 11. Final Tweaks ##

import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("unrate.csv")
data["DATE"]=pd.to_datetime(data["DATE"])
data["MONTH"]=data["DATE"].dt.month
x1_values=data["MONTH"][0:12]
x2_values=data["MONTH"][12:24]
x3_values=data["MONTH"][24:36]
x4_values=data["MONTH"][36:48]
x5_values=data["MONTH"][48:60]
y1_values=data["VALUE"][0:12]
y2_values=data["VALUE"][12:24]
y3_values=data["VALUE"][24:36]
y4_values=data["VALUE"][36:48]
fig=plt.figure(figsize=(10,6))
chart=fig.add_subplot(1,1,1)
chart.plot(x1_values,y1_values,color="red",label="1948")
chart.plot(x2_values,y2_values,color="blue",label="1949")
chart.plot(x3_values,y3_values,color="green",label="1950")
chart.plot(x4_values,y4_values,color="orange",label="1951")
#chart.plot(x5_values,y5_values,color="black",label="1952")
chart.legend(loc="lower right")
chart.set_title("Monthly Unemployment Trends, 1948-1952")
chart.set_xlabel("Month, Integer")
chart.set_ylabel("Unemployment Rate, Percent")
fig.show()
