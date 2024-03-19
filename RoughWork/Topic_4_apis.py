# API's

import requests

url ="http://andrewbeatty1.pythonanywhere.com/books"
#url = "http://google.com"


response = requests.get(url)
print(response.text)

#def getallbooks():
#  response = requests.get(url)
#  return response.json()

#if __name__ =="__main__":
#  print(getallbooks())
