## 1. Introduction ##

strings = ["data science", "big data", "metadata"]
regex = "data"

## 2. Wildcards in Regular Expressions ##

strings = ["bat", "robotics", "megabyte"]
regex = "..t"

## 3. Searching the Beginnings And Endings Of Strings ##

strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b.tter"

## 5. Reading and Printing the Data Set ##

import csv
f=open("askreddit_2015.csv","r")
c=csv.reader(f)
posts_with_header=list(c)
posts=posts_with_header[1:len(posts_with_header)]
print(posts[0:10])

## 6. Counting Simple Matches in the Data Set with re() ##

import re
import csv
f=open("askreddit_2015.csv","r")
c=csv.reader(f)
posts_with_header=list(c)
posts=posts_with_header[1:len(posts_with_header)]
of_reddit_count=0
for post in posts:
    if re.search("of Reddit",post[0]) is not None:
        of_reddit_count=of_reddit_count+1
print(of_reddit_count)
    
    

## 7. Using Square Brackets to Match Multiple Characters ##

import re
import csv
f=open("askreddit_2015.csv","r")
c=csv.reader(f)
posts_with_header=list(c)
posts=posts_with_header[1:len(posts_with_header)]
of_reddit_count=0
for post in posts:
    if re.search("of [rR]eddit",post[0]):
        of_reddit_count=of_reddit_count+1
print(of_reddit_count)

## 8. Escaping Special Characters ##

import re
import csv
f=open("askreddit_2015.csv","r")
c=csv.reader(f)
posts_with_header=list(c)
posts=posts_with_header[1:len(posts_with_header)]
serious_count=0
for post in posts:
    if re.search("\[Serious\]",post[0]):
        serious_count=serious_count+1
print(serious_count)

## 9. Combining Escaped Characters and Multiple Matches ##

import re
import csv
f=open("askreddit_2015.csv","r")
c=csv.reader(f)
posts_with_header=list(c)
posts=posts_with_header[1:len(posts_with_header)]
serious_count=0
for post in posts:
    if re.search("\[[Ss]erious\]",post[0]):
        serious_count=serious_count+1
print(serious_count)

## 10. Adding More Complexity to Your Regular Expression ##

import re

serious_count = 0
for row in posts:
    if re.search("[\[\(][Ss]erious[\)\]]", row[0]):
        serious_count += 1

## 11. Combining Multiple Regular Expressions ##

import re
import csv
f=open("askreddit_2015.csv","r")
c=csv.reader(f)
posts=list(c)
serious_start_count=0
serious_end_count=0
serious_count_final=0
for post in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]",post[0]):
        serious_start_count+=1
    if re.search("[\[\(][Ss]erious[\]\)]$",post[0]):
        serious_end_count+=1
    if re.search("^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$",post[0]) is not None:
        serious_count_final+=1
print(serious_start_count)
print(serious_end_count)
print(serious_count_final)

## 12. Using Regular Expressions to Substitute Strings ##

import csv
import re
f=open("askreddit_2015.csv","r")
c=csv.reader(f)
posts=list(c)
posts=posts[1:len(posts)]
for each in posts:
    each[0]=re.sub("[\[\(][Ss]erious[\]\)]","[Serious]",each[0])
    

## 13. Matching Years with Regular Expressions ##

import re
year_strings = []
for string in strings:
    if re.search("[1-2][0-9][0-9][0-9]",string) is not None:
        year_strings.append(string)



## 14. Repeating Characters in Regular Expressions ##

import re
year_strings = []
for string in strings:
    if re.search("[1-2][0-9]{3}",string) is not None:
        year_strings.append(string)

## 15. Challenge: Extracting all Years ##

import re
years=re.findall("[1-2][0-9]{3}",years_string)