import json
import urllib.request
from api import *
import ssl
import os

def getData():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context

    #opening the philpapers json data and turning it into a string
    url = "https://philpapers.org/philpapers/raw/categories.json?apiId="+apiKey + "&apiKey="+ userID
    openedUrl = urllib.request.urlopen(url)
    urlContent = openedUrl.read().decode('utf-8')
    data = json.loads(urlContent)
    jsonString=json.dumps(data)

    #replace all of the extraneous stuff
    jsonString=jsonString.replace("], [","\n")
    jsonString=jsonString.replace("[[", "")
    jsonString=jsonString.replace("]]", "")

    os.chdir(os.path.dirname(__file__))
    os.chdir("..")
    os.chdir("data")

    #write the modified json string to a text file
    with open("PhilpapersTaxonomy.txt", 'w') as f:
        f.write(jsonString)
        f.close()
