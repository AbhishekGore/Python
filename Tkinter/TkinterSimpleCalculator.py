#Importing tkinter
from tkinter import * 
#Creating main root widget
root = Tk()
root.title("Simple Calculator")
#Functions

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
    return

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global  f_num
    global  math
    math = "add"
    f_num = int(first_number)
    e.delete(0,END)
    
def button_sub():
    first_number=e.get()
    global  f_num
    global  math
    math = "sub"
    f_num = int(first_number)
    e.delete(0,END)

def button_mul():
    first_number=e.get()
    global  f_num
    global  math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0,END)

def button_divid():
    first_number=e.get()
    global  f_num
    global  math
    math = "divide"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if  math =="add":
        e.insert(0,f_num+int(second_number))

    if math =="sub":
        e.insert(0,f_num - int(second_number))
        
    if math =="multiply":
        e.insert(0,f_num * int(second_number))
        
    if math =="divide":
        e.insert(0,f_num / int(second_number))
#Entry widget
e = Entry (root, width = 35, borderwidth = 5)
e.grid(row=0, column=0, columnspan=3, padx = 10, pady = 10)
button1 = Button(root, text = "1",padx=40,pady=20,command=lambda: button_click(1))
button2 = Button(root, text = "2",padx=40,pady=20,command= lambda: button_click(2))
button3 = Button(root, text = "3",padx=40,pady=20,command= lambda: button_click(3))
button4 = Button(root, text = "4",padx=40,pady=20,command= lambda: button_click(4))
button5 = Button(root, text = "5",padx=40,pady=20,command= lambda: button_click(5))
button6 = Button(root, text = "6",padx=40,pady=20,command= lambda: button_click(6))
button7 = Button(root, text = "7",padx=40,pady=20,command= lambda: button_click(7))
button8 = Button(root, text = "8",padx=40,pady=20,command= lambda: button_click(8))
button9 = Button(root, text = "9",padx=40,pady=20,command= lambda: button_click(9))
button0 = Button(root, text = "0",padx=40,pady=20,command= lambda: button_click(0))
buttonadd = Button(root, text = "+",padx=40,pady=20,command= button_add)
buttonsubtract = Button(root, text = "-",padx=40,pady=20,command= button_sub)
buttonmultiply = Button(root, text = "*",padx=40,pady=20,command= button_mul)
buttondivide = Button(root, text = "/",padx=40,pady=20,command= button_divid)
buttonequal= Button(root, text = "=",padx=40,pady=20,command= button_equal)
buttonclear =  Button(root,text="Clear",padx=40,pady=20,command= button_clear)

button1.grid(row= 3,column=0)
button2.grid(row= 3,column=1)
button3.grid(row= 3,column=2)

button4.grid(row=2 ,column=0)
button5.grid(row= 2,column=1)
button6.grid(row= 2,column=2)

button7.grid(row=1 ,column=0)
button8.grid(row= 1,column=1)
button9.grid(row= 1,column=2)

button0.grid(row= 4,column=0)
buttonadd.grid(row=4,column=1)
buttonsubtract.grid(row=4,column =2)

buttonmultiply.grid(row=5,column=0)
buttondivide.grid(row=5,column=1)
buttonequal.grid(row=5,column=2)

buttonclear.grid(row=6,column=0,columnspan =3)

