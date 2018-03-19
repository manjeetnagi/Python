## 4. Querying a normalized database ##

q="select ceremonies.year, nominations.movie from nominations INNER JOIN ceremonies ON nominations.ceremony_id=ceremonies.id  WHERE nominations.nominee='Natalie Portman';"
conn=sqlite3.connect("academy_awards.db")
cursor=conn.cursor()
cursor.execute(q)
portman_movies=cursor.fetchall()

## 7. Join table ##

import sqlite3
conn=sqlite3.connect("academy_awards.db")
q1="select * from movies_actors LIMIT 5;"
cursor=conn.cursor()
cursor.execute(q1)
five_join_table=cursor.fetchall()
q2="select * from actors limit 5"
five_actors=cursor.execute(q2).fetchall()
five_movies=cursor.execute("select * from movies limit 5").fetchall()
print(five_movies)

## 9. Querying a many-to-many relation ##

import sqlite3
q='''Select actors.actor,movies.movie from  actors INNER join movies_actors on actors.id=movies_actors.actor_id INNER join movies on movies.id=movies_actors.movie_id where movies.movie="The King's Speech";'''
conn=sqlite3.connect("academy_awards.db")
cursor=conn.cursor()
kings_actors=cursor.execute(q).fetchall()

## 10. Practice: querying a many-to-many relation ##

import sqlite3
q='select movie,actor from movies INNER join movies_actors on movies.id=movies_actors.movie_id INNER join actors on actors.id=movies_actors.actor_id where actors.actor="Natalie Portman";'
conn=sqlite3.connect("academy_awards.db")
cursor=conn.cursor()
portman_joins=cursor.execute(q).fetchall()