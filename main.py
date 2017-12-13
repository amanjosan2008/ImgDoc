#!/usr/bin/env python3

from tkinter import *
from tkinter import filedialog
import sys, glob, os, re
import tarfile
import imghdr, shutil
import subprocess
from pathlib import Path
#from collections import Counter
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

def ls():
    if validate():
        for file in fullpath():
            name = os.path.relpath(file, en.get())
            listbox.insert(END, name)

def count():
    if validate():
        global leng
        x = []
        for file in fullpath():
            x.append(file)
        leng = len(x)
        listbox.insert(END, "Count: "+str(leng))

def backup():
    if validate():
        try:
            os.mkdir("tmp")
        except Exception:
            pass
        tar = tarfile.open(os.path.join("tmp/" + "backup.tar.gz"), "w:gz")
        wr = open(os.path.join("tmp/" + "file_list.txt"), "w")
        wr.write("List of files:\n\n")
        for name in fullpath():
            wr.write(name + '\n')
            tar.add(name)
        wr.close()
        tar.close()
        listbox.insert(END, "--------------Backup Done-----------------")

def missing():
    if validate():
        for file in fullpath():
            fn, ext = os.path.splitext(file)
            ftype = imghdr.what(file)
            if ftype == None:
                listbox.insert(END, "Unsupported file")
            else:
                newname = file +"."+ ftype
                if not ext:
                    filechk = Path(newname)
                    if filechk.is_file():
                        listbox.insert(END, file+": File already EXISTS, not overwriting: "+str(filechk))
                    else:
                        listbox.insert(END, file+": has no ext, Appending: "+ftype)
                        if write():
                            shutil.move(file, newname)
                else:
                    continue
        listbox.insert(END, "--------------Done adding missing extensions--------------")

def correct():
    if validate():
        for file in fullpath():
            # find the correct extension
            ftype = imghdr.what(file)
            ext = os.path.splitext(file)[1][1:]
            # find files with the (incorrect) extension to rename
            if ext:
                if ftype != ext:
                    if ftype != None:
                        #File type is JPG/JPEG, ignoring
                        if (ftype == "jpeg") & (ext == "jpg"):
                            continue
                        else:
                            filechk = file.replace(ext,ftype)
                            filechk2 = Path(filechk)
                            if filechk2.is_file():
                                listbox.insert(END, file+": File already EXISTS, not overwritting: "+str(filechk2))
                            else:
                                # rename the file
                                listbox.insert(END, file+ext+("=>")+ftype)
                                if write():
                                    shutil.move(file, file.replace(ext,ftype))
                    else:
                        if ext == "png":
                            filechk = file.replace(ext,"jpg")
                            filechk2 = Path(filechk)
                            if filechk2.is_file():
                                listbox.insert(END, file+": File already EXISTS, not overwritting: "+filechk2)
                            else:
                                listbox.insert(END, file+": File type not determined for PNG => "+file.replace(ext,"jpg"))
                                if write():
                                    shutil.move(file, file.replace(ext,"jpg"))
                        else:
                            listbox.insert(END, file+": Could not determine file type.")
                else:
                    # Correct Extension
                    continue
            else:
                listbox.insert(END, file+": No Extension detected, Run Missing Extensions function.")
        listbox.insert(END, "--------------Done correcting extensions--------------")

def webpconv():
    if validate():
        for file in fullpath():
            name, ext = os.path.splitext(file)
            if ext == ".webp":
                fnpng = name + ".jpg"
                fpath = Path(fnpng)
                if fpath.is_file():
                    listbox.insert(END, file+"("+filesize(file)+"MB)"+": File already EXISTS, not overwritting: "+fnpng+"("+filesize(fnpng)+"MB)")
                else:
                    try:
                        if write():
                            im = Image.open(file).convert("RGB")
                            im.save(fnpng, "jpeg")
                            if fpath.is_file():
                                listbox.insert(END, file+"("+filesize(file)+"MB)"+" deleted and Converted file saved as: "+fnpng+"("+filesize(fnpng)+"MB)")
                                os.remove(file)
                            else:
                                listbox.insert(END, file+": Conversion to JPG failed")
                        else:
                            listbox.insert(END, file+"("+filesize(file)+"MB)"+" WILL BE deleted and Converted file TO BE saved as: "+name+".jpg")

                    except OSError as e:
                        listbox.insert(END, file+": Exception occured: "+str(e))
                        pass
                    except:
                        listbox.insert(END, "Exception error occured when processing: "+file)
                        pass
            else:
                #File is not Webp, Skipping
                continue
        listbox.insert(END, "--------------Done Webp Conversion--------------")

def colonrep():
    if validate():
        for file in fullpath():
            if re.search(r':', file):
                filechk = file.replace(":","_")
                filechk2 = Path(filechk)
                if filechk2.is_file():
                    listbox.insert(END, file+": File already EXISTS, not overwriting: "+filechk2)
                else:
                    # rename the file
                    listbox.insert(END, file+(" Colon => ")+file.replace(":","_"))
                    if write():
                        shutil.move(file, file.replace(":","_"))
            else:
                #Colon not found in name
                continue
        listbox.insert(END, "--------------Done Colon Replace with Space--------------")

def verify():
    if validate():
        try:
            listbox.insert(END, "Initial Count: "+str(leng))
            x = []
            for file in fullpath():
                x.append(file)
            leng2 = len(x)
            listbox.insert(END, "Final Count: "+str(leng2))
            if leng == leng2:
                listbox.insert(END, "Operation completed successfully")
            else:
                listbox.insert(END, "Operation failed, some files missing, Restore from backup !!!")
        except NameError:
            listbox.insert(END, "Count function not used before operation, cannot use this feature now")

def delete():
    if validate():
        try:
            shutil.rmtree("tmp")
            listbox.insert(END, "Backup Directory Deleted")
        except:
            listbox.insert(END, "Backup not found")

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
        b = 1
        for i in range(len(x)):
            for j in range(i+1, len(x)):
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

def stats():
    if validate():
        listbox.insert(END, "Directory Stats are below:")
        x = []
        for file in fullpath():
                ext = os.path.splitext(file)[1][1:]
                x.append(ext)
        y = set(x)
        for i in y:
            listbox.insert(END, i+" : "+str(x.count(i)))
        listbox.insert(END, "--------------Done Stats--------------")

def top():
    if validate():
        x = {}
        for file in fullpath():
            filesize = (os.path.getsize(file))
            relfile = os.path.relpath(file, en.get())
            x.update({relfile: filesize})
        # Limit iterations to 10 or less in case lesser no of files
        if (len(x) < 10):
            a = len(x)
        else:
            a = 10
        for i in range(a):
            key, value = max(x.items(), key = lambda p: p[1])
            sizeinmb = (value/1000000)
            sizeflt = "{:.2f}".format(sizeinmb)
            listbox.insert(END, key+" => "+sizeflt+"MB")
            x.pop((max(x, key=x.get)))
        listbox.insert(END, "--------------Done Top 10 Function--------------")

def hugepng():
    if validate():
        x = {}
        for file in fullpath():
            filesz = (os.path.getsize(file))
            name, ext = os.path.splitext(file)
            # search huge PNG Files
            if (ext == ".png")|(ext == ".PNG") & (filesz > 1000000):
                fnpng = name + ".jpg"
                fpath = Path(fnpng)
                if fpath.is_file():
                    listbox.insert(END, file+"("+filesize(file)+"MB)"+ ": File already EXISTS, not overwritting: "+ fnpng+ "("+filesize(fnpng)+"MB)" )
                else:
                    try:
                        if write():
                            im = Image.open(file).convert("RGB")
                            im.save(fnpng, "jpeg")
                            if fpath.is_file():
                                listbox.insert(END, file+"("+filesize(file)+"MB)"+ " deleted and Converted file saved as: "+ fnpng+ "("+filesize(fnpng)+"MB)")
                                os.remove(file)
                            else:
                                listbox.insert(END, file+": Conversion to JPG failed")
                        else:
                            listbox.insert(END, file+"("+filesize(file)+"MB)"+" WILL BE deleted and Converted file TO BE saved as: "+fnpng)
                    except OSError as e:
                        listbox.insert(END, file+": Exception occured: "+str(e))
                        pass
                    except:
                        listbox.insert(END, "Exception error occured when processing: "+file)
                        pass
            else:
                #File is not Huge PNG, Skipping
                continue
        listbox.insert(END, "--------------Done Webp Conversion--------------")

def clear():
    listbox.delete(0, END)

Label(root, text="Extensions Doctor", font=("Times", 35), width=20).grid(row=0, columnspan=6)
en = Entry(root, width=60)
en.grid(row=1, column=0,columnspan=4)
en.focus_set()

Button(root, text="Browse", width=20, command=browse).grid(row=1, column=3)

var = IntVar()
c = Checkbutton(root, text="Write Access", variable=var)
c.grid(row=1, column=4, rowspan=1, columnspan=1)

var2 = IntVar()
d = Checkbutton(root, text="Recursive", variable=var2)
d.grid(row=1, column=5, rowspan=1, columnspan=1)

root.grid_rowconfigure(2, minsize=20)

Button(root, text="Show Files", width=20, command=ls).grid(row=3, column=0)
Button(root, text="Count of Files", width=20, command=count).grid(row=4, column=0)
Button(root, text="Backup Files", width=20, command=backup).grid(row=5, column=0)
Button(root, text="Missing Extensions", width=20, command=missing).grid(row=6, column=0)
Button(root, text="Correct Extensions", width=20, command=correct).grid(row=7, column=0)
Button(root, text="Webp Convert", width=20, command=webpconv).grid(row=8, column=0)
Button(root, text="Replace Colon", width=20, command=colonrep).grid(row=9, column=0)
Button(root, text="Verify Files", width=20, command=verify).grid(row=10, column=0)
Button(root, text="Delete Backups", width=20, command=delete).grid(row=11, column=0)
Button(root, text="Delete Duplicate", width=20, command=duplicate).grid(row=12, column=0)
Button(root, text="Find Similar Images", width=20, command=similar).grid(row=13, column=0)
Button(root, text="Image Search", width=20, command=search).grid(row=14, column=0)
Button(root, text="Show Stats", width=20, command=stats).grid(row=15, column=0)
Button(root, text="Top 10 Files", width=20, command=top).grid(row=16, column=0)
Button(root, text="Huge PNG Convertor", width=20, command=hugepng).grid(row=17, column=0)
Button(root, text="Clear Log Output", width=20, command=clear).grid(row=18, column=0)
Button(root, text="Exit", width=20, command=exit).grid(row=19, column=0)

root.grid_rowconfigure(7, minsize=20)
root.grid_columnconfigure(1, minsize=10)

listbox = Listbox(root, height=30, width=140)
listbox.xview_scroll(3, "pages")
listbox.yview_scroll(3, "pages")
listbox.grid(row=3, column=2, rowspan=20, columnspan=6)

listbox.insert(END, "Ready, Log Output: ")

root.geometry("1400x700")
root.title("File Extensions Doctor")

img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.mainloop()
