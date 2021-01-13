#Importing tkinter
from tkinter import * 
#Creating main root widget
root = Tk()
#Entry widget
e = Entry (root, width = 50, borderwidth = 5)
e.pack()
e.insert(0,"Enter file path here") #Default line
#e.get()  Captures content inputed by user

#Adding funcitonality to the button
def myclick():
    
    mylabel = Label(root, text = "Hello "  + e.get())
    mylabel.pack()

#Creating a button
mybutton = Button(root, text ="Press here to execute", padx=25,pady=25,command = myclick)

#Packing a button
mybutton.pack()

#Program Loop
root.mainloop()
