import requests, json
from bs4 import BeautifulSoup

def extract_data(username):
	main_URL = "https://codeforces.com/profile/" + username
	main_page = requests.get(main_URL)

	main_soup = BeautifulSoup(main_page.content, 'html.parser')
	main_data = {}

	main_data["rating"] = main_soup.find_all('span',class_ = "user-red")[1].text
	main_data["experience"] = main_soup.find_all('span', class_ = "format-humantime")[1].text

	main_location = []
	for a in main_soup.find_all('a', href=True): 
	    if a.text and (a['href'])[:17] == "/ratings/country/":
	    	main_location.append(a.text)

	for i in main_location:
		main_data["location"] = i
	return save_data(main_data)

def save_data(main_data):
	with open('main_data.txt', 'w') as outfile:
		json.dump(main_data, outfile)
