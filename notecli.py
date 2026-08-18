from noteManager import *
from noteWriter import *
from txtParser import *

class NotesCLI:
    def __init__(self):
        self.manager = NoteManager()

    def newFile(self):
        clearConsole()
        name = input("Note name: ")

        if name in self.manager.notes:
            print("A note with that name already exists.")
            input("Press ENTER to continue.")
            return False

        note = self.manager.createNote(name)
        self.manager.addNote(name, note)
        return True

    def editFile(self):
        clearConsole()
                                
        self.manager.displayNoteNames()
        print("")

        name = input("Note name to edit: ")
        note = self.manager.loadNote(name)

        if note is None:
            print("Note not found.")
            input("Press ENTER to continue.")
            return False

        writer = NoteWriter(
            name,
            note["tags"],
            note["lines"]
        )

        note["lines"] = writer.getDetailedInput()

        self.manager.saveNote(name, note)
        return True

    def deleteFile(self):
        clearConsole()
        self.manager.displayNoteNames()
        print("")
        name = input("Note name to delete: ")

        if name == "" or name.startswith(" "):
            print("Invalid note name.")
            input("Press ENTER to continue.")
            return False

        yn = input("Are you sure you want to delete this note? (y/n): ")

        if yn == "y":
            if self.manager.deleteNote(name):
                print("Note deleted.")
            else:
                print("Note not found.")
        elif yn == "n":
            print("OK. Cancelled.")

        input("Press ENTER to continue.")
        return True

    def editTags(self):
        clearConsole()
        
        self.manager.displayNoteNames()
        print("")

        name = input("Note name to edit tags: ")

        if self.manager.editFileTags(name):
            print("Tags updated.")
        else:
            print("Note not found.")
            input("Press ENTER to continue.")

    def searchByTag(self):
        clearConsole()
        
        tag = input("Search tag: ")

        print("")
        self.manager.displayNotesByTag(tag)

        input("Press ENTER to continue.")

    def convertNoteToTxt(self):
        clearConsole()
        self.manager.displayNoteNames()

        name = input("File to convert to .txt: ")
        note = self.manager.loadNote(name)
        if (note == None):
            print("No note found.")
            return 

        fileName = input("File found. Enter the name to save it as: ")

        txt = TxtFileParser.generateTextFile(name, note["tags"], note["lines"])
        TxtFileParser.saveToFile(fileName,  txt)

        print(f'Succesfully saved {name} as ./txtOutput/{fileName}.txt.')
        input("Press ENTER to continue.")


    def drawMainMenu(self):
        clearConsole()
        
        print("NotesCLI                                      - by 7projected")
        print("A keyboard-first note management software.")
        print("")
        print("!new                      Create a new note.")
        print("!edit                     Edit a note.")
        print("!del                      Delete a note.")
        print("!tag                      Search notes by tag.")
        print("!edittags                 Edit a note's tags.")
        print("!totxt                    Saves a note to a .txt file")
        print("!quit                     Exit the program.")
        print("")

    def mainLoop(self):
        while True:
            self.drawMainMenu()
            userInput = input("> ")
            
            match userInput:
                case "!new":
                    if self.newFile() == False: continue
                case "!edit":
                    if self.editFile() == False: continue
                case "!del":
                    if self.deleteFile() == False: continue
                case "!tag":
                    self.searchByTag()
                case "!edittags":
                    self.editTags()
                case "!totxt":
                    self.convertNoteToTxt()
                case "!quit":
                    break
                case _:
                    print("Unknown command.")
                    input("Press ENTER to continue.")