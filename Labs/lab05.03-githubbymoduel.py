#

import requests
import json


from github import Github
from config import apikeys as cfg

apikey = cfg["aprivateone"]
g = Github(apikey)

#for repo in g.get_user():
#  print(repo.name)

repo = g.get_repo("Kevin002023/aprivateone")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
#print(contentOfFile)

newContents = contentOfFile + "more stuff \n"
#print(newContents)

githubResponse = repo.update_file(fileInfo.path, "updated by prog", newContents, fileInfo.sha)
print(githubResponse)