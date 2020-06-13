import urllib.request
import sys
import re
import json


# Get ID from url
id = re.split(r"/", sys.argv[1])[-1]
# print(id)

# api-endpoint
URL = "http://api.rtvslo.si/ava/getRecording/{id}?client_id=82013fb3a531d5414f478747c1aca622".format(id=id)
print("URL: " + URL)

# extracting data in json format
webURL = urllib.request.urlopen(URL)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
data = json.loads(data.decode(encoding))
# print("DATA: "+ str(data))

# composing the url

server = data['response']['mediaFiles'][0]['streamers']['http']
filename = data['response']['mediaFiles'][0]['filename']
filename = '/'+filename if filename[0] != '/' else filename

dow_name = re.split(r"/", filename)[-1]

address = "{s}{f}".format(s=server, f=filename)
# print("ADDRESS: "+ address)

try:
    urllib.request.urlretrieve(address, dow_name)
    print("DOWNLOADED")
except:
    print("ERROR")




