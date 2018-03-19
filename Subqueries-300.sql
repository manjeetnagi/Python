## 2. Subqueries ##

SELECT Major, Unemployment_rate from recent_grads where Unemployment_rate < (SELECT AVG(Unemployment_rate) from recent_grads) ORDER BY Unemployment_rate ASC

## 3. Subquery In SELECT ##

SELECT CAST(COUNT(*) as float)/CAST ((SELECT COUNT(*) from recent_grads) as float) proportion_abv_avg from recent_grads WHERE ShareWomen > (SELECT AVG(ShareWomen) from recent_grads)


## 4. Returning Multiple Results In Subqueries ##

Select Major, Major_category from recent_grads WHERE Major_category IN (Select Major_category from recent_grads GROUP BY Major_category ORDER BY SUM(Total) DESC LIMIT 5)

## 5. Building Complex Subqueries ##

Select AVG(CAST(Sample_size as float)/CAST(Total as float) ) as avg_ratio from recent_grads

## 6. Practice Integrating A Subquery With The Outer Query ##

select Major, Major_category, cast(Sample_size as float)/cast(Total as float) ratio from recent_grads
where ratio > (select AVG(cast(Sample_size as float)/cast(Total as float)) avgratio from recent_grads)