#!/usr/bin/env python
import os, sys, json, webbrowser

# 1. compile .coffee files
command = "coffee --compile --output static/_coffee/ scripts/"
os.system(command)

# 2. pre-compile .handlebars files
templatesListFilename = "scripts/templatesList.json"
jsonData = open(templatesListFilename).read()
data = json.loads(jsonData)

origPathPrefix = "scripts/templates/"
newPathPrefix = "static/_handlebars/"

for origName in data:
  newName = ".".join(origName.split(".")[:-1]) + ".js"
  origPath = origPathPrefix + origName
  newPath = newPathPrefix + newName
  command = "handlebars %s -f %s" % (origPath, newPath)
  os.system(command)

# 3. launch website
url = "http://localhost:5000"
webbrowser.open(url, new = 0)