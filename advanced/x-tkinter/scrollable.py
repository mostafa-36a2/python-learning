# Import the required library
from tkinter import *

# Create an instance of tkinter frame
win = Tk()
win.title("Scrollable")
# Set the geometry
win.geometry("700x350")

# Add a Scrollbar(horizontal)
v = Scrollbar(win, orient="vertical")
v.pack(side=RIGHT, fill="y")

# Add a text widget
text = Text(win, font=("Georgia, 12"), yscrollcommand=v.set)

# Add some text in the text widget
file = open(
    "/home/mostafa/Documents/Python/Lessons/Lessons/tkinter/file_input.txt", "r"
)
text.insert(END, file.read())

# Attach the scrollbar with the text widget
v.config(command=text.yview)
text.pack()

win.mainloop()
