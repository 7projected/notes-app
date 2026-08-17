from enum import Enum
import os


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def showHelp():
    clearConsole()

    l = [
        "!!        = Exits and saves the note.",
        "!edit     = Overrides the selected line.",
        "!rm       = Removes the selected line.",
        "!help     = Shows this help menu.",
        "!new      = Goes to the newest line in the document.",
        "!prev     = Goes to the previous line.",
        "!next     = Goes to the next line.",
        "!clear    = Clears all of the notes in the document."
    ]

    for line in l:
        print(line)

    print("\n" * 5)

    input("Press ENTER to exit this menu.")


class ConsoleCommand(Enum):
    EXIT = 0
    TYPE = 1


class NoteWriter:
    def __init__(self, name, tags, lines=None):
        self.lines = lines if lines is not None else []
        self.currentLine = len(self.lines)
        self.name = name
        self.tags = tags
        self.command = ConsoleCommand.TYPE

        self.preUIline = "Type !help to see commands."

    def drawBasicUI(self):
        clearConsole()

        print(self.preUIline)
        print(f"File: {self.name}")
        print(f"Tags: {self.tags}")
        print("-" * 60)

        for index, line in enumerate(self.lines):
            print(f"{index + 1:>3} | {line}")

        print("-" * 60)

    def removeLine(self):
        self.drawBasicUI()

        try:
            # Convert user's 1-based number to Python's 0-based index
            lineNumber = int(input("Remove line number: ")) - 1

            if 0 <= lineNumber < len(self.lines):
                self.lines.pop(lineNumber)
                self.command = ConsoleCommand.TYPE
                self.currentLine = max(0, self.currentLine - 1)
            else:
                self.preUIline = "Invalid line number."

        except ValueError:
            self.preUIline = "Please enter a valid number."

    def editLine(self, lineNumber):
        self.drawBasicUI()

        if 0 <= lineNumber < len(self.lines):
            self.command = ConsoleCommand.TYPE
            self.currentLine = lineNumber
        else:
            self.preUIline = "Invalid line number."

    def clearAll(self):
        clearConsole()

        f = input("If you REALLY want to delete this whole note document type PLEASEDEL: ")
        
        if f == "PLEASEDEL":
            self.lines = []
            self.currentLine = 0

    def getDetailedInput(self):
        clearConsole()

        while self.command != ConsoleCommand.EXIT:
            self.drawBasicUI()

            # Display current line as 1-based
            userInput = input(f"{self.currentLine + 1:>3} | ")

            if userInput.startswith("!"):
                if userInput.startswith("!help"):
                    showHelp()

                elif userInput.startswith("!rm"):
                    self.removeLine()

                elif userInput.startswith("!edit"):
                    try:
                        # Convert user's 1-based number to 0-based index
                        lineNumber = int(input("Edit line number: ")) - 1
                        self.editLine(lineNumber)
                    except ValueError:
                        self.preUIline = "Please enter a valid number."

                elif userInput.startswith("!!"):
                    self.command = ConsoleCommand.EXIT
                    continue

                elif userInput.startswith("!new"):
                    self.currentLine = len(self.lines)

                elif userInput.startswith("!prev"):
                    if self.currentLine > 0:
                        self.currentLine -= 1

                elif userInput.startswith("!next"):
                    self.currentLine += 1

                elif userInput.startswith("!clear"):
                    self.clearAll()

            else:
                if self.currentLine >= len(self.lines):
                    self.lines.append(userInput)
                else:
                    self.lines[self.currentLine] = userInput

                if self.command == ConsoleCommand.TYPE:
                    self.currentLine += 1

        return self.lines