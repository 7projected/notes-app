import json
from noteWriter import NoteWriter, clearConsole




class NoteManager:
    def __init__(self, fileName="notes.json"):
        self.fileName = fileName
        self.notes = self.loadNotes()

    def loadNotes(self):
        try:
            with open(self.fileName, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            return {}

        except json.JSONDecodeError:
            return {}

    def saveNotes(self):
        with open(self.fileName, "w") as file:
            json.dump(self.notes, file, indent=4)

    def getFileTags(self):
        tags = []
        lastValue = ""

        while lastValue != "!!":
            clearConsole()

            print("Current Tags:")
            for tag in tags:
                print(f"- {tag}")

            print("-" * 60)
            print("Type !! to confirm.")
            print("Type << to remove the last tag.")

            lastValue = input("Input: ")

            if lastValue != "" and lastValue != " ":
                if lastValue != "!!" and lastValue != "<<":
                    tags.append(lastValue)

                elif lastValue == "<<":
                    if len(tags) > 0:
                        tags.pop()

        return tags

    def createNote(self):
        clearConsole()

        tags = self.getFileTags()

        writer = NoteWriter("", tags)
        lines = writer.getDetailedInput()

        return {
            "tags": tags,
            "lines": lines
        }

    def addNote(self, key, note):
        self.notes[key] = note
        self.saveNotes()

    def loadNote(self, key):
        if key in self.notes:
            return self.notes[key]

        return None

    def saveNote(self, key, note):
        self.notes[key] = note
        self.saveNotes()

    def deleteNote(self, key):
        if key in self.notes:
            del self.notes[key]
            self.saveNotes()
            return True

        return False

    def displayNoteNames(self):
        if len(self.notes) == 0:
            print("No notes found.")
            return

        print("Notes:")
        print("-" * 60)

        for name in self.notes:
            print(name)

        print("-" * 60)