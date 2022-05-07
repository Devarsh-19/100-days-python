from os import link
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.geeksforgeeks.org/data-science-tutorial/?ref=ghm').text
soup = BeautifulSoup(html_text, 'lxml')

tags = soup.find_all('li')

for x in tags:
    print(x.text)

# for job in jobs:
#     links = soup.find('li').text
#     print(links)
