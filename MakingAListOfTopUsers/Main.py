import urllib.request, json

only_active = "false"
query = "https://codeforces.com/api/user.ratedList?activeOnly=" + only_active + "?lang=en"


def listOfUsers(n):
	with urllib.request.urlopen(query) as url:
		data = json.loads(url.read().decode())
	users = data["result"][:n]

	result = []
	for i in users:
		if 'country' in i:
			result.append({'handle': i['handle'], 'country': i['country'], "maxRating": i['maxRating']})
		else:
			result.append({'handle': i['handle'], 'country': "Unknown", "maxRating": i['maxRating']})
		
		
	return save_data(result)

def save_data(user_list):
	with open('user_list.txt', 'w') as outfile:
		json.dump(user_list, outfile)

listOfUsers(10)


	
