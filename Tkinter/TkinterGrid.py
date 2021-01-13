from tkinter import * #Importing tkinter

root = Tk() #Creating main root widget

#Creating a label widget
mylabel1 = Label(root, text = "Hello World !")
mylabel2 = Label(root, text = "My name is Abhishek")
#Putting on to the screen
mylabel1.grid(row = 0, column = 0)
mylabel2.grid(row = 1, column = 0)

#Program Loop
root.mainloop()
