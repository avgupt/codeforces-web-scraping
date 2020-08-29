import urllib.request, json

only_active = "false"
query = "https://codeforces.com/api/user.ratedList?activeOnly=" + only_active + "?lang=en"


def listOfUsers():

	with urllib.request.urlopen(query) as url:
		data = json.loads(url.read().decode())

	users = data["result"]

	result = []
	for i in range(len(users)):
		if 'country' in users[i]:
			result.append([users[i]['handle'], users[i]['country'], users[i]['maxRating']])
		else:
			result.append([ users[i]['handle'], "Unknown", users[i]['maxRating']])

	result = sorted(result, key=lambda x: -x[2])

	print_data(result)
	return save_data(result)


def save_data(user_list):
	with open('user_list.json', 'w') as outfile:
		json.dump(user_list, outfile)

def print_data(user_list):
	for i in user_list:
		print( str(user_list.index(i)+1) + " " + i[0] + " " + i[1] + " " + str(i[2]))


if __name__ == "__main__":  
	listOfUsers()



	
