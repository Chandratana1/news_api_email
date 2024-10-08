import requests

api_key = "a5d6283b412b4f86b010490b59434918"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-09-08"
       "&sortBy=publishedAt&"
       "apiKey=a5d6283b412b4f86b010490b59434918")


# Make request
request = requests.get(url)

#Make a dict using json
content = request.json()

#  Access the article titles and description
for article in content["articles"]:
       print(article["title"])
# print(content["articles"])

print(type(content))
