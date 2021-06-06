from tkinter import *
from PIL import ImageTk, Image

root = Tk()
#title
root.title("Images")
#window icon
root.iconbitmap("logo.ico")
#image adding
my_image = ImageTk.PhotoImage(Image.open("mountain.jpg"))
label = Label(image=my_image)
label.pack()

root.mainloop()
