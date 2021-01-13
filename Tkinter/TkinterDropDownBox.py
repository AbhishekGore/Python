from tkinter import *
root = Tk()
root.title("Drop down menu")


clicked = StringVar()
clicked .set("None")
drop = OptionMenu(root,clicked,"None","Fucntion1","Function2")
drop.pack()


def show():
    mylabel = Label(root,text = clicked.get())
    mylabel.pack()

button = Button(root,text="Show Selection",command=show)
button.pack()

