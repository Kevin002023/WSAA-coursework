import requests 
import json

urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAll(dataset):
  url = urlBeginning + dataset + urlEnd
  response = requests.get(url)
  return response.json()

def getAll(dataset):
  url = urlBeginning + dataset + urlEnd
  response = requests.get(url)
  return response.json()

def getFormattedAsFile(dataset):
  with open("cso-formatted.json", "wt") as fp:
    print(json.dumps(getFormatted(dataset)), file=fp)


def getFormatted(dataset):
  data = getAll(dataset)
  ids = data["id"]
  values = data["value"]
  dimensions= data["dimension"]
  sizes = data["size"]
  valuecount = 0
  result = {}

  for dim0 in range(0, sizes[0]):
    currentId = ids[0]
    index = dimensions[currentId]["category"]["index"][dim0]
    label0 = dimensions[currentId]["category"]["label"][index]
    result[label0]={}
    #currentDict = currentDict[label]
    #print(label)
    for dim1 in range(0, sizes[1]):
      currentId = ids[1]
      index = dimensions[currentId]["category"]["index"][dim1]
      label1 = dimensions[currentId]["category"]["label"][index]
      result[label0][label1] = {}
      #currentDict = currentDict[label]
      #print("\t",label)
      
      for dim2 in range(0, sizes[2]):
        currentId = ids[2]
        index = dimensions[currentId]["category"]["index"][dim2]
        label2 = dimensions[currentId]["category"]["label"][index]
        result[label0][label1][label2] = {}
        #print("\t\t",label)
        
        for dim3 in range(0, sizes[3]):
          currentId = ids[3]
          index = dimensions[currentId]["category"]["index"][dim3]
          label3 = dimensions[currentId]["category"]["label"][index]
          result[label0][label1][label2][label3] = values[valuecount]
          valuecount+=1

  return result

  #for id in ids:
  # print(id)
  
  

if __name__  == "__main__":
  #with open("2cso.json", "wt") as fp:
  #  print(json.dumps(getAll("FP001")), file=fp)
  getFormattedAsFile("FP001")