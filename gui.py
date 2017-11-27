#!/usr/bin/env python3

from tkinter import *
import sys, glob, os, re
import tarfile
import imghdr, shutil
import subprocess
from pathlib import Path

root = Tk()

def ls():
    for name in glob.glob(os.path.join(en.get(), '*')):
        Label(root, text=name, width=100, anchor=W, justify=LEFT).pack()

def count():
        x = 0
        for name in glob.glob(os.path.join(en.get(), '*')):
            x+=1
        Label(root, text="Count: " + str(x), width=100, anchor=W, justify=LEFT).pack()

def backup():
    tar = tarfile.open("backup.tar.gz", "w:gz")
    wr = open("file_list.txt", "w")
    wr.write("List of files:\n\n")
    for name in glob.glob(os.path.join(en.get(), '*')):
        wr.write(name + '\n')
        tar.add(name)
    wr.close()
    tar.close()
    Label(root, text="Backup Done", width=100, anchor=W, justify=LEFT).pack()

def missing():
    for root1, dirs, files in os.walk(en.get()):
        for name in files:
            file = root1 +"/"+ name

            fn, ext = os.path.splitext(file)
            ftype = imghdr.what(file)

            if ftype == None:
                Label(root, text=file + "Unsupported file", width=100, anchor=W, justify=LEFT).pack()
            else:
                newname = file +"."+ ftype
                if not ext:
                    filechk = Path(newname)
                    if filechk.is_file():
                        Label(root, text=str(filechk) + " File already EXISTS, not overwriting", width=100, anchor=W, justify=LEFT).pack()
                    else:
                        shutil.move(file, newname)
                        Label(root, text=file + " has no ext, Appending: " + ftype, width=100, anchor=W, justify=LEFT).pack()
                else:
                    continue
    Label(root, text="Done adding missing extensions", width=100, anchor=W, justify=LEFT).pack()

def verify():
    Label(root, text="Function Under Construction", width=100, anchor=W, justify=LEFT).pack()

def exit():
    print("Application closed by user !!")
    sys.exit()

Label(root, text="Renamer App", font=("Times", 35)).pack()

en = Entry(root, width=30)
en.pack()
en.focus_set()

Button(root, text="ls", width=20, command=ls).pack()
Button(root, text="Count", width=20, command=count).pack()
Button(root, text="Backup Files", width=20, command=backup).pack()
Button(root, text="Missing Extensions", width=20, command=missing).pack()
Button(root, text="Correct Extensions", width=20, command="correct").pack()
Button(root, text="Webp Convert", width=20, command="webpconv").pack()
Button(root, text="Replace Colon", width=20, command="colonrep").pack()
Button(root, text="Verify Files", width=20, command=verify).pack()
Button(root, text="Delete Backups", width=20, command="delete").pack()
Button(root, text="Exit App", width=20, command=exit).pack()

root.geometry("400x600")
root.mainloop()
