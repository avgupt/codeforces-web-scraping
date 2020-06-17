import requests, json
from bs4 import BeautifulSoup

sub_soup = ""
sub_data = ""

def extract_data(username):
    sub_page_num = 1
    sub_URL = "https://codeforces.com/submissions/" + username + "/page/" + str(sub_page_num)
    sub_table_body = ""

    global sub_soup, sub_data
    sub_data = {}
    while True:
        sub_page = requests.get(sub_URL)
        
        sub_soup = BeautifulSoup(sub_page.content, 'html.parser')
        sub_table = sub_soup.find('div', 'datatable')
        temp = sub_table.find('table', 'status-frame-datatable')
        if sub_table_body == temp:
            break
        sub_table_body = temp
        sub_rows = sub_table_body.find_all('tr')
        for row in sub_rows:
            sub_cols = row.find_all('td')
            sub_cols = [ele.text.strip() for ele in sub_cols]
            if sub_cols and sub_cols[0] != "No items":
                sub_data[int(sub_cols[0])] = {
                    'When' : sub_cols[1],
                    'Who' : sub_cols[2],
                    'Problem' : sub_cols[3],
                    'Lang' : sub_cols[4],
                    'Verdict' : sub_cols[5],
                    'Time' : sub_cols[6],
                    'Memory' : sub_cols[7]
                }
        sub_page_num += 1
        sub_URL = "https://codeforces.com/submissions/" + username + "/page/" + str(sub_page_num)
    return save_data(sub_data)

def save_data(sub_data):
    with open('submissions_data.txt', 'w') as sub_outfile:
        json.dump(sub_data, sub_outfile)
    return

def output_HTML():
	global sub_soup
	print(sub_soup.prettify)

def output_data():
    ''' Prints data on last page'''
    global sub_data
    print(sub_data)