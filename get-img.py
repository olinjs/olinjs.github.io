import json, requests

with open("token.txt") as f:
    token = f.readline().strip()

def updateperson(person):
	if not person["github"]:
		person["github"] = "olinjs"
	userdata = requests.get("https://api.github.com/users/"+person["github"], auth=(token, "")).json()

	print person["name"]
	person["image"] = userdata["avatar_url"]
	person["githuburl"] = "http://www.github.com/"+person["github"]

	return person

##

with open("./content/input.json") as jsonfile:
	index = json.load(jsonfile)

index["teachers"] = map(updateperson, index["teachers"])
index["ninjas"] = map(updateperson, index["ninjas"])
index["students"] = map(updateperson, index["students"])

print "Done!"

with open("./content/index.json", "w") as jsonfile:
	json.dump(index, jsonfile, indent=4, separators=(',', ': '))
