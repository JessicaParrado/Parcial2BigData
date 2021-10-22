import requests

from bs4 import BeautifulSoup

r = requests.get('https://www.eltiempo.com')
soup = BeautifulSoup(r.text, 'lxml')
print(soup.prettify())