## 2. Adding columns ##

ALTER TABLE facts ADD leader text

## 6. Creating a table with relations ##

CREATE TABLE factbook.state(
id INTEGER PRIMARY KEY,
name TEXT,
area INTEGER,
country INTEGER,
FOREIGN KEY(country) REFERENCES facts(id)
)

## 7. Querying across foreign keys ##

SELECT * from landmarks INNER JOIN facts on landmarks.country=facts.id 

## 9. Types of joins ##

SELECT * FROM LANDMARKS LEFT OUTER JOIN facts on landmarks.country=facts.id