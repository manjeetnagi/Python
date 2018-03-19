## 1. Opening Files ##

f=open("crime_rates.csv","r")

## 2. Reading In Files ##

f=open("crime_rates.csv","r")
data=f.read()
#print(data)
data

## 3. Splitting ##

f=open("crime_rates.csv","r")
c=f.read()
rows=c.split("\n")
rows

## 5. Practice - Loops ##

ten_rows=rows[0:10]
for row in ten_rows:
    print(row)

## 6. List of Lists ##

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])

## 7. Practice - Splitting Elements in a List ##

f=open("crime_rates.csv","r")
c=f.read()
rows=c.split("\n")
final_data=[]
for item in rows:
    new_list=item.split(",")
    final_data.append(new_list)
print(final_data)

    

## 8. Accessing Elements in a List of Lists: The Manual Way ##

print(five_elements)
cities_list=[]
for item in five_elements:
    cities_list.append(item[0])
print(cities_list)


## 9. Looping Through a List of Lists ##

crime_rates = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
cities_list = []
for outer_list in final_data:
    city = outer_list[0]
    cities_list.append(city)

## 10. Challenge ##

int_crime_rates=[]
for item in rows:
    split_item=item.split(",")
    split_int=int(split_item[1])
    int_crime_rates.append(split_int)