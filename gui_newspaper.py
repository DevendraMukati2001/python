from tkinter import *

root = Tk()
root.title("dancing_chairs")
root.geometry("650x700")
root.minsize(650,700)
root.configure(bg="#D2B48C")#bg color whole window
header_label = Label(text="****** SPECIAL MEMEORIAL EDITION ******",bg="#D2B48C")
header_label.pack(anchor="n",fill=X)

header_label1 = Label(text="The National News",font = "timesnewroman 50",bg="#D2B48C")
header_label1.pack(fill=X)

line_label = Label(text="---------------------------------------------------------------------------------------------------------------------------------",bg="#D2B48C")
line_label.pack(fill=X)
text_in = Label(root,text=" VOL-XIV-NE 1230\t\t\t\tTUESDAY,NOVEMBER 8,1864\t\t\tTPRICE TEN CENTS",bg="#D2B48C")
text_in.pack(anchor="nw",fill=X)
line_label1 = Label(text="---------------------------------------------------------------------------------------------------------------------------------",bg="#D2B48C")
line_label1.pack(fill=X)

main_heading = Label(text="LINCOLN WON",font="Ariel 50 bold",bg="#D2B48C")
main_heading.pack(fill=X)
s_line = Label(text="O------------------------------------------------O",bg="#D2B48C")
s_line.pack(fill=X,anchor="n")
text_in1 = Label(text="ELECTON MAP REPRESENTS RESULTS",font="comicsansms 20 italic",bg="#D2B48C")
text_in1.pack(fill=X)
s_line1 = Label(text="O------------------------------------------------O",bg="#D2B48C")
s_line1.pack(fill=X,anchor="n")

text = Label(text="Presidential Election In Which Abraham Lincoln Won Beating Out George McClellan",bg="#D2B48C",font="arial 10 bold")
text.pack(fill=X)

photo = PhotoImage(file="1.png")
label1 = Label(image=photo,bg="#D2B48C")
label1.pack(fill=X,anchor="nw")#anchor function disable ho ja rha fill use krte he
text1 = Label(text="\nLencho was a dedicated farmer\n He was expecting a decent harvest\n However, to his grief, a hail storm came and destroyed his harvest completely\n",bg="#D2B48C")
text1.pack(fill=X)

line_label2 = Label(text="---------------------------------------------------------------------------------------------------------------------------------",bg="#D2B48C")
line_label2.pack(fill=X)

root.mainloop()