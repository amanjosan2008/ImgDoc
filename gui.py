#!/usr/bin/env python3

from tkinter import Tk, Button, Label, Entry
import sys

root = Tk()

def backup():
    print("Backup Files")

def unique():
    print("Unique Extensions")

def correct():
    print("Correct Extensions")

def webpconv():
    print("Webp Convert")

def colonrep():
    print("Replace Colon")

def verify():
    print("Verify Files")

def delete():
    print("Delete Backups")

def exit():
    print("Bye Bye!!")
    sys.exit()

def callback():
    print (h.get())

header = Label(root, text="Renamer App v1.0")
header.pack()

h = Entry(root)
h.pack()
h.focus_set()

input = Button(root, text="get", width=10, command=callback)
input.pack()

a = Button(root, text="Backup Files", command=backup)
a.pack()

b = Button(root, text="Unique Extensions", command=unique)
b.pack()

c = Button(root, text="Correct Extensions", command=correct)
c.pack()

d = Button(root, text="Webp Convert", command=webpconv)
d.pack()

e = Button(root, text="Replace Colon", command=colonrep)
e.pack()

f = Button(root, text="Verify Files", command=verify)
f.pack()

g = Button(root, text="Delete Backups", command=delete)
g.pack()



exit = Button(root, text="Exit App", command=exit)
exit.pack()

root.mainloop()
