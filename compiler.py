#!/usr/bin/env python
import os, sys, json, webbrowser

def compileCoffee():
  command = "coffee --compile --output static/js/ scripts/"
  os.system(command)

def compileHandlebars():
  templatesListFilename = "scripts/templatesList.json"
  jsonData = open(templatesListFilename).read()
  data = json.loads(jsonData)

  origPathPrefix = "scripts/templates/"
  newPathPrefix = "static/templates/"

  for origName in data:
    newName = ".".join(origName.split(".")[:-1]) + ".js"
    origPath = origPathPrefix + origName
    newPath = newPathPrefix + newName
    command = "handlebars %s -f %s" % (origPath, newPath)
    os.system(command)

def compileLess():
  stylesListFilename = "scripts/stylesList.json"
  jsonData = open(stylesListFilename).read()
  data = json.loads(jsonData)

  origPathPrefix = "scripts/styles/"
  newPathPrefix = "static/styles/"

  for origName in data:
    newName = ".".join(origName.split(".")[:-1]) + ".css"
    origPath = origPathPrefix + origName
    newPath = newPathPrefix + newName
    command = "lessc %s %s" % (origPath, newPath)
    os.system(command)

def launch():
  url = "http://localhost:5000"
  webbrowser.open(url, new = 0)  

compileCoffee()
compileHandlebars()
compileLess()
launch()