## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")
cursor=conn.cursor()
schema=cursor.execute("PRAGMA table_info(facts)").fetchall()
for each in schema:
    print(each)


## 3. Explain query plan ##

import sqlite3
conn=sqlite3.connect("factbook.db")
cursor=conn.cursor()
query_plan_one=cursor.execute("EXPLAIN QUERY PLAN SELECT * from facts where area>40000").fetchall()
query_plan_two=cursor.execute("EXPLAIN QUERY PLAN SELECT area from facts where area>40000").fetchall()
query_plan_three=cursor.execute("EXPLAIN QUERY PLAN SELECT * from facts where name='Czech Republic'").fetchall()
print(query_plan_one)
print(query_plan_two)
print(query_plan_three)


## 5. Time complexity ##

import sqlite3
conn=sqlite3.connect("factbook.db")
cursor=conn.cursor()
q1="EXPLAIN QUERY PLAN Select * from facts where id=20"
query_plan_four=cursor.execute(q1).fetchall()
print(query_plan_four)

## 9. All together now ##

query_plan_six = conn.execute("explain query plan select * from facts where population > 10000 ;").fetchall()
print(query_plan_six)
conn.execute("create index if not exists pop_idx on facts(population)")
query_plan_seven = conn.execute("explain query plan select * from facts where population > 10000 ;").fetchall()
print(query_plan_seven)