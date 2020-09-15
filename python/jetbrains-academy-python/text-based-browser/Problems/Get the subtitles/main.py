import requests

from bs4 import BeautifulSoup

article_id = int(input())
url = input()

response = requests.get(url)
parsed_response = BeautifulSoup(response.content, 'html.parser')

print(parsed_response.find_all('h2')[article_id])


