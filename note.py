class Note:
    name = ""
    text = ""
    tags = []
    
    def __init__(self, dict):
        self.name = dict["name"]
        self.text = dict["text"]
        self.tags = dict["tags"]
        
    def debug(self):
        st = f'Name: {self.name}, Text: {self.text}, Tags: {self.tags}'
        print(st)