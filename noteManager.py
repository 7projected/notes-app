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

    def getFileTags(self, currentTags=None):
        tags = currentTags.copy() if currentTags is not None else []
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
                    if lastValue not in tags:
                        tags.append(lastValue)

                elif lastValue == "<<":
                    if len(tags) > 0:
                        tags.pop()

        return tags

    def createNote(self, name):
        clearConsole()

        tags = self.getFileTags()

        writer = NoteWriter(name, tags)
        lines = writer.getDetailedInput()

        return {
            "tags": tags,
            "lines": lines
        }

    def addNote(self, name, note):
        self.notes[name] = note
        self.saveNotes()

    def loadNote(self, name):
        if name in self.notes:
            return self.notes[name]

        return None

    def saveNote(self, name, note):
        self.notes[name] = note
        self.saveNotes()

    def deleteNote(self, name):
        if name in self.notes:
            del self.notes[name]
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

    def searchByTag(self, tag):
        results = []

        for name, note in self.notes.items():
            if tag in note["tags"]:
                results.append(name)

        return results

    def displayNotesByTag(self, tag):
        results = self.searchByTag(tag)

        if len(results) == 0:
            print(f'No notes found with tag "{tag}".')
            return

        print(f'Notes with tag "{tag}":')
        print("-" * 60)

        for name in results:
            print(name)

        print("-" * 60)

    def editTags(self, name):
        note = self.loadNote(name)

        if note is None:
            return False

        note["tags"] = self.getFileTags(note["tags"])
        self.saveNote(name, note)

        return True