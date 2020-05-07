import requests, json
from bs4 import BeautifulSoup

username = input(">")

main_URL = "https://codeforces.com/contests/with/" + username
main_page = requests.get(main_URL)


#starts here
main_soup = BeautifulSoup(main_page.content, 'html.parser')


main_table = main_soup.find_all('span',class_ ='user-red')
#for i in main_table:
#	print(i)
print(main_table)

