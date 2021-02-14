import requests
from config import api_key
from pprint import pprint


# url = "https://jsonplaceholder.typicode.com/posts/"

# data = requests.get(url).json()

# posts = len(data)

# t = type(posts)

# print(data)

# print(posts)

# print(t)

# url = "https://www.omdbapi.com/"
# api_key = "trilogy"
# title = ["Aliens", "Sing", "Moana"]
# title_director = []
# for movie_title in title:
#     data = requests.get(url, params={
#     "apikey": api_key,
#     "t": movie_title}).json()

#     title_director.append(data)
#     print(data["Director"])
# print(title_director)


url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

payload = {
    "api-key": api_key,
    "q": "entry-level-job-opportunities-2020"
}
data = requests.get(url, params=payload).json()
# print(data)
data_articles = data["response"]["docs"]
pprint(data_articles)
for data in data_articles:
    pprint(data["web_url"]) 
