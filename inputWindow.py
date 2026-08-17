import tkinter as tk
from tkinter import messagebox

class TextInput:
    def __init__(self, parent):
        self.text = tk.Text(parent, wrap="word")
        self.text.pack(fill="both", expand=True)

    def insert(self, text):
        self.text.insert("end", text)

    def get(self):
        return self.text.get("1.0", "end-1c")

    def clear(self):
        self.text.delete("1.0", "end")


class Window:
    def __init__(self):
        self.lastText = ""
        self.saved = False
        
        self.window = tk.Tk()
        self.window.title("Note App Input")
        self.window.geometry("1280x720")
        
        self.text_input = TextInput(self.window)

        self.window.bind("<Control-s>", lambda event: self.save())
        self.window.protocol("WM_DELETE_WINDOW", exit)
        
        self.window.after(1, self.start)
        self.window.after(1, self.customLoop)
        
        self.window.mainloop()

    def save(self):
        self.lastText = self.text_input.get()
        self.saved = True

    def start(self):
        self.text_input.clear()

    def exit(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.window.destroy()

    def customLoop(self):
        if (self.lastText != self.text_input.get()): self.saved = False

        self.window.after(1, self.customLoop)
    

def __init__():
    win = Window()
    
__init__()