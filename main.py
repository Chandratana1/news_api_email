import requests

ap_key = "a5d6283b412b4f86b010490b59434918"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-09-08&" \
       "sortBy=publishedAt& " \
       "apiKey=a5d6283b412b4f86b010490b59434918 "

request = requests.get(url)
content = request.text
print(content)