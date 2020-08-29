import urllib.request, json

only_active = "false"
query = "https://codeforces.com/api/user.ratedList?activeOnly=" + only_active + "?lang=en"


def listOfUsers():

	with urllib.request.urlopen(query) as url:
		data = json.loads(url.read().decode())

	users = data["result"]

	result = {}
	for i in range(len(users)):
		if 'country' in users[i]:
			result[i] = [users[i]['handle'], users[i]['country'], users[i]['maxRating']]
		else:
			result[i] = [ users[i]['handle'], "Unknown", users[i]['maxRating']]

	result = {k: v for k, v in sorted(result.items(), key=lambda item: -item[1][2])}

	print_data(result)
	return save_data(result)


def save_data(user_list):
	with open('user_list.json', 'w') as outfile:
		json.dump(user_list, outfile)

def print_data(user_list):
	for i in user_list.keys():
		print( str(i+1) + " " + user_list[i][0] + " " + user_list[i][1] + " " + str(user_list[i][2]))


if __name__ == "__main__":  
	listOfUsers()



	
