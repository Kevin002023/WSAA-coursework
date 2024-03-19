# Accessing a private repository on github using an API key

import requests
import urllib.parse
import json
from config import apikeys as cfg

filename = "private-repositories.json"

#url = 'https://api.github.com/users/Kevin002023/repos?per_page=100'
url = 'https://api.github.com/repos/Kevin002023/aprivateone/contentse'


apikey = cfg["aprivateone"]

response = requests.get(url, auth=('token', apikey))
print(response.status_code)

reposit = response.json()
#print(reposit)

with open(filename, 'w') as fp:
  json.dump(reposit, fp, indent=4)

#print (response.status_code)
#result =response.content
