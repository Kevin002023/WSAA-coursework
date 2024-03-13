# assignment04-github.py 
# Read a file from a respository, replace all instances of the word "Andrew" with my name "Kevin" and then commit the changes and push the file back to the repository
# Kevin O'Leary


# First I created a text file by copying the wikipedia entry for the name Andrew. This was added to my github repository 'aprivateone' that needs a token to allow access. 
# source = https://en.wikipedia.org/wiki/Andrew

import requests
import urllib.parse
import json
from config import apikeys as cfg

# The fine grained token is stored in another file config.py

from github import Github

apikey = cfg["aprivateone"]
g = Github(apikey)

#for repo in g.get_user().get_repos():
#  print(repo.name)

# The file we want is in our private repository 'aprivateone'

repo = g.get_repo("Kevin002023/aprivateone") 
#print(repo.clone_url) # check its connecting with correct repository

file = repo.get_contents("Andrew.txt")
urlOfFile = file.download_url
#print(urlOfFile)

response = requests.get(urlOfFile)
content = response.text
#print(content)

updatedContents = content.replace("Andrew", "Kevin").replace("andrew", "kevin") # Probably irrelevant for a name but I wanted to make case insensitive, so it could be used for other words.
#print(updatedContents)

githubResponse = repo.update_file(file.path, "Replaced Andrew with Kevin", updatedContents, file.sha)
print(githubResponse)

