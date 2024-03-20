from tkinter import *

root = Tk()

#dacha
root.title("three fruits")
root.geometry("2000x1000")
#root.maxsize(800, 600)
root.minsize(800, 600)
root.configure(bg="blue")

#heading
an=Label(root, text="click on fruit to know about its color ; itne bade hogaye ho fir bhi nahi pata", font="Algerian 25 bold", bg="yellow")
an.pack()

#functions
def createNewWindow():
    newWindow = Toplevel()
    newWindow.title("info about apple")
    newWindow.geometry("800x600")
    newWindow.maxsize(800, 600)
    newWindow.minsize(800, 600)
    newWindow.configure(bg="red")
    bn = Label(newWindow, text="APPLE", font="Algerian 50 bold", bg="yellow")
    bn.pack()
    zn = Label(newWindow,text="i am red in color",font="Algerian 50 bold")
    zn.pack(side=LEFT)

def createNewWindow1():
    newWindow1 = Toplevel()
    newWindow1.title("info about banana")
    newWindow1.geometry("800x600")
    newWindow1.maxsize(800, 600)
    newWindow1.minsize(800, 600)
    newWindow1.configure(bg="yellow")
    cn = Label(newWindow1, text="BANANA", font="Algerian 50 bold", bg="purple")
    cn.pack()
    zn = Label(newWindow1,text="i am yellow in color",font="Algerian 50 bold")
    zn.pack(side=LEFT)

def createNewWindow2():
    newWindow2 = Toplevel()
    newWindow2.title("info about grapes")
    newWindow2.geometry("800x600")
    newWindow2.maxsize(800, 600)
    newWindow2.minsize(800, 600)
    newWindow2.configure(bg="green")
    dn = Label(newWindow2, text="GRAPES", font="Algerian 50 bold", bg="yellow")
    dn.pack()
    zn = Label(newWindow2,text="i am green in color",font="Algerian 50 bold")
    zn.pack(side=LEFT)

def newWindow3():
    newWindow3 = Toplevel()
    newWindow3.title("info about grapes")
    newWindow3.geometry("800x600")
    newWindow3.maxsize(800, 600)
    newWindow3.minsize(800, 600)
    newWindow3.configure(bg="orange")
    dn = Label(newWindow3, text="MANGO", font="Algerian 50 bold", bg="yellow")
    dn.pack()
    zn = Label(newWindow3,text="i am yellow in color",font="Algerian 50 bold")
    zn.pack(side=LEFT)


#BUTTONS
b1=Button(text="APPLE", font="Algerian 25 bold", height = 1, width = 20, command=createNewWindow)
b1.pack(side=TOP,padx=10,pady=52)
b2=Button(text="BANANA",font="Algerian 25 bold", height = 1, width = 20, command=createNewWindow1)
b2.pack(side=TOP,padx=10,pady=52)
b3=Button(text="GRAPES",font="Algerian 25 bold", height = 1, width = 20 ,command=createNewWindow2)
b3.pack(side=TOP,padx=10,pady=52)
b4=Button(text="MANGO", font="Algerian 25 bold" ,height = 1, width = 20, command=newWindow3)
b4.pack()

root.mainloop()
