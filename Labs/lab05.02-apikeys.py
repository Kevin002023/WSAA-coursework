
import requests
import urllib.parse

from config import apikeys as cfg

targetUrl = 'https://en.wikipedia.org/wiki/Jamie_Osborne_(rugby_union)'
apiUrl = 'https://api.html2pdf.app/v1/generate'

apikey = cfg["htmltopdfkey"]

params = {'html': targetUrl,'apiKey': apikey}
parsedparams = urllib.parse.urlencode(params)

requestUrl = apiUrl +"?" + parsedparams 
print (requestUrl)

response = requests.get(requestUrl)

print (response.status_code)
result =response.content

with open("document.pdf", "wb") as handler:
    handler.write(result)