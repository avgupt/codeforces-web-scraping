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
			result.append([i['handle'], i['country'], i['maxRating']])
		else:
			result.append([ i['handle'], "Unknown", i['maxRating']])

	result = sorted(result, key=lambda x: -x[2])

	print_data(result)
	return save_data(result)


def save_data(user_list):
	with open('user_list.txt', 'w') as outfile:
		json.dump(user_list, outfile)

def print_data(user_list):
	for i in user_list:
		print( str(user_list.index(i)) + " " + i[0] + " " + i[1] + " " + str(i[2]))


listOfUsers(200)



	
