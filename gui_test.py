#!/usr/bin/env python3

from tkinter import *
from tkinter import filedialog
import os

root = Tk()

def browse():
    currdir = os.getcwd()
    dir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    en.insert(0,dir)

def checked():
    if var.get():
        return True
    else:
        return False

def ls():
    #validate()
    if checked():
        print("Checked")


#def ls():
    #validate()
#    while checked():
#        for file in files():
#            listbox.insert(END, file)

Label(root, text="Renamer App", font=("Times", 35), width=20, anchor=W, justify=LEFT).grid(row=0, columnspan=3)

en = Entry(root, width=60)
en.grid(row=1, column=0,columnspan=4)
en.focus_set()

Button(root, text="Browse", width=20, command=browse).grid(row=1, column=3)

var = IntVar()
c = Checkbutton(root, text="Delete", variable=var)
c.grid(row=1, column=4, rowspan=1, columnspan=1)

var2 = IntVar()
d = Checkbutton(root, text="Recursive", variable=var2)
d.grid(row=1, column=5, rowspan=1, columnspan=1)

root.grid_rowconfigure(2, minsize=20)

Button(root, text="Show Files", width=20, command=ls).grid(row=3, column=0)
Button(root, text="Count of Files", width=20, command="count").grid(row=4, column=0)
Button(root, text="Backup Files", width=20, command="backup").grid(row=5, column=0)
Button(root, text="Missing Extensions", width=20, command="missing").grid(row=6, column=0)
Button(root, text="Correct Extensions", width=20, command="correct").grid(row=7, column=0)
Button(root, text="Webp Convert", width=20, command="webpconv").grid(row=8, column=0)
Button(root, text="Replace Colon", width=20, command="colonrep").grid(row=9, column=0)
Button(root, text="Verify Files", width=20, command="verify").grid(row=10, column=0)
Button(root, text="Delete Backups", width=20, command="delete").grid(row=11, column=0)
Button(root, text="Find Duplicate", width=20, command="duplicate").grid(row=12, column=0)
Button(root, text="Find Similar Images", width=20, command="similar").grid(row=13, column=0)
Button(root, text="Show Stats", width=20, command="stats").grid(row=14, column=0)
Button(root, text="Top 10 Files", width=20, command="top").grid(row=15, column=0)
Button(root, text="Huge PNG Convertor", width=20, command="hugepng").grid(row=16, column=0)
Button(root, text="Clear Log Output", width=20, command="clear").grid(row=17, column=0)
Button(root, text="Exit", width=20, command="exit").grid(row=18, column=0)
Button(root, text="Checked", width=20, command=checked).grid(row=19, column=0)

root.grid_rowconfigure(7, minsize=20)
root.grid_columnconfigure(1, minsize=10)

listbox = Listbox(root, height=30, width=140)
listbox.xview_scroll(3, "pages")
listbox.yview_scroll(3, "pages")
listbox.grid(row=3, column=2, rowspan=20, columnspan=6)

listbox.insert(END, "Log Output: ")

root.geometry("1200x700")
root.mainloop()
