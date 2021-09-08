import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

def main():
    webURL = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php")
    print("result code: " + str(webURL.getcode()))


if __name__ == "__main__":
    main() 