from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg

root = Tk() # tk naam ka object banate hhai

root.geometry("1000x1000") #geometry
#root.minsize(300,300)
#root.maxsize(600,600)

#labels - label vo hota hai jiske saath user interact nhi karta hai
"""label1 = Label(text="this is a label")
label2 = Label(text="i am label")
label1.pack()
label2.pack()"""

#label adding png images
"""photo = PhotoImage(file="1.png")
label1 = Label(image=photo)
label1.pack()"""

#label addding jpg images
"""image = Image.open("goku_drawing_by_muhammadaks-d700ey0.jpg")
photo = ImageTk.PhotoImage(image)
label1 = Label(image=photo)
label1.pack()"""

#title
root.title("My GUI summary")

#important label options
"""text = adds the text
bg = background
fg = foreground
font = sets the font
padx = x padding
pady = y padding
relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
"""
"""title_label = Label(text='''Lencho was a dedicated farmer\n He was expecting a decent harvest\n However, to his grief, a hail storm came and destroyed his harvest completely\n Lencho was very sad\n However, he had a strong belief in God\n He was certain that God would help him\n Also, he was an extremely straightforward man\n Although working for a long time on the farm, he knew writing\n Thus, he composed a letter to God\n In the letter, he asked God to send him one hundred pesos\n At that point, he went to the post office and put his letter into the post box\n The postman removed the letter from the letter-box\n He read the address on it and laughed very much\n Also, he rushed to the postmaster and demonstrated to him that strange letter\n Moreover, the postmaster also laughed in the same way when he saw the address of God\n However, on reading the letter, he got very serious\n He lauded this man who had unquestioned faith in God and decided to help him in terms of money\n He asked the employees of the post office to give charity\n Moreover, he gave a part of-of his salary too\n However, they were able to collect only a little more than 50 pesos as requested for by Lencho\n The postmaster put the money in an envelope\n It was addressed to Lencho\n

''',bg="black",fg="white",padx=113,pady=94,font="comicsansma 10 bold",borderwidth=3,relief=SUNKEN)
#anchor
#title_label.pack(anchor="se")
#title_label.pack(side = bottom,anchor = "se")
title_label.pack(side = LEFT, fill = Y)"""

#frames
"""f1 = Frame(root,bg="grey",borderwidth=10,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y,pady=9)#frame ko y mai space de rha
l=Label(f1,text="helllllllllllnoooooooooooooooo")
l.pack(pady=143)
f2 = Frame(root,bg="grey",borderwidth=2,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
l1=Label(f2,text="helllllllllllnoooooooooooooooo",font="helvetica 34 bold")
l1.pack()"""

#buttons

def hello():
    print("here is hell")

"""frame = Frame(root, borderwidth=6 ,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")
b1 = Button(frame,fg="red",text="print now",command=hello)
b1.pack(side=LEFT,padx=10)
b2 = Button(frame,fg="red",text="print now")
b2.pack(side=LEFT,padx=10)
b3 = Button(frame,fg="red",text="print now")
b3.pack(side=LEFT,padx=10)
b4 = Button(frame,fg="red",text="print now")
b4.pack(side=LEFT,padx=10)"""

#grid_layout ->
"""user = Label(text="Username")
password = Label(text="Password")
user.grid()
password.grid(row=1)"""

#variable classes
#booleanVar ,DoubleVar ,IntVar,StringVar

#box baana rhe jisme value likhte
"""uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable=uservalue)
passentry = Entry(root,textvariable=passvalue)

userentry.grid(row=0, column =1)
passentry.grid(row=1, column=1)

def getval():
    print("value of user is",uservalue.get())
    print("value of user is",passvalue.get())"""
#one liner button
#Button(text="submit",command=getval).grid(row=2,column=1)

#example user entry form

"""Label(root,text="WELCOME TO ABC TRAVELS",font="comicsansms 13 bold").grid(row=0,column=1)
name = Label(root,text="Name")
phone = Label(root,text="Phone")
gender = Label(root,text="Gender")
eme = Label(root,text="Emergency Contact")
pay_mode=Label(root,text="Payment Mode")

name.grid(row=1,column=0)
phone.grid(row=2,column=0)
gender.grid(row=3,column=0)
eme.grid(row=4,column=0)
pay_mode.grid(row=5,column=0)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root,textvariable=paymentmodevalue)

nameentry.grid(row=1,column=1)
phoneentry.grid(row=2,column=1)
genderentry.grid(row=3,column=1)
emergencyentry.grid(row=4,column=1)
paymentmodeentry.grid(row=5,column=1)

#checkbox
foodservice = Checkbutton(text="want to prebook your meals",variable=foodservicevalue)
foodservice.grid(row=6,column=1)"""

#opening file
"""def getvals():
    print("submitting form")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}")
    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()},\n")"""

#button
#Button(text="submit to ABC travels",command = getvals).grid(row=7,column=1)

#canvas
"""canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")"""

#widget
"""can_widget = Canvas(root, width=canvas_width,height=canvas_height)
can_widget.pack()"""

#the line goes from point x1, y1, to x2, y2
"""can_widget.create_line(3,2,600,2,fill="red")"""
#topleft and bottomright corner -> coordinate specification
"""can_widget.create_rectangle(3,4,5,6)"""
#text coordinates
"""can_widget.create_text(200,200,text="python")
can_widget.create_oval(300,400,899,400)"""


#handling events
"""widget = Button(root,text="click me please")
widget.pack()
def harry(event):
    print("button was pressed at the location",{event.x},{event.y})
widget.bind("<Button-1>",harry)
widget.bind("<Double-1>",quit)"""

#making newspaper
#reading text from files , opening three files
"""texts = []
photos = []

#full stop ke jagah new line character daldega and new line mai text print karega
def ever_space(text):666y
    new_text = ""
    for char in text:
        if char ==".":
            new_text += ".\n"
        else :
            new_text += char
    return new_text

for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(ever_space(text))

    image = Image.open(f"{i+1}.png")
    #TODO: Resize these images
    image = image.resize((225,225),Image.ANTIALIAS)#blurry effect ko hatane ke leye
    photos.append(ImageTk.PhotoImage(image))

f = Frame(root, width=800, height=70)
Label(f, text="NATIONAL ANIME NEWS",font = "lucida 33 bold").pack()
Label(f, text="23 jan 2023",font = "lucida 13 bold").pack()
f.pack()

for i in range(0,3):
    fi = Frame(root,width=800, height=70)
    Label(fi,text=texts[0]).pack(side="left")
    Label(fi,image=photos[0]).pack(side="right")
    fi.pack(anchor="w")"""

#menus and submenus
def myfun():
    print("i am a function")

# not a drop down menu
"""mymenu = Menu(root)
mymenu.add_command(label="File",command=myfun)
mymenu.add_command(label="Exit",command=quit)
root.config(menu=mymenu)"""

#dropdown menu , message boxes
"""your_menubar = Menu(root)#menu banaya
# menu ke andar menu banana
m1 = Menu(your_menubar, tearoff=0)#tearoff matlab jo menu bar create kraa vo detach nhi hoga
m1.add_command(label = "new project", command=myfun)
m1.add_command(label = "Save as", command=myfun)
m1.add_separator()#line add kardega options ke between mai
m1.add_command(label = "print", command=myfun)
m1.add_command(label = "save", command=myfun)
root.config(menu=your_menubar)
your_menubar.add_cascade(label="File", menu=m1)

m2 = Menu(your_menubar, tearoff=0)#tearoff matlab jo menu bar create kraa vo detach nhi hoga
m2.add_command(label = "cut", command=myfun)
m2.add_command(label = "copy", command=myfun)
m2.add_separator()#line add kardega options ke between mai
m2.add_command(label = "paste", command=myfun)
m2.add_command(label = "print", command=myfun)
root.config(menu=your_menubar)
your_menubar.add_cascade(label="Edit", menu=m2)

def myfun1():
    print("i will help you")
    tmsg.showinfo("Help","i will help you with this GUI")

def rateus():
    value = tmsg.askquestion("que","was your experience good ?")
    #value1 = tmsg.askretrycancel() -> many options available as per requirement
    if value == "yes":
        msg = "great rate us"
    else:
        msg = "tell us what went wrong. we will call you"
    tmsg.showinfo("experience",msg)

m3 = Menu(your_menubar, tearoff=0)#tearoff matlab jo menu bar create kraa vo detach nhi hoga
m3.add_command(label = "Help", command=myfun1)
root.config(menu=your_menubar)
your_menubar.add_cascade(label="Help", menu=m3)

m4 = Menu(your_menubar, tearoff=0)#tearoff matlab jo menu bar create kraa vo detach nhi hoga
m4.add_command(label = "rate", command=rateus)
root.config(menu=your_menubar)
your_menubar.add_cascade(label="rate us", menu=m4)"""

#sliders
"""def getdollar():
    print(f"we have credited {myslider.get()} dollars to your account")
    tmsg.showinfo("help","i will help you")
Label(text="how many dollars you want ?").pack()
myslider = Scale(root,orient=HORIZONTAL,tickinterval=50)#tickinterval -> value likhne ke leye sliders ke neeche 
myslider.set(32)
myslider.pack()
Button(root,text="GET DOLLARS",command=getdollar).pack()"""

#radiobuttons
"""def order():
    tmsg.showinfo("msg",f"we have received your order for {var.get()}")
var = StringVar()
var.set("Radio")#sab aarhe the clicked radio par toh unko hatane ke leye
Label(root,text="what would you like to have ?",font = "lucid 32 bold").pack()
radio = Radiobutton(root,text="dosa",variable = var, value ="dosa").pack(anchor="w")
radio1 = Radiobutton(root,text="idli",variable = var, value ="idli").pack(anchor="w")
Button(text="order now",command=order).pack(anchor="w")"""

#Listbox tutorial
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i = 0
lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "first item of our listbox")

Button(root, text="Add Item", command=add).pack()

#ScrollBar
#for connecting scrollbar to a widget
#1. widget(yscrollcommand = scrollbar.set)
#2. scrollbar.config(command=widget.yview)
"""scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar1 = Scrollbar(root,orient=HORIZONTAL)
scrollbar1.pack(side=BOTTOM,fill=X)"""

"""listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(344):
    listbox.insert(END, f"item{i}")

listbox.pack(fill="both")
scrollbar.config(command=listbox.yview)"""

# simple notepad connections
"""text = Text(root, yscrollcommand = scrollbar.set, xscrollcommand = scrollbar1.set)
text.pack(expand=True,fill=BOTH)
scrollbar.config(command = text.yview)
scrollbar1.config(command = text.xview)"""

#statusbar
"""def upload():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command = upload).pack()"""

root.mainloop()
