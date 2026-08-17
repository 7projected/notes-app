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

        note = manager.createNote()
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
        yn = input("Are you sure? (y/n): ")
        if (yn == "y"):
            if manager.deleteNote(name):
                print("Note deleted.")
            else:
                print("Note not found.")
        elif (yn == "n"):
            print("Cancelled.")

        input("Press ENTER to continue.")

    elif userInput == "!quit":
        break

    else:
        print("Unknown command.")
        input("Press ENTER to continue.")