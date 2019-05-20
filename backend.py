from tkinter import *
def price(tradeEntry,output):
    id = tradeEntry.get()
    output.delete(1.0,END)
    if id is "":
        output.insert(END,"Please enter an ID")
    else:
        output.insert(END,"NPV = "+id)