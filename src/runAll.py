import CreateJson as getJson
import GETserver as server
import getPhilpapersData as Extraction

if __name__ == "__main__": 
    Extraction.getData()
    getJson.createJson()
    server.startServer()