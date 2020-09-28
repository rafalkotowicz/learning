import requests

from bs4 import BeautifulSoup

wanted_word = input()
url = input()

response = requests.get(url)

response_parser = BeautifulSoup(response.content, 'html.parser')
print(response_parser.find_all('p')[0].get_text())

# def first_paragraph_containing_wanted_word():
#     pass
