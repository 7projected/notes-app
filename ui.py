import tkinter
import os

def getFileTags():
    retValue = []
    lastValue = ""
    
    while lastValue != "!!":
        os.system('cls' if os.name == 'nt' else 'clear') # clear console
        outputString = "Current Tags: "
        for i in range(len(retValue)):
            outputString += f'{retValue[i]}, '
        
        print(outputString)
        print("Type !! to confirm")
        print("Type << to remove last tag")
        
        lastValue = input("Input: ")
        
        if lastValue != " " and lastValue != "":
            if lastValue != "!!" and lastValue != "<<":
                retValue.append(lastValue)
            if lastValue == "<<":
                if len(retValue) >= 1:
                    retValue.pop()
    
    return retValue
    

def getDetailedInput(fileName):
    return ""


def getFileCreationInput():
    retValue = {
        "name":"",
        "text":"",
        "tags":[]
    }
    
    retValue["name"] = input("File Name: ")
    retValue["text"] = getDetailedInput(retValue["name"])
    retValue["tags"] = getFileTags()
    
    return retValue