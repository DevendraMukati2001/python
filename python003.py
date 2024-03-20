from tkinter import *

riya = Tk()
riya.geometry("400x400")
riya.minsize(500,500)
riya.maxsize(500,500)



#screen
scvalue = StringVar()
scvalue.set("get lost")
screen = Entry(riya,textvar=scvalue,font="comicsans 40 bold")
screen.pack(padx=10,pady=10)

#frame and button

b1 = Button( text ="9", font ="comicsans 40 bold")
b1.pack(side =TOP,anchor="nw",padx = 3 , pady= 30)
b2 = Button( text ="8", font ="comicsans 40 bold")
b2.pack(side = TOP, anchor="nw")
b3 = Button( text ="7", font ="comicsans 40 bold")
b3.pack(side = TOP, anchor="nw")
b4 = Button( text ="6", font ="comicsans 40 bold")
b4.pack(side=LEFT)
b5 = Button( text="5", font ="comicsans 40 bold")
b5.pack(side=BOTTOM)
b6 = Button( text="4", font ="comicsans 40 bold")
b6.pack(side=BOTTOM)
b7 = Button( text="3", font ="comicsans 40 bold")
b7.pack(side=LEFT)





riya.mainloop()