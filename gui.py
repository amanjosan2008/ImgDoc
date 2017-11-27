#!/usr/bin/env python3

from tkinter import *
import sys, glob, os

#try:
#    directory = sys.argv[1]
#except:
#    print("\nException occured: Full Directory path with images not defined.\n")
#    sys.exit()

root = Tk()

def ls():
    for name in glob.glob(os.path.join(en.get(), '*')):
        Label(root, text=name, width=100, anchor=W, justify=LEFT).pack()

def x():
    x = 0
    for name in glob.glob(os.path.join(en.get(), '*')):
        x+=1
    return x

def count():
    Label(root, text="Count: " + str(x()), width=100, anchor=W, justify=LEFT).pack()


def exit():
    print("Application closed by user !!")
    sys.exit()

Label(root, text="Renamer App", font=("Times", 35)).pack()

en = Entry(root, width=30)
en.pack()
en.focus_set()


Button(root, text="ls", width=20, command=ls).pack()
Button(root, text="Count", width=20, command=count).pack()
Button(root, text="Backup Files", width=20, command="backup").pack()
Button(root, text="Unique Extensions", width=20, command="unique").pack()
Button(root, text="Correct Extensions", width=20, command="correct").pack()
Button(root, text="Webp Convert", width=20, command="webpconv").pack()
Button(root, text="Replace Colon", width=20, command="colonrep").pack()
Button(root, text="Verify Files", width=20, command="verify").pack()
Button(root, text="Delete Backups", width=20, command="delete").pack()
Button(root, text="Exit App", width=20, command=exit).pack()

root.geometry("400x600")
root.mainloop()
