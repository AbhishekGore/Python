#Importing tkinter
from tkinter import * 
#Creating main root widget
root = Tk() 
#Adding funcitonality to the button
def myclick():
    mylabel = Label(root,text = "Woohooo Button Works!")
    mylabel.pack()
#Creating a button
mybutton = Button(root, text ="Click me", padx=50,pady=60,command = myclick)
#Packing a button
mybutton.pack()
#Program Loop
root.mainloop()
