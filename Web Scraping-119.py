## 2. Web Page Structure ##

# Write your code here.
response=requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
content=response.content

## 3. Retrieving Elements from a Page ##

from bs4 import BeautifulSoup

response=requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

content=response.content

parser=BeautifulSoup(content, "html.parser")
title_text=parser.title.text
print(title_text)

## 4. Using Find All ##

from bs4 import BeautifulSoup
response=requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
parser=BeautifulSoup(response.content, "html.parser")
head=parser.find_all("head")
print(head[0])
title=head[0].find_all("title")
print(title[0].text)



## 5. Element IDs ##

from bs4 import BeautifulSoup

response=requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
parser=BeautifulSoup(response.content, "html.parser")
body=parser.find_all("body")
#print(body[0])
para_2=body[0].find_all("p", id="second")[0].text
second_paragraph_text=para_2
#second_paragraph_text



## 6. Element Classes ##

import json
from bs4 import BeautifulSoup

response=requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
parser=BeautifulSoup(response.content,"html.parser")
second_inner_paragraph_text=parser.find_all("p", class_="inner-text")[1].text
first_outer_paragraph_text=parser.find_all("p", class_="outer-text")[0].text


## 8. Using CSS Selectors ##

import json
from bs4 import BeautifulSoup
response=requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
parser=BeautifulSoup(response.content, "html.parser")
first_outer_text=parser.select(".outer-text")[0].text
second_text=parser.select("#second")[0].text

## 10. Using Nested CSS Selectors ##

# Get the Superbowl box score data.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/2014_super_bowl.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Find the number of turnovers the Seahawks committed.
turnovers = parser.select("#turnovers")[0]
seahawks_turnovers = turnovers.select("td")[1]
seahawks_turnovers_count = seahawks_turnovers.text
print(seahawks_turnovers_count)
patriots_total_plays_count = parser.select("#total-plays")[0].select("td")[2].text

seahawks_total_yards_count = parser.select("#total-yards")[0].select("td")[1].text