from tkinter import *
import tkinter as tk

# create a GUI window
def from_kg():
    #convet kg to gram
    gram = float(e2_value.get()) * 1000

    #convert kg to pound
    pound = float(e2_value.get()) * 2.20462
    #convert kg to ounce
    ounce = float(e2_value.get()) * 35.274
    # enter the converted weight to
    #the text widget
    t1.delete("1.0", END)
    t1.insert(END, gram)

    t2.delete("1.0", END)
    t2.insert(END, pound)

    t3.delete("1.0", END)
    t3.insert(END, ounce)

    #create the label widgets
    el = Label(window, text="Enter the weight in kg")
    e2_value = StringVar()
    e2 = Entry(window, textvariable=e2_value)
    e3 = Label(window, text='Gram')
    e4 = Label(window, text='pounds')
    e5 = Label(window, text='ounce')

    #create the txt widgets
    t1 = Text(window, hieght=1, width=20)
    t2 = Text(window, hieght=1, width=20)
    t3 = Text(window, hieght=1, width=20)

    #create the button widget
    b1 = Button(window, text='convert',command=from_kg)
    #grid method is used for placing the widgets at respective positions
    # in table like structure
    e1.grid(row=0, column=0)
    e2.grid(row=0, column=1)
    e3.grid(row=1, column=0)
    e4.grid(row=1, column=1)
    e5.grid(row=1, column=2)
    t1.grid(row=2, column=0)
    t2.grid(row=2, column=1)
    t3.grid(row=2, column=2)
    b1.grid(row=0, column=2)

    #start the GUI
    window.mainloop()










