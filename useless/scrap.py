
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.geeksforgeeks.org/data-science-tutorial/?ref=ghm').text
soup = BeautifulSoup(html_text, 'lxml')

tags = soup.find_all('ul')

for x in tags:
    anc = x.find('a')
    print(anc.text)

# for job in jobs:
#     links = soup.find('li').text
#     print(links)
