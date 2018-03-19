## 3. Connecting to the Database ##

import sqlite3
conn=sqlite3.connect("jobs.db")

## 6. Creating a Cursor and Running a Query ##

import sqlite3

conn=sqlite3.connect("jobs.db")
query="select Major from recent_grads"
cursor=conn.cursor()
cursor.execute(query)
majors=cursor.fetchall()
print(majors[0:2])

## 8. Fetching a Specific Number of Results ##

import sqlite3

conn=sqlite3.connect("jobs.db")
query="select major, Major_category from recent_grads"
cursor=conn.cursor()
cursor.execute(query)
five_results=cursor.fetchmany(5)

## 9. Closing the Database Connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

import sqlite3

conn=sqlite3.connect("jobs2.db")
query="Select Major from recent_grads Order by Major Desc;"
cursor=conn.cursor()
cursor.execute(query)
reverse_alphabetical=cursor.fetchall()
conn.close()