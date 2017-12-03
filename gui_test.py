#!/usr/bin/env python3

from tkinter import *

root = Tk()

Label(root, text="Renamer App", font=("Times", 35), width=20, anchor=W, justify=LEFT).grid(row=0, columnspan=3)

en = Entry(root, width=60)
en.grid(row=1, columnspan=3)
en.focus_set()

Button(root, text="Show Files", width=20, command="ls").grid(row=2, column=0)
Button(root, text="Count of Files", width=20, command="count").grid(row=3, column=0)
Button(root, text="Backup Files", width=20, command="backup").grid(row=4, column=0)
Button(root, text="Missing Extensions", width=20, command="missing").grid(row=5, column=0)
Button(root, text="Correct Extensions", width=20, command="correct").grid(row=2, column=1)
Button(root, text="Webp Convert", width=20, command="webpconv").grid(row=3, column=1)
Button(root, text="Replace Colon", width=20, command="colonrep").grid(row=4, column=1)
Button(root, text="Verify Files", width=20, command="verify").grid(row=5, column=1)
Button(root, text="Delete Backups", width=20, command="delete").grid(row=2, column=2)
Button(root, text="Find Duplicate", width=20, command="duplicate").grid(row=3, column=2)
Button(root, text="Find Similar Images", width=20, command="similar").grid(row=4, column=2)
Button(root, text="Show Stats", width=20, command="stats").grid(row=5, column=2)
Button(root, text="Top 10 Files", width=20, command="top").grid(row=2, column=3)
Button(root, text="Huge PNG Convertor", width=20, command="hugepng").grid(row=4, column=3)
Button(root, text="Clear Log Output", width=20, command="clear").grid(row=3, column=3)
Button(root, text="Exit", width=20, command="exit").grid(row=5, column=3)

listbox = Listbox(root, height=30, width=140)
listbox.xview_scroll(3, "pages")
listbox.yview_scroll(3, "pages")
listbox.grid(row=7, columnspan=6)

listbox.insert(END, "Log Output: ")

root.geometry("1000x700")
root.mainloop()
