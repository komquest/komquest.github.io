# awesome.py

```python 
#!/usr/bin/python3

#This file will take in a "json" line file and parse it.
#You have different kinds of search: single, greedy, and EVERYTHING (recursive greedy search)
#greedy = grab everything with file

#Good link to help with file and dir malipulation:
#https://realpython.com/working-with-files-in-python/

#Defaultdict explanation:
#https://docs.python.org/2/library/collections.html
#and how to use them for dynamic memory allocation:
#https://python-forum.io/Thread-Create-a-new-list-dynamically

import json
import os
import argparse
import fnmatch
from pathlib import Path
from collections import Counter
#This can help allocate Lists dynamically
from collections import defaultdict


#Argument Parser
parser = argparse.ArgumentParser(description='Parse a JSON File!!!')
parser.add_argument('files', type=str, nargs=1, help='File Name or Path')

args = parser.parse_args()

filePath=args.files[0]

#List Dir

#dirs = os.scandir(filePath)

#for entry in dirs:
#        print(entry.name)

#global massiveList
#massiveList = []
#global massiveString
#massiveString = ""


#IDEAS
#splicer path search runNumber
#traffic = Greedy and Single Greedy

#Function(http, dns, etc)(filePath,Greediness)

#Todo:
#1 Make the Json parser X
#2 Start building your specific parsers:
    #Http, traffic, etc
#3 Learn how to write log files and make dirs!!!

#Todo: (above stuff and:)
#1. My idea for processing Load files --> Parse Json --> preCount  Processing --> Count --> Post Count Processing (add csv header here) --> Write results Dir --> Write csv Files
#Implent that above starting at "preCount Processing"


class Splicer:

        def __init__(self):
            
            self.paths = ""
            #0 = Single
            #1 = Single Greedy
            #2 = Greedy
            #3 = Greedy Recursive
            #4 = Single Greedy Recursive???
            self.searches = 0

            #The phases of how we count and parse the json files
            #self.jsonString
            #self.jsonList
            #self.jsonDict

        #Utility Functions

        #ParseFiles will return a list that contains lists of what was found in the Json Files
        #for the most part this will be a list with one list of json lines, however, if 
        #Single Greedy (1) is selected then it will be a list of many lists of json lines
        #"anchor" is the string to match for in the filePath directory
        def ParseFiles(self,filePath, greedy,anchor):
            
            jsList = []
            jsHolderList = []
            #This is for a single file
            if (greedy == 0):
                with open(filePath) as f:
                        for line in f:
                            jsList.append(line)
                return jsList
            #Otherwise we lookup files based off of an expression search    
            else:    
                basepath = Path(filePath)
                files_in_basepath = basepath.iterdir()
                for item in files_in_basepath:
                    if item.is_file():
                        if fnmatch.fnmatch(item.name, anchor + "*"):
                            with open(basepath.name + item.name) as f:
                                for line in f:
                                    jsList.append(line)
                            #if your greedy value is for singles, make sure you make a separator
                            #so that you can pull out different files
                            #Print out the name between data sets
                            if (greedy == 1 or greedy == 4): 
                                    jsList.append(basepath.name + item.name)
            
                return jsList

        #This will take in a list of json lines and file names and then
        #parse. Put in list of jsonLines, then a list of keys to look for
        def ParseJson(self,jsonList, keys):
            listDict = defaultdict(list)
            holderString = ""
            counter = 0

            for line in jsonList:
                if (line[0] == "{"):
                    jsonLine = json.loads(line)
                    for k, v in jsonLine.items():
                        if (k in keys):
                            holderString += v + ','
                            holderString = holderString[:-1]
                            listDict[counter].append(holderString)
                            holderString = ""
                #Assume Filename
                else:
                    listDict[counter].append(line)
                    counter = counter + 1
                    

            return listDict
                

                

                


def ProcessJSON(fPath):
    massiveList = []
    massiveString = ""
    #headerString="counted,"
    with open(fPath) as f:
            for line in f:
            #       print(line, end='')
                jsonLine = json.loads(line)
                #print(jsonLine.keys())
                for k, v in jsonLine.items():
                    massiveString += v + ','
                massiveString = massiveString[:-1]
                massiveList.append(massiveString)
                massiveString = ""

    #for item in massiveList:
    #       print(item)
    counted = dict(Counter(massiveList))

    #for k, v in counted.items():
    #    print(str(v) + "," + k)

    sortedList = sorted(counted.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)  


    #print(headerString)
    print("count,ts,uri")
    for item in sortedList:
        print(str(item[1]) + "," + item[0])

def Scratch():
    fPattern = '*'
    basepath = Path(filePath)
    #print(basepath.name)
    files_in_basepath = basepath.iterdir()
    for item in files_in_basepath:
        if item.is_file():
            if fnmatch.fnmatch(item.name, fPattern):
                print(item.name)
        else:
            #Recursion, note this only goes one deep, since that is my use case at the moment
            subPath = Path(basepath.name + "/" + item.name)
            files_in_subPath = subPath.iterdir()
            for subItem in files_in_subPath:
                if subItem.is_file():
                    if fnmatch.fnmatch(subItem.name, fPattern):
                        print("Sub!: " + subItem.name)


#This demonstrates that I can usthe default dictionary features to dynamically
#allocate Memeory
def DDict():
    d = defaultdict(list)

    for i in range(10):
        d[i].append("Woot")
    
    for j,k in d.items():
        print(k)
                


#ProcessJSON(filePath)

#MAIN

a = Splicer()
testList = a.ParseFiles(filePath,1,"test")
testDict = a.ParseJson(testList,["ts", "headers"])

for k, v in testDict.items():
    print(k)
    print("###############################################################")
    for i in v:
        print(i)
#print(testDict)
#print(testList)
#print(type(testList))

#DDict()






```