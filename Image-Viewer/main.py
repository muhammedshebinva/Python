from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")
root.geometry("500x500")


image1 = Image.open("me1.jpg")
resize_image1 = image1.resize((500,450))
my_image1 = ImageTk.PhotoImage(resize_image1)

image2 = Image.open("me2.jpg")
resize_image2 = image2.resize((500,450))
my_image2 = ImageTk.PhotoImage(resize_image2)

image3 = Image.open("me3.jpg")
resize_image3 = image3.resize((500,450))
my_image3 = ImageTk.PhotoImage(resize_image3)

image4 = Image.open("me4.jpg")
resize_image4 = image4.resize((500,450))
my_image4 = ImageTk.PhotoImage(resize_image4)

image_list = [my_image1, my_image2, my_image3, my_image4]



label = Label(image=my_image1)
label.grid(row=0, column=0, columnspan=4)

def forward(image_number):
    global label
    global button_forward
    global button_back

    label.grid_forget()
    label = Label(image = image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda : forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda :backward(image_number-1))

    if image_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=4)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=3)


def backward(image_number):
    global label
    global button_forward
    global button_back

    label.grid_forget()
    label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: backward(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=4)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=3)


button_back=Button(root,text="<<", command=backward, state=DISABLED)
button_exit=Button(root,text="exit", command=root.quit)
button_forward=Button(root,text=">>", command= lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1, column=1, columnspan=2)
button_forward.grid(row=1, column=3)


root.mainloop()


