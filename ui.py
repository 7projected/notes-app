from noteWriter import *

def getFileTags():
    retValue = []
    lastValue = ""
    
    while lastValue != "!!":
        clearConsole()
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

def getFileCreationInput():
    retValue = {
        "name":"",
        "text":"",
        "tags":[]
    }

    clearConsole()
    retValue["name"] = input("File Name: ")
    retValue["tags"] = getFileTags()

    nw = NoteWriter(retValue["name"], retValue["tags"]) # <=== Right here is where you wwould input a saved files lines

    retValue["text"] = nw.getDetailedInput()
    
    return retValue