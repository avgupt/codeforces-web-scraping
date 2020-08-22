import urllib.request, json

only_active = "false"
query = "https://codeforces.com/api/user.ratedList" + only_active + "?lang=en"

with urllib.request.urlopen(query) as url:
	data = json.loads(url.read().decode())
print(data["result"][0].keys())
#print(data["result"])
#print(size(data["status"]))
#for i in range(10):
#	l = data["result"]
#	print(l[i])
	
