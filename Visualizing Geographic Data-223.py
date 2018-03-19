## 1. Geographic Data ##

import pandas as pd
airlines=pd.read_csv("airlines.csv")
airports=pd.read_csv("airports.csv")
routes=pd.read_csv("routes.csv")
print(airlines.iloc[0])
print(airports.iloc[0])
print(routes.iloc[0])
                 

## 4. Workflow With Basemap ##

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
m = Basemap(projection="merc",llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180  )


## 5. Converting From Spherical to Cartesian Coordinates ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
latti=airports["latitude"].tolist()
longi=airports["longitude"].tolist()
x,y=m(longi,latti)
print(x)
print(y)


## 6. Generating A Scatter Plot ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
x, y = m(longitudes, latitudes)
m.scatter(x,y, s=1)
plt.show()

## 7. Customizing The Plot Using Basemap ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()

## 8. Customizing The Plot Using Matplotlib ##

# Add code here, before creating the Basemap instance.

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
fig=plt.figure(figsize=(15,20))
chart=fig.add_subplot(1,1,1)
m.scatter(x, y, s=1)
m.drawcoastlines()
chart.set_title("Scaled Up Earth With Coastlines")
plt.show()

## 9. Introduction to Great Circles ##

import pandas as pd
geo_routes=pd.read_csv("geo_routes.csv")
geo_routes[0:5]

## 10. Displaying Great Circles ##



def create_great_circles(df):
    for indes,row_list in df.iterrows():
        if abs(row_list["end_lon"]-row_list["start_lon"])<180:
            if abs(row_list["start_lat"]-row_list["end_lat"])<180:
                
#                return(None)
                m.drawgreatcircle(row_list["start_lon"],row_list["start_lat"], row_list["end_lon"],row_list["end_lat"])
                
df=geo_routes[(geo_routes["source"]=="DFW")][["start_lon","start_lat","end_lon","end_lat"]]
#print(df)
fig, ax = plt.subplots(figsize=(15,20))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180)
m.drawcoastlines()
create_great_circles(df)


