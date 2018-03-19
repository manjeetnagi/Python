## 1. Introduction ##

SELECT * from recent_grads LIMIT 5

## 2. Calculating Group-Level Summary Statistics ##

SELECT Major_category, AVG(ShareWomen) from recent_grads GROUP BY Major_category

## 3. Practice: Using GROUP BY ##

SELECT Major_category, AVG(Employed)/AVG(Total) as share_employed from recent_grads GROUP BY Major_category

## 4. Querying Virtual Columns With the HAVING Statement ##

SELECT Major_category, AVG(Low_wage_jobs)/AVG(Total) as share_low_wage from recent_grads GROUP BY Major_category HAVING share_low_wage > 0.1

## 5. Rounding Results With the ROUND() Function ##

SELECT ROUND(ShareWomen, 4), Major_category from recent_grads LIMIT 10

## 6. Nesting functions ##

SELECT Major_category, ROUND(AVG(College_jobs)/AVG(Total) , 3) as share_degree_jobs from recent_grads  GROUP BY Major_category HAVING share_degree_jobs < 0.3

## 7. Casting ##

SELECT Major_category, (CAST(SUM(Women) as Float)/CAST(SUM(Total) as Float)) as SW from recent_grads GROUP BY Major_category ORDER BY SW