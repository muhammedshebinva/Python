from tkinter import *

root = Tk()
# button creating
myButton = Button(root, text="Click Me")
myButton.pack()
# State Disabled
button2 = Button(root, text="Desabled", state=DISABLED)
button2.pack()

# to cange button size using - padx & pady
sizeButton = Button(root, text="click me", padx=50, pady=20)
sizeButton.pack()


# giving an action to the button
def onClick():
    mylabel = Label(root, text="U cliked the Button!!")
    mylabel.pack()


label_Btn = Button(root, text="Click Here", command=onClick)
label_Btn.pack()
# to change the color of button
color_btn = Button(root, text="style", fg="white", bg="blue")
color_btn.pack()


root.mainloop()
