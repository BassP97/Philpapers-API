# PhilPapers JSON API reorganization

This project gathers, restructures, and serves up Philpapers' API's json data on a web server written in python.

## Overview
The Philpapers JSON API is, while usable, not optimized to best use the JSON file format. The Philpapers API is supposed to provide the user with every category on the site organized into parent and child categories. For instance, virtue ethics is ethics' child, since Ethics is the category under which virtue ethics falls. One would expect this JSON data to take advantage of JSON's inbuilt tree file structure, but unfortunately it does not. This makes the json difficult to use and navigate.

The philpapers JSON API has the following data for each category: ["category name", "category ID", "list of parent IDs", "Primary Parent ID"] and is structured as a list

This repo contains several files that attempt to restructure the API using the python library "anytree". Extractionandformatting.py gets the json data and formats it for Tree Creation.py to use and parse. Tree Creation.py uses the anytree module to restucture the JSON data into a tree structure and writes it to a new JSON file, which is then served up on socket 8008. 

## Installing and Running
After cloning the repo, install (via pip) the "anytree" library using the command "pip anytree". You also need your own philpapers.org API key and user ID (both of which you can obtain here: https://philpapers.org/help/api), which need to be placed into a python file called "api.py" in the ./src folder. In "api.py" create two strings, "apiKey" and "userID", which should contain your philpapers API key and user ID respectively. After both these steps, the user can run "runAll.py" to create a web server that serves up json data on port 8008!

