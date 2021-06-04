from tkinter import *

window = Tk()
# window.geometry("500x500")
window.title("Calculator")

# label = Label(window, text="welcome")
display = Entry(window, width=45, borderwidth=5)

display.grid(row=0, column=0, columnspan=5, padx=10, pady=20)


def hello():
    print("Hello")


def button_click(number):
    current = display.get()
    display.delete(0,END)
    display.insert(0,str(current) + str(number))
def clear_btn():
    display.delete(0,END)
def add_btn():
    global first_number
    global math
    math = "add"
    first_number=int(display.get())
    display.delete(0,END)
def sub_btn():
    global first_number
    global math
    math = "sub"
    first_number=int(display.get())
    display.delete(0,END)
def mul_btn():
    global first_number
    global math
    math = "mul"
    first_number=int(display.get())
    display.delete(0,END)
def div_btn():
    global first_number
    global math
    math = "div"
    first_number=int(display.get())
    display.delete(0,END)


def equal_btn():
    second_number = display.get()
    display.delete(0,END)

    if math=="add":
        display.insert(0, first_number+int(second_number))

    if math=="sub":
        display.insert(0, first_number-int(second_number))

    if math=="mul":
        display.insert(0, first_number*int(second_number))

    if math=="div":
        display.insert(0, first_number/int(second_number))


# button define
button7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))

button4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))

button1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))

button0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_dot = Button(window, text=".", padx=41, pady=20, command=lambda: button_click())

button_add = Button(window, text="+", padx=39, pady=20, command=add_btn)
button_sub = Button(window, text="-", padx=40, pady=20, command=sub_btn)
button_mul = Button(window, text="X", padx=40, pady=20, command=mul_btn)
button_div = Button(window, text="/", padx=40, pady=20, command=div_btn)

button_clear = Button(window, text="C", padx=40, pady=20, command=clear_btn)

button_equal = Button(window, text="=", padx=184, pady=20, command=equal_btn)

# adding buttons to the screen

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)

button_add.grid(row=4, column=2)
button_sub.grid(row=4, column=4)
button_mul.grid(row=3, column=4)
button_div.grid(row=2, column=4)

button_clear.grid(row=1, column=4)

button_equal.grid(row=5, column=0, columnspan=5)

window.mainloop()
