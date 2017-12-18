#!/usr/bin/env python3

from tkinter import *
from tkinter import filedialog
import sys, glob, os, re
import tarfile
import imghdr, shutil
import subprocess
from pathlib import Path
from PIL import Image
import PIL
from itertools import islice
from hashlib import md5
import imagehash

root = Tk()

def fullpath():
    if var2.get():
        for root,dir,fname in os.walk(en.get()):
            for file in fname:
                yield (os.path.join(root, file))
    else:
        for file in os.listdir(en.get()):
            if os.path.isfile(os.path.join(en.get(), file)):
                yield (os.path.join(en.get(), file))

def filesize(file):
    size = os.path.getsize(file)
    sizeinmb = size/1000000
    sizeflt = "{:.2f}".format(sizeinmb)
    return sizeflt

def validate():
    if os.path.exists(en.get()):
        return True
    else:
        listbox.insert(END, "Incorrect or No Path Entered")
        return False

def browse():
    currdir = os.getcwd()
    dir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    en.delete(0,END)
    en.insert(0,dir)

def write():
    if var.get():
        return True
    else:
        listbox.insert(END, "Write Access not enabled")
        return False

def duplicate():
    if validate():
        x,y = [],[]
        for file in fullpath():
            afile = open(file, 'rb')
            hasher = md5()
            buf = afile.read(65536)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(65536)
            afile.close()
            hash = hasher.hexdigest()
            x.append(hash)
            y.append(file)
        a = len(x)
        b = 1
        for i in range(a):
            for j in range(i+1, a):
                if x[i] == x[j]:
                    listbox.insert(END, "Duplicate Set"+str(b)+":")
                    listbox.insert(END, y[i], y[j])
                    b += 1
                    if write():
                        try:
                            os.remove(y[j])
                            listbox.insert(END, "Duplicate file deleted: "+y[j])
                        except FileNotFoundError:
                            listbox.insert(END, "File already deleted: "+y[j])
                            pass
        listbox.insert(END, "--------------Done Finding Duplicates--------------")

def similar():
    if validate():
        x,y = [],[]
        for file in fullpath():
            try:
                hash = imagehash.whash(Image.open(file))
                x.append(file)
                y.append(hash)
                for i in range(len(x)):
                    for j in range(i+1, len(x)):
                        if y[i]-y[j] < 8:
                            listbox.insert(END, "Dupes: "+ x[i]+"  "+ x[j]+ " Factor: "+str(y[i]-y[j]))
            except OSError:
                pass
        listbox.insert(END, "--------------Done Finding Similar Images--------------")

def search():
    if validate():
        currdir = os.getcwd()
        img = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select an image')
        hash1 = imagehash.whash(PIL.Image.open(img))
        x,y = [],[]
        for file in fullpath():
            hash = imagehash.whash(PIL.Image.open(file))
            x.append(file)
            y.append(hash)
        for i in range(len(x)):
            if not (img == x[i]):
                if y[i]-hash1 < 8:
                    listbox.insert(END, x[i]+" Factor: "+str(y[i]-hash1))
        listbox.insert(END, "--------------Done Similar Function--------------")

Label(root, text="Extensions Doctor", font=("Times", 35), width=20).grid(row=0, columnspan=6)

en = Entry(root, width=60)
en.grid(row=1, column=1,columnspan=3)
en.focus_set()

Button(root, text="Browse", width=20, command=browse).grid(row=1, column=5)

var = IntVar()
c = Checkbutton(root, text="Write Access", variable=var)
c.grid(row=1, column=6, rowspan=1, columnspan=1)

var2 = IntVar()
d = Checkbutton(root, text="Recursive", variable=var2)
d.grid(row=1, column=7, rowspan=1, columnspan=1)

root.grid_rowconfigure(2, minsize=20)

Button(root, text="Delete Duplicate", width=20, command=duplicate).grid(row=3, column=0)
Button(root, text="Find Similar Images", width=20, command=similar).grid(row=4, column=0)
Button(root, text="Image Search", width=20, command=search).grid(row=5, column=0)
Button(root, text="Exit", width=20, command=exit).grid(row=6, column=0)

#root.grid_rowconfigure(7, minsize=20)
#root.grid_columnconfigure(1, minsize=10)

listbox = Listbox(root, height=30, width=140)
listbox.xview_scroll(3, "pages")
listbox.yview_scroll(3, "pages")
listbox.grid(row=3, column=2, rowspan=20, columnspan=6)

listbox.insert(END, "Ready, Log Output: ")

root.geometry("1400x700")
root.title("Duplicate Image Remover")

img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.mainloop()
