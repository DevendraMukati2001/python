import tkinter as tk


root = tk.Tk()
root.title("to_do_list")
root.configure(bg="#D2B48C")

root.geometry("400x500")
root.maxsize(400, 500)
root.minsize(400, 500)
title = tk.Label(text="To-Do list", font="comicsansms 30 bold",bg="#D2B48C")
title.grid(column=1)

title1 = tk.Label(text="your item: ", font="timesroman 10 bold ",bg="#D2B48C")
title1.grid(row=2)
title1 = tk.StringVar()
entry = tk.Entry(root, textvariable=title1)
entry.grid(row=2, column=1)


def add():
    user = entry.get()
    if user:
        lbx.insert(tk.END, user)
        entry.delete(0, tk.END)


lbx = tk.Listbox(root)
lbx.grid(row=3, column=1)

tk.Button(root, text="Add Item", font="italic 8 bold", command=add).grid(row=2, column=2, padx=8)

root.mainloop()
