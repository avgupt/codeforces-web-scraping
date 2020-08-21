import urllib.request, json

only_active = "false"
query = "https://codeforces.com/api/user.ratedList"

with urllib.request.urlopen(query) as url:
	data = json.loads(url.read().decode())
	print(data)
