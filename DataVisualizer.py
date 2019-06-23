from __future__ import print_function
import sys
import json

with open("data.json", 'r') as f:
    data = json.load(f)

#create an array for all the edges of our tree
tree = []

def get_edges(convertedDict, parent=None):
    name = next(iter(convertedDict.keys()))
    if parent is not None:
        tree.append((parent, name))
    #iterate through all children of our current thing
    for item in convertedDict[name]["children"]:
        #does our current item have children?
        if isinstance(item, dict):
            get_edges(item, parent=name)
        else:
            tree.append((name, item))

get_edges(data)
