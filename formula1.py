import requests
from bs4 import BeautifulSoup
import random

print("Hello world")

response = requests.get(url="https://en.wikipedia.org/wiki/2020_Formula_One_World_Championship")

#https://medium.com/analytics-vidhya/web-scraping-wiki-tables-using-beautifulsoup-and-python-6b9ea26d8722

print(response.status_code)

htmlParser = BeautifulSoup(response.content, 'html.parser')

title = htmlParser.find(id="firstHeading")
print(title.string)