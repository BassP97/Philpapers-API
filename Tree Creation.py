from anytree import Node, RenderTree, AnyNode
from anytree.exporter import JsonExporter
from csv import reader
import json

philFile = open('PhilpapersTaxonomy.txt', 'r')

nodes = {"1":Node("root")}

#for every line in our extracted philpapers taxonomy, make a new node for our tree
for line in reader(philFile):
    #get just the integers from our ID (get rid of spaces, commas, etc...) though we keep them as strings
    currID=''.join(filter(str.isdigit, line[1]))

    #create N nodes. the key for each node is the ID from philFile, meaning that we can
    #access any arbitrary category using its ID
    nodes[currID]=(Node("temp"))

#reset out position in philFile so we can restart from the front
philFile.seek(0)

#remember that our file is organized as follows ["name" "ID" "parent IDs" "primary parent ID"]
for line in reader(philFile):
    #Take the ID number of the category and find the corresponding node from our dictionary
    #after finding said node, we set its parent node to the corresponding node from our dictionary
    #We also get just the integers from our ID (get rid of spaces, commas, etc...) though we keep them
    #as strings so that they play nice with the dictionary
    currID=''.join(filter(str.isdigit, line[1]))
    currParentID=''.join(filter(str.isdigit, line[len(line)-1]))
    currName = line[0]
    currName=str(currName)

    #set the current node's name to the corresponding name
    nodes[currID].name = currName
    #we then set the parent ID to the primary parent ID
    nodes[currID].parent=nodes[currParentID]

philFile.close()

#export our tree to json
exporter = JsonExporter(indent=2, sort_keys=True)
with open('data.json', 'w') as f:
    exporter.write(nodes["1"],f)

#uncomment to check tree contents
#print(exporter.export(nodes["1"]))
