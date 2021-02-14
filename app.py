import requests

# url = "https://jsonplaceholder.typicode.com/posts/"

# data = requests.get(url).json()

# posts = len(data)

# t = type(posts)

# print(data)

# print(posts)

# print(t)

url = "https://www.omdbapi.com/"
api_key = "trilogy"
title = ["Aliens", "Sing", "Moana"]
title_director = []
for movie_title in title:
    data = requests.get(url, params={
    "apikey": api_key,
    "t": movie_title}).json()

    title_director.append(data)
    print(data["Director"])
print(title_director)


