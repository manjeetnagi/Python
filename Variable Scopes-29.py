## 1. The Data Set ##

print(city)


## 2. Built-In Functions ##

total=sum([6,11])

## 4. Scopes ##

def find_average(column):
    length = len(column)
    print(length)
    total = sum(column)
    print(total)
    return total / length

average = find_average(principal_outstanding_240)
total=sum(borrower_default_count_240)
print(average)

## 5. Scope Isolation ##

def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

def find_length(column):
    length = len(column)
    return length

principal_length = find_length(principal_outstanding_240)
average=find_average(principal_outstanding_240)
length=len(borrower_default_count_240)

## 6. Scope Inheritance ##

def find_average(column):
    total = sum(column)
    # In this function, we are going to pretend that we forgot to calculate the length
    return total / length

length = 10
average=find_average(principal_outstanding_240)

## 9. Global Variables ##

def test_func():
    global b
    b=20
a=test_func()
print(b)