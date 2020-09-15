import requests

from bs4 import BeautifulSoup

url = input()
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.find('h1').text)
