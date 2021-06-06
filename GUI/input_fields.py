from tkinter import *

root = Tk()
# input field using 'Entry'
e = Entry(root, width=50)
e.pack()
#default text in field
e.insert(0, "enter Your name")

# input field using Text widget
t = Text(root, height=2, width=40, borderwidth=5)
t.pack()


# get value from input field
def click_action():

    hello = "Hello" + e.get()
    label = Label(root, text=hello)
    label.pack()


click_button = Button(root, text="click",padx=30, command=click_action)
click_button.pack()

root.mainloop()
