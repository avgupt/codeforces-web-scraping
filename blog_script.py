import requests, json
from bs4 import BeautifulSoup

username = input(">")

#starts here
blog_URL = "https://codeforces.com/blog/" + username
blog_page = requests.get(blog_URL)

blog_soup = BeautifulSoup(blog_page.content, 'html.parser')

blog_data = {}
for a in blog_soup.find_all('a', href=True): 
    if a.text and (a['href'])[:12] == "/blog/entry/" and (a['href'])[::-1][:9] != 'stnemmoc#':
    	blog_data[a.text] = a['href']


with open('blog_data.txt', 'w') as outfile:
	json.dump(blog_data, outfile)

