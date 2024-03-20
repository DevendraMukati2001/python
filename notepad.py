from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root = Tk()
root.geometry("1000x1000")
root.title("Notepad")


#scrollbars
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar1 = Scrollbar(root,orient=HORIZONTAL)
scrollbar1.pack(side=BOTTOM,fill=X)

# simple notepad connectionst
Textarea = Text(root, yscrollcommand = scrollbar.set, xscrollcommand = scrollbar1.set)
Textarea.pack(expand=True,fill=BOTH)
scrollbar.config(command = Textarea.yview)
scrollbar1.config(command = Textarea.xview)

#commands
def newWindow():
    global new_window
    new_window = Toplevel(root)
    new_window.title("New Window")

    # scrollbars
    scrollbar = Scrollbar(new_window)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar1 = Scrollbar(root, orient=HORIZONTAL)
    scrollbar1.pack(side=BOTTOM, fill=X)

    # simple notepad connections
    Textarea = Text(new_window, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar1.set)
    Textarea.pack(expand=True, fill=BOTH)
    scrollbar.config(command=Textarea.yview)
    scrollbar1.config(command=Textarea.xview)

def open():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        Textarea.delete(1.0, END)
        f = open(file,"r")
        Textarea.insert(1.0, f.read())
        f.close()

#edit command

def Undo():
    Textarea.event_generate(("<<Undo>>"))
def Cut():
    Textarea.event_generate(("<<Cut>>"))
def Copy():
    Textarea.event_generate(("<<Copy>>"))
def Paste():
    Textarea.event_generate(("<<Paste>>"))
def Delete():
    Textarea.event_generate(("<<Cut>>"))

def Search():
    pass
def close():
    root1.destroy()


#menubar
your_menubar = Menu(root)
m1 = Menu(your_menubar, tearoff=0)
m1.add_command(label = "New window",command=newWindow)
m1.add_command(label = "Open",command=open)
m1.add_command(label = "Save")
m1.add_command(label = "Save as")
m1.add_command(label = "Save all")
m1.add_separator()
m1.add_command(label = "Page Setup")
m1.add_command(label = "Print")
m1.add_separator()
m1.add_command(label = "Close Tab")
m1.add_command(label = "Close Window")
m1.add_command(label = "Exit")
root.config(menu=your_menubar)
your_menubar.add_cascade(label="File", menu=m1)

m2 = Menu(your_menubar, tearoff=0)
m2.add_command(label = "Undo",command=Undo)
m2.add_separator()
m2.add_command(label = "Cut",command=Cut)
m2.add_command(label = "Copy",command=Copy)
m2.add_command(label = "Paste",command=Paste)
m2.add_command(label = "Delete",command=Delete)
m2.add_separator()
m2.add_command(label = "Find")
m2.add_command(label = "Find next")
m2.add_command(label = "Find Previous")
m2.add_command(label = "Replace")
m2.add_command(label = "Go to")
m2.add_separator()
m2.add_command(label = "Select all")
m2.add_command(label = "Time/Date")
m2.add_separator()
m2.add_command(label = "Font")
root.config(menu=your_menubar)
your_menubar.add_cascade(label="Edit", menu=m2)

m3 = Menu(your_menubar, tearoff=0)
Zoom = Menu(your_menubar, tearoff=0)
Zoom.add_command(label = "Zoom in")
Zoom.add_command(label = "Zoom out")
Zoom.add_command(label = "Restore Default Zoom")
m3.add_cascade(label="Zoom",menu=Zoom)
m3.add_separator()
m3.add_command(label = "Status Bar")
m3.add_command(label = "Word wrap")
your_menubar.add_cascade(label="View", menu=m3)



root.mainloop()