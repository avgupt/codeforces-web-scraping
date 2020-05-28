import requests, json
from bs4 import BeautifulSoup
import urllib.request

user_soup = ""
user_data = ""


def extract_data_usingAPI(username):
	user_URL = "https://codeforces.com/api/user.info?handles=" + username
	with urllib.request.urlopen(user_URL) as url:
		user_data = json.loads(url.read().decode())
	#print(user_data)
	return save_data(user_data)

def extract_data(username):
	user_URL = "https://codeforces.com/profile/" + username
	user_page = requests.get(user_URL)

	global user_soup, user_data
	user_soup = BeautifulSoup(user_page.content, 'html.parser')
	user_data = {}

	user_data["rating"] = user_soup.find_all('span',class_ = "user-red")[1].text
	user_data["experience"] = user_soup.find_all('span', class_ = "format-humantime")[1].text

	user_location = []
	for a in user_soup.find_all('a', href=True): 
	    if a.text and (a['href'])[:17] == "/ratings/country/":
	    	user_location.append(a.text)

	for i in user_location:
		user_data["location"] = i
	return save_data(user_data)

def save_data(user_data):
	with open('user_data.txt', 'w') as outfile:
		json.dump(user_data, outfile)

def output_HTML():
	global user_soup
	print(user_soup.prettify)

def output_data():
	global user_data
	print(user_data)
