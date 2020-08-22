import urllib.request, json

only_active = "false"
query = "https://codeforces.com/api/user.ratedList?activeOnly=" + only_active + "?lang=en"


def listOfUsers():
	with urllib.request.urlopen(query) as url:
		data = json.loads(url.read().decode())
	users = data["result"]
	print(type(users))
	return save_data(users)

def save_data(user_list):
	with open('user_list.txt', 'w') as outfile:
		json.dump(user_list, outfile)

listOfUsers()


	
