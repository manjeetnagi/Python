## 2. Array Comparisons ##

countries_canada=(world_alcohol[:,2]=="Canada")
years_1984=(world_alcohol[:,0]=="1984")
print(years_1984)

## 3. Selecting Elements ##

country_is_algeria=(world_alcohol[:,2]=="Algeria")
print(world_alcohol.shape)
print(country_is_algeria.shape)
country_algeria=world_alcohol[country_is_algeria]
print(country_algeria.shape)

## 4. Comparisons with Multiple Conditions ##


is_algeria_and_1986=(world_alcohol[:,0]=="1986") & (world_alcohol[:,2]=="Algeria")
print(world_alcohol.shape)
print(is_algeria_and_1986.shape)
rows_with_algeria_and_1986=world_alcohol[is_algeria_and_1986]
print(rows_with_algeria_and_1986.shape)

## 5. Replacing Values ##

check_1986=(world_alcohol[:,0]=="1986")
check_wine=(world_alcohol[:,3]=="Wine")
world_alcohol[check_1986,0]="2014"
world_alcohol[check_wine,3]="Grog"
print(world_alcohol.shape)
print(check_1986.shape)
print(check_wine.shape)

## 6. Replacing Empty Strings ##

is_value_empty=(world_alcohol[:,4]=="")
world_alcohol[is_value_empty,4]="0"

## 7. Converting Data Types ##

alcohol_consumption=world_alcohol[:,4]
alcohol_consumption=alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol=alcohol_consumption.sum()
average_alcohol=alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

canada_1986=world_alcohol[(world_alcohol[:,0]=="1986") & (world_alcohol[:,2]=="Canada")]
canada_alcohol=canada_1986[:,4]
canada_alcohol[canada_alcohol==""]="0"
canada_alcohol=canada_alcohol.astype(float)
print(canada_alcohol)
total_canadian_drinking=canada_alcohol.sum()


## 10. Calculating Consumption for Each Country ##

totals={}
year=world_alcohol[world_alcohol[:,0]=="1989"]
for each in year:
    if each[4]=="":
            each[4]="0"
    if each[2] in totals:
                totals[each[2]]=totals[each[2]]+float(each[4])
    else:
        totals[each[2]]=float(each[4])
#print(totals)

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
for country in totals:
    consumption = totals[country]
    if highest_value < consumption:
        highest_value = consumption
        highest_key = country