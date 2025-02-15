import requests, json
from bs4 import BeautifulSoup

contests_soup = ""
contests_data = ""

def extract_data(username):
    contests_URL = "https://codeforces.com/contests/with/" + username
    contests_page = requests.get(contests_URL)

    global contests_soup, contests_data
    contests_soup = BeautifulSoup(contests_page.content, 'html.parser')
    contests_data = {}

    contests_table = contests_soup.find('div', 'datatable')
    contests_table_body = contests_table.find('tbody')

    contests_rows = contests_table_body.find_all('tr')
    for row in contests_rows:
        contests_cols = row.find_all('td')
        contests_cols = [ele.text.strip() for ele in contests_cols]
        if contests_cols:
            contests_data[int(contests_cols[0])] = {
                'Contest' : contests_cols[1],
                'Rank' : contests_cols[2],
                'Solved' : contests_cols[3],
                'Rating change' : contests_cols[4],
                'New rating' : contests_cols[5]
            }
    return save_data(contests_data)

def save_data(contests_data):
    with open('contests_data.txt', 'w') as contests_outfile:
        json.dump(contests_data, contests_outfile)

def output_HTML():
	global contests_soup
	print(contests_soup.prettify)

def output_data():
	global contests_data
	print(contests_data)