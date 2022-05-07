from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.youtube.com').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_="course-unit-container-BecauseyouviewedWebScrapingwithPythonBeautifulSoupRequestsSelenium")

print(jobs)
