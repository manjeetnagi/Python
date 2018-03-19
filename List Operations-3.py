## 2. Parsing the File ##

f=open("la_weather.csv","r")
c=f.read()
weather_data=[]
list=c.split("\n")
for each in list:
    weather_data.append(each.split(","))

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.

weather=[]
for each in weather_data:
    weather.append(each[1])
weather

## 4. Counting the Items in a List ##

count=0
for each in weather:
    count=count+1
count

## 5. Removing the Header ##

print(len(weather))
new_weather=weather[1:len(weather)]
print(len(new_weather))

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found="cat" in animals
space_monster_found="space_monster" in animals
print(cat_found)
print(space_monster_found)

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "X"]
weather_type_found=[]
for each in weather_types:
    weather_type_found.append(each in new_weather)
print(weather_type_found)