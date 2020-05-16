import requests, json
from bs4 import BeautifulSoup

blog_soup = ""
blog_data = ""

def extract_data(username):
	blog_URL = "https://codeforces.com/blog/" + username
	blog_page = requests.get(blog_URL)

	global blog_soup, blog_data
	blog_soup = BeautifulSoup(blog_page.content, 'html.parser')
	blog_data = {}

	for a in blog_soup.find_all('a', href=True): 
	    if a.text and (a['href'])[:12] == "/blog/entry/" and (a['href'])[::-1][:9] != 'stnemmoc#':
	    	blog_data[a.text] = a['href']
	return save_data(blog_data)

def save_data(blog_data):
	with open('blog_data.txt', 'w') as outfile:
		json.dump(blog_data, outfile)

def output_HTML():
	global blog_soup
	print(blog_soup.prettify)

def output_data():
	global blog_data
	print(blog_data)