import tkinter as tk
import random


def btnClick_indoor():
    experience = ["To the movies", "Bowling", "Bouldering", "Board Games", "Trading Card Games"]
    random.shuffle(experience)
    txtEntry.config(text=f"Let's go {experience[0]}")

def btnClick_outdoor():
    # TO DO
    # Read From a JSON file of list of things to do outdoor/indoor, randomly select from there
    # Take result and search internet for nearby places to do said things
    experience = ["Hike", "Golf", "To The Gun Range", "To The Mall", "To The Beach"]
    random.shuffle(experience)
    txtEntry.config(text=f"Let's go {experience[0]}")

# This is purely for the UI box
form = tk.Tk()
form.title("Let's Do Something!")
form.geometry('500x500')
form.resizable(False, False)

# Content of UI
lblMainTitle = tk.Label(form, text="Let's Do Something!")

btnclick = tk.Button(form, text="Find Indoor Activity", command=btnClick_indoor)
btnclick.place(x=87.5, y=200)


btnclick = tk.Button(form, text="Find Outdoor Activity", command=btnClick_outdoor)
btnclick.place(x=275, y=200)

txtEntry = tk.Label(form, text="")
txtEntry.grid(row=3, column=3)
txtEntry.place(x=175, y=250)

form.mainloop()
