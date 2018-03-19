## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i,ship in enumerate(ships):
    print(ship)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
print(enumerate(things))
for i,thing in enumerate(things):
    thing.append(trees[i])
print(things)

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled=[2*apple for apple in apple_prices]
print(apple_prices_doubled)
apple_prices_lowered=[(apple-100) for apple in apple_prices ]

## 5. Counting Female Names ##

name_counts={}
for each in legislators:
    if each[3]=="F":
        if int(each[2].split("-")[0])>1940:
            if each[1] in name_counts:
                name_counts[each[1]]=name_counts[each[1]]+1
            else:
                name_counts[each[1]]=1
print(name_counts)

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []
for value in values:
    checks.append(value is not None and value > 30 )
print(checks)

## 8. Highest Female Name Count ##

max_value=None
for each in name_counts:
    if max_value is None or name_counts[each]>max_value :
        max_value=name_counts[each]
print(max_value)

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for i,plant in plant_types.items():
    print(i)
    print(plant)

## 10. Finding the Most Common Female Names ##

top_female_names = []
print(name_counts)
for name,count in name_counts.items():
    if count==2:
        top_female_names.append(name)
print(top_female_names)

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts={}
for each in legislators:
    if each[3]=="M" and each[7]>1940:
        if each[1] in male_name_counts:
            male_name_counts[each[1]]=male_name_counts[each[1]]+1
        else:
            male_name_counts[each[1]]=1
highest_male_count=None
for each in male_name_counts:
    if highest_male_count is None or male_name_counts[each]>highest_male_count:
        highest_male_count=male_name_counts[each]
for each in male_name_counts:
    if male_name_counts[each]==highest_male_count:
        top_male_names.append(each)
        