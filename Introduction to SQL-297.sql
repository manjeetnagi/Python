## 2. Previewing A Table Using SELECT ##

Select * from recent_grads Limit 10


## 3. Filtering Rows Using WHERE ##

Select Major, ShareWomen from recent_grads where ShareWomen < 0.5

## 4. Expressing Multiple Filter Criteria Using AND ##

select Major, Major_category, Median, ShareWomen from recent_grads where ShareWomen > 0.5 and Median > 50000

## 5. Returning One of Several Conditions With OR ##

select Major, Median, Unemployed from recent_grads where Median >= 10000 OR Unemployed <= 1000 limit 20

## 6. Grouping Operators With Parentheses ##

select Major, Major_category, ShareWomen, Unemployment_rate from recent_grads where ((ShareWomen > 0.5) OR (Unemployment_rate < 0.051)) and Major_category="Engineering"
                                                                                     
                                                                                     

## 7. Ordering Results Using ORDER BY ##

select Major, ShareWomen, Unemployment_rate from recent_grads where ShareWomen > 0.3 and Unemployment_rate < 0.1 Order By ShareWomen DESC

## 8. Practice Writing A Query ##

Select Major_category, Major, Unemployment_rate from recent_grads where Major_category in ("Engineering", "Physical Sciences") Order by Unemployment_rate Asc