## 3. Finding Correlations With the r Value ##

import pandas as pd

correlations=combined.corr()
#correlations=correlations["sat_score"]
#correlations=correlations.loc["sat_score"]
print(correlations.loc["sat_score"])


## 5. Plotting Enrollment With the Plot() Accessor ##

import matplotlib.pyplot as plt

fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.scatter(combined["total_enrollment"],combined["sat_score"])
chart.set_xlabel("total_enrollment")
chart.set_ylabel("sat_score")
fig.show()


## 6. Exploring Schools With Low SAT Scores and Enrollment ##

low_enrollment=combined[(combined["total_enrollment"]<1000) & (combined["sat_score"]<1000)]
print(low_enrollment["School Name"])

## 7. Plotting Language Learning Percentage ##

import matplotlib.pyplot as plt
fig=plt.figure()
chart=fig.add_subplot(1,1,1)
chart.scatter(combined["ell_percent"], combined["sat_score"])
chart.set_xlabel("ell_percent")
chart.set_ylabel("sat_score")
fig.show()

## 9. Mapping the Schools With Basemap ##

import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.basemap import Basemap
fig=plt.figure()
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)
m.drawmapboundary(fill_color='#85A6D9')
m.drawrivers(color='#6D5F47', linewidth=0.4)
m.drawcoastlines(color='#6D5F47', linewidth=0.4)
longitudes=combined.lon.tolist()
latitudes=combined.lat.tolist()
#print(longitudes, latitudes)
#chart=fig.add_subplot(1,1,1)
m.scatter(longitudes,latitudes, s=20, zorder=2, latlon=True)
fig.show()

## 10. Plotting Out Statistics ##

import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.basemap import Basemap
fig=plt.figure()
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)
m.drawmapboundary(fill_color='#85A6D9')
m.drawrivers(color='#6D5F47', linewidth=0.4)
m.drawcoastlines(color='#6D5F47', linewidth=0.4)
longitudes=combined.lon.tolist()
latitudes=combined.lat.tolist()
#print(longitudes, latitudes)
#chart=fig.add_subplot(1,1,1)
m.scatter(longitudes,latitudes, s=20, zorder=2, latlon=True, c=combined["ell_percent"],cmap="summer")
fig.show()

## 11. Calculating District-Level Statistics ##

import numpy
import pandas as pd

districts=combined.groupby(["school_dist"]).agg(numpy.mean)
districts.reset_index(inplace=True)

## 12. Plotting Percent Of English Learners by District ##

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m=Basemap(projection="merc",llcrnrlat=40.496044,llcrnrlon=-74.255735,urcrnrlat=40.915256,urcrnrlon=-73.700272,resolution="i")
m.drawcoastlines(color='#6D5F47',linewidth=0.4)
m.drawrivers(color='#6D5F47',linewidth=0.4)
m.drawmapboundary(fill_color='#85A6D9')
longitudes=districts["lon"].tolist()
latitudes=districts["lat"].tolist()
m.scatter(longitudes,latitudes, s=50, zorder=2, latlon=True,c=districts["ell_percent"], cmap="summer")
plt.show()
