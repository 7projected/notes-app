import tkinter as tk
from tkinter import messagebox

def verify_action():
    # Returns True if OK is pressed, False if Cancel is pressed
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

root = tk.Tk()
root.geometry("200x100")

btn = tk.Button(root, text="Click Me", command=verify_action)
btn.pack(pady=20)

root.mainloop()
