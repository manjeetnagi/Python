## 3. Psycopg2 ##

import psycopg2
conn=psycopg2.connect("dbname=dq user=dq")
cursor=conn.cursor()
print(cursor)
conn.close()

## 4. Creating a table ##

import psycopg2
conn=psycopg2.connect("dbname=dq user=dq")
q1="CREATE TABLE notes(id integer PRIMARY KEY, body text, title text)"
cursor=conn.cursor()
cursor.execute(q1)
cursor.close()

## 5. SQL Transactions ##

import psycopg2
conn=psycopg2.connect("dbname=dq user=dq")
cursor=conn.cursor()
q1="create table notes (id integer primary key, body text, title text)"
cursor.execute(q1)
conn.commit()

## 6. Autocommitting ##

import psycopg2
conn=psycopg2.connect("dbname=dq user=dq")
conn.autocommit=True
q1="CREATE TABLE facts(id integer PRIMARY KEY, country text, value integer)"
cursor=conn.cursor()
cursor.execute(q1)
conn.close()

## 7. Executing queries ##

import psycopg2
conn=psycopg2.connect("dbname=dq user=dq")
conn.autocommit=True
q1="INSERT INTO notes VALUES(5,'Do more missions on Dataquest.','Dataquest reminder')"
cursor=conn.cursor()
cursor.execute(q1)
q2="SELECT * FROM notes"
print("here")
cursor.execute(q2)
rows=cursor.fetchall()[0]
print(rows)
conn.close()

## 8. Creating a database ##

import psycopg2
conn=psycopg2.connect("dbname=dq user=dq")
conn.autocommit=True
q1="CREATE DATABASE income OWNER dq"
cursor=conn.cursor()
cursor.execute(q1)
conn.close()


## 9. Deleting a database ##

import psycopg2
conn=psycopg2.connect("dbname=dq user=dq")
conn.autocommit=True
cursor=conn.cursor()
q1="DROP DATABASE income"
cursor.execute(q1)
cursor.close()