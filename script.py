import requests
from bs4 import BeautifulSoup

username = input(">")

URL = "https://codeforces.com/contests/with/" + username
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('div', class_='datatable')

for k in results.findAll():
    print(k)