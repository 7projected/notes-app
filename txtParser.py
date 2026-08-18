class TxtFileParser:
    @staticmethod
    def generateTextFile(name, tags, textLines):
        retTxt = f'Name: {name} \n'
        retTxt += f'Tags: '
        for i, tag in enumerate(tags):
            retTxt += f'{tag}'
            if i < len(tags) - 1:
                retTxt += ', '

        # Tags and name are done, now add each line

        retTxt += "\n"
        retTxt += "\n"

        for i, line in enumerate(textLines):
            retTxt += line
            retTxt += "\n"

        return retTxt

    @staticmethod
    def saveToFile(name, txt):
        with open(f"txtOutput/{name}.txt", "w") as file:
            file.write(txt)