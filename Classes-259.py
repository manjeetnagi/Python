## 2. Defining the Dataset Class ##

class Dataset:
    def __init__(self):
        self.type="csv"

dataset = Dataset()
print(dataset.type)

## 3. Passing Additional Arguments to the Initializer ##

class Dataset:
    def __init__(self,data):
        self.type="csv"
        self.data=data
import csv

f=open("nfl.csv","r")
c=csv.reader(f)
nfl_data=list(c)
nfl_dataset = Dataset(nfl_data)
dataset_data=nfl_dataset.data


## 4. Adding Additional Behavior ##

class Dataset():
    def __init__(self,data):
        self.type="csv"
        self.data=data
    def print_data(self,num_rows):
        print(self.data[0:num_rows])

import csv

f=open("nfl.csv","r")
c=csv.reader(f)
nfl_data=list(c)
nfl_dataset= Dataset(nfl_data)
nfl_dataset.print_data(5)

## 5. Enhancing the Initializer ##

class Dataset():
    def __init__(self,data):
        self.type="csv"
        self.data=data[1:len(data)]
        self.header=data[0]
      

import csv
f=open("nfl.csv","r")
c=csv.reader(f)
nfl_data=list(c)
nfl_dataset= Dataset(nfl_data)
nfl_header=nfl_dataset.header
print(nfl_header)

## 6. Grabbing Column Data ##

class Dataset():
    def __init__(self,data):
        self.data=data
    def column(self, input_label):
        for idx,value in enumerate(self.data[0]):
            Found=False
            if input_label==value:
                Found=True
                temp_list=[]
                for each in self.data[1:len(self.data)]:
                    temp_list.append(each[idx])
                return(temp_list)
            if Found==False:
                return(None)

import csv
f=open("nfl.csv","r")
c=csv.reader(f)
nfl_data=list(c)
nfl_dataset=Dataset(nfl_data)
#year_column=nfl_dataset.column("year")
year_column=nfl_dataset.column("year")
player_column=nfl_dataset.column("player")

## 7. Count Unique Method ##

class Dataset():
    def __init__(self,data):
        self.data=data
        
    def column(self,input_label):
        temp_list=[]
        for idx,value in enumerate(self.data[0]):
            Found=False
            if value==input_label:
                Found=True
                for each in self.data[1:len(self.data)]:
                    temp_list.append(each[idx])
        return(temp_list)
            
    def count_unique(self,input_label):
        column_list=self.column(input_label)
        return(len(set(column_list)))

import csv
f=open("nfl.csv","r")
c=csv.reader(f)
nfl_data=list(c)
nfl_dataset=Dataset(nfl_data)
total_years=nfl_dataset.count_unique("year")
print(total_years)

## 8. Make Objects Human Readable ##

class Dataset():
    def __init__(self,data):
        self.data=data
    def __str__(self):
        out_str=""
        for each in self.data[1:10]:
            out_str=out_str+str(each)+", "
        out_str="["+out_str+str(self.data[10])+"]"
        return(out_str)

import csv
f=open("nfl.csv","r")
c=csv.reader(f)
nfl_data=list(c)
nfl_dataset= Dataset(nfl_data)
print(nfl_dataset.__str__())