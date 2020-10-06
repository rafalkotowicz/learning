import re

import requests

from bs4 import BeautifulSoup

looking_for = input()
url = input()

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.find(string=re.compile(looking_for)).strip())
