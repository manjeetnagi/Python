## 3. Read the File Into a String ##

f=open("dq_unisex_names.csv","r")
names=f.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
first_five = names_list[0:5]

## 5. Convert the List of Strings to a List of Lists ##

f=open("dq_unisex_names.csv","r")
names=f.read()
name_list=names.split("\n")
nested_list=[]
for name in name_list:
    nested_list.append(name.split(","))
print(nested_list)

## 6. Convert Numerical Values ##

f=open("dq_unisex_names.csv","r")
names=f.read()
name_list=names.split("\n")
numerical_list=[]
for name in name_list:
    temp_name=name.split(",")[0]
    temp_number=float(name.split(",")[1])
    temp_list=[temp_name,temp_number]
    numerical_list.append(temp_list)
print(numerical_list[0:4])


## 7. Filter the List ##

f=open("dq_unisex_names.csv","r")
names=f.read()
name_list=names.split("\n")
numerical_list=[]
for name in name_list:
    temp_name=name.split(",")[0]
    temp_number=float(name.split(",")[1])
    temp_list=[temp_name,temp_number]
    numerical_list.append(temp_list)

thousand_or_greater=[]    
for item in numerical_list:
    if item[1]>=1000:
        thousand_or_greater.append(item[0])

       