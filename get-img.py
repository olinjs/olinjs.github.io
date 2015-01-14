import json, requests

def updateperson(person):
	if not person["github"]:
		person["github"] = "segerphilip"
	token = "a5e92af24222b2218d6b6a2c073ef017bf67123c"
	userdata = requests.get("https://api.github.com/users/"+person["github"], auth=(token, "")).json()

	print person["name"]
	person["image"] = userdata["avatar_url"]
	person["githuburl"] = "http://www.github.com/"+person["github"]

	return person

##

with open("./jade/in.json") as jsonfile:
	index = json.load(jsonfile)

index["teachers"] = map(updateperson, index["teachers"])
index["ninjas"] = map(updateperson, index["ninjas"])
index["students"] = map(updateperson, index["students"])

print "Done!"

with open("./jade/index.json", "w") as jsonfile:
	json.dump(index, jsonfile, indent=4, separators=(',', ': '))