from noteManager import *
from noteWriter import *


manager = NoteManager()


while True:
    clearConsole()

    print("Note Manager CLI      - by 7projected")
    print("")
    print("!new          Create a new note.")
    print("!edit         Edit a note.")
    print("!del          Delete a note.")
    print("!tag          Search notes by tag.")
    print("!edittags     Edit a note's tags.")
    print("!quit         Exit the program.")
    print("")

    userInput = input("Desired command: ")

    if userInput == "!new":
        clearConsole()

        name = input("Note name: ")

        if name in manager.notes:
            print("A note with that name already exists.")
            input("Press ENTER to continue.")
            continue

        note = manager.createNote(name)
        manager.addNote(name, note)

    elif userInput == "!edit":
        clearConsole()

        manager.displayNoteNames()
        print("")

        name = input("Note name to edit: ")
        note = manager.loadNote(name)

        if note is None:
            print("Note not found.")
            input("Press ENTER to continue.")
            continue

        writer = NoteWriter(
            name,
            note["tags"],
            note["lines"]
        )

        note["lines"] = writer.getDetailedInput()

        manager.saveNote(name, note)

    elif userInput == "!del":
        clearConsole()

        manager.displayNoteNames()
        print("")

        name = input("Note name to delete: ")
        yn = input("Are you sure you want to delete this note? (y/n): ")

        if (yn == "y"):
            if manager.deleteNote(name):
                print("Note deleted.")
            else:
                print("Note not found.")
        elif (yn == "n"):
            print("OK. Cancelled.")

        input("Press ENTER to continue.")

    elif userInput == "!tag":
        clearConsole()

        tag = input("Search tag: ")

        print("")
        manager.displayNotesByTag(tag)

        input("Press ENTER to continue.")

    elif userInput == "!edittags":
        clearConsole()

        manager.displayNoteNames()
        print("")

        name = input("Note name to edit tags: ")

        if manager.editTags(name):
            print("Tags updated.")
        else:
            print("Note not found.")
            input("Press ENTER to continue.")

    elif userInput == "!quit":
        break

    else:
        print("Unknown command.")
        input("Press ENTER to continue.")