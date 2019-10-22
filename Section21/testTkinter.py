'''
TKinter Demo
'''

from tkinter import *

window = Tk()

def solveConversions():
    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274
    t1.delete("1.0", END)
    t1.insert(END, grams)
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ounces)

l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=solveConversions)
b1.grid(row=0, column=5)

t1 = Text(window, height=1, width=10)
t1.grid(row=1, column=0)

l2 = Label(window, text="Grams")
l2.grid(row=1, column=1)

t2 = Text(window, height=1, width=10)
t2.grid(row=1, column=2)

l3 = Label(window, text="Pounds")
l3.grid(row=1, column=3)

t3 = Text(window, height=1, width=10)
t3.grid(row=1, column=4)

l4 = Label(window, text="Ounces")
l4.grid(row=1, column=5)

window.mainloop()
