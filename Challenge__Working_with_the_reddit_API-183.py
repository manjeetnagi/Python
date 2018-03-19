## 2. Authenticating with the API ##

auth_header={"Authorization" : "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent" : "Dataquest/1.0" }
params={"t" : "day"}
response=requests.get("https://oauth.reddit.com/r/python/top", headers=auth_header, params=params )
python_top=response.json()

## 3. Getting the Most Upvoted Post ##

python_top_articles=python_top["data"]["children"]
print(type(python_top_articles))
most_votes=0
most_voted={}
subreddit_id=""

for post in python_top_articles:
    if post["data"]["ups"]> most_votes:
        most_votes=post["data"]["ups"]
        most_upvoted=post["data"]["id"]
        subreddit_id=post["data"]["subreddit"]
print(most_votes)
print(most_upvoted)
print(subreddit_id)

## 4. Getting Post Comments ##

python_top_articles=python_top["data"]["children"]
print(type(python_top_articles))
most_votes=0
most_voted={}
subreddit_id=""

for post in python_top_articles:
    if post["data"]["ups"]> most_votes:
        most_votes=post["data"]["ups"]
        most_upvoted=post["data"]["id"]
        subreddit_id=post["data"]["subreddit"]
auth_header={"Authorization" : "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent":"Dataquest/1.0"}
response=requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=auth_header)
comments=response.json()
print(comments)

## 5. Getting the Most Upvoted Comment ##

import json
auth_head={"Authorization" : "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk" , "User-Agent" : "Dataquest/1.0"}
params={"t" : "day"}
response=requests.get("https://oauth.reddit.com/r/python/top", headers=auth_head, params=params)
top_topics=response.json()["data"]["children"]

most_votes=0
most_voted=""
reddit_id=""

for each in top_topics:
    if each["data"]["ups"]>most_votes:
        most_votes=each["data"]["ups"]
        most_voted=each["data"]["id"]
        reddit_id=each["data"]["subreddit"]

response=requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=auth_head)
comments=response.json()

most_votes=0
most_upvoted_comment=""
comments_list=comments[1]["data"]["children"]
for comment in comments_list:
    if comment["data"]["ups"]>most_votes:
        most_upvoted_comment=comment["data"]["id"]
        most_votes=comment["data"]["ups"]
print(most_upvoted_comment)
        

## 6. Upvoting a Comment ##

auth_head={"Authorization" : "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk" , "User-Agent" : "Dataquest/1.0"}
payload={"dir": 1 ,"id": "d16y4ry"}
response=requests.post("https://oauth.reddit.com/api/vote", json=payload, headers=auth_head)
status=response.status_code