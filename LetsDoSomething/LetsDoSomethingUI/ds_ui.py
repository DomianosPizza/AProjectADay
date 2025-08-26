import tkinter as tk
import random


def btnClick_click():
    global x
    print('button was clicked')
    lblInfo.config(text=f'BUTTON HAS BEEN CLICKED:{x} TIMES')
    x += 1


# This is purely for the UI box
form = tk.Tk()
form.title("Let's Do Something!")
form.geometry('500x500')
form.resizable(False, False)

# Content of UI
lblMainTitle = tk.Label(form, text="Let's Do Something!")
lblMainTitle.pack()

lblInfo = tk.Label(form, text="Text Output")
lblInfo.pack()

btnclick = tk.Button(form, text="Click me", command=btnClick_click)
btnclick.pack()

txtEntry = tk.Entry(form)
txtEntry.pack()

form.mainloop()
