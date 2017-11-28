from tkinter import *

root = Tk()

Label(root, text="Renamer App", width=80, anchor=W, justify=LEFT).grid(row=0, column=0)

en = Entry(root, width=30)
en.focus_set()
en.grid(row=1, column=0)

Button(root, text="ls", width=20, command="ls").grid(row=2, column=0)
Button(root, text="Count", width=20, command="count").grid(row=3, column=0)
Button(root, text="Backup Files", width=20, command="backup").grid(row=4, column=0)
Button(root, text="Missing Extensions", width=20, command="missing").grid(row=5, column=0)
Button(root, text="Correct Extensions", width=20, command="correct").grid(row=6, column=0)
Button(root, text="Webp Convert", width=20, command="webpconv").grid(row=7, column=0)
Button(root, text="Replace Colon", width=20, command="colonrep").grid(row=8, column=0)
Button(root, text="Verify Files", width=20, command="verify").grid(row=2, column=1)
Button(root, text="Delete Backups", width=20, command="delete").grid(row=3, column=1)
Button(root, text="Find Duplicate", width=20, command="duplicate").grid(row=4, column=1)
Button(root, text="Find Similar Images", width=20, command="similar").grid(row=5, column=1)
Button(root, text="Stats", width=20, command="stats").grid(row=6, column=1)
Button(root, text="Exit App", width=20, command="exit").grid(row=7, column=1)

root.geometry("800x400")
root.mainloop()
