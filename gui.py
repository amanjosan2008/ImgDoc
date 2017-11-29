#!/usr/bin/env python3

from tkinter import *
import sys, glob, os, re
import tarfile
import imghdr, shutil
import subprocess
from pathlib import Path
from collections import Counter

root = Tk()

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def ls():
    for file in files(en.get()):
        listbox.insert(END, file)

def count():
    global leng
    leng = len([name for name in os.listdir(en.get()) if os.path.isfile(os.path.join(en.get(), name))])
    listbox.insert(END, "Count: "+str(leng))

def backup():
    try:
        os.mkdir("tmp")
    except Exception:
        pass
    tar = tarfile.open(os.path.join("tmp/" + "backup.tar.gz"), "w:gz")
    wr = open(os.path.join("tmp/" + "file_list.txt"), "w")
    wr.write("List of files:\n\n")
    for name in glob.glob(os.path.join(en.get(), '*')):
        wr.write(name + '\n')
        tar.add(name)
    wr.close()
    tar.close()
    listbox.insert(END, "--------------Backup Done-----------------")

def missing():
    for rootdir, dirs, files in os.walk(en.get()):
        for name in files:
            file = rootdir +"/"+ name
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
                        shutil.move(file, newname)
                        listbox.insert(END, file+": has no ext, Appending: "+ftype)
                else:
                    continue
    listbox.insert(END, "--------------Done adding missing extensions--------------")

def correct():
    for rootdir, dirs, files in os.walk(en.get()):
        for name in files:
            file = rootdir+"/"+name
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
                                listbox.insert(END, file+": File already EXISTS, not overwritting: "+filechk2)
                            else:
                                # rename the file
                                shutil.move(file, file.replace(ext,ftype))
                                listbox.insert(END, file+ext+("=>")+ftype)
                    else:
                        if ext == "png":
                            filechk = file.replace(ext,"jpg")
                            filechk2 = Path(filechk)
                            if filechk2.is_file():
                                listbox.insert(END, file+": File already EXISTS, not overwritting: "+filechk2)
                            else:
                                shutil.move(file, file.replace(ext,"jpg"))
                                listbox.insert(END, file+": File type not determined for PNG => "+file.replace(ext,"jpg"))
                        else:
                            listbox.insert(END, file+": Could not determine file type.")
                else:
                    # Correct Extension
                    continue
            else:
                listbox.insert(END, file+": No Extension detected, Run Missing Extensions function.")
    listbox.insert(END, "--------------Done correcting extensions--------------")

def webpconv():
    for rootdir, dirs, files in os.walk(en.get()):
        for name in files:
            file = rootdir + "/" + name

            fn, ext = os.path.splitext(file)
            if ext == ".webp":
                fnpng = fn + ".png"
                fpath = Path(fnpng)
                if fpath.is_file():
                    listbox.insert(END, file+": File already EXISTS, not overwritting: "+fnpng)
                else:
                    conv = subprocess.Popen(["dwebp", file, "-o", fnpng], stdout=subprocess.PIPE)
                    output, err = conv.communicate()
                    rmfile = subprocess.Popen(["rm", file], stdout=subprocess.PIPE)
                    output2, err2 = rmfile.communicate()
                    listbox.insert(END, file+" Some Webp conv output, Need to create function")
            else:
                #File is not Webp, Skipping
                continue
    listbox.insert(END, "--------------Done Webp Conversion--------------")

def colonrep():
    for rootdir, dirs, files in os.walk(en.get()):
        for name in files:
            file = rootdir + "/" + name
            if re.search(r':', file):
                filechk = file.replace(":","_")
                filechk2 = Path(filechk)
                if filechk2.is_file():
                    listbox.insert(END, file+": File already EXISTS, not overwriting: "+filechk2)
                else:
                    # rename the file
                    shutil.move(file, file.replace(":","_"))
                    listbox.insert(END, file+(" Colon => ")+file.replace(":","_"))
            else:
                #Colon not found in name
                continue
    listbox.insert(END, "--------------Done Colon Replace with Space--------------")

def verify():
    listbox.insert(END, "Initial Count: "+str(leng))
    leng2 = len([name for name in os.listdir(en.get()) if os.path.isfile(os.path.join(en.get(), name))])
    listbox.insert(END, "Final Count: "+str(leng2))
    if leng == leng2:
        listbox.insert(END, "Operation completed successfully")
    else:
        listbox.insert(END, "Operation failed, some files missing, Restore from backup !!!")

def delete():
    try:
        shutil.rmtree("tmp")
        listbox.insert(END, "Backup Directory Deleted")
    except:
        listbox.insert(END, "Backup not found")

def duplicate():
    listbox.insert(END, "duplicate Function Under Construction")
def similar():
    listbox.insert(END, "similar Function Under Construction")

def stats():
    x = []
    for file in files(en.get()):
        ext = os.path.splitext(file)[1][1:]
        x.append(ext)
        count = Counter(x)
    for ext, count in count.most_common(10):
        listbox.insert(END, ("{0}: {1}".format(ext, count)))
    listbox.insert(END, "Done Stats")

def top():
    listbox.insert(END, "Top 10 Function Under Construction")

def clear():
    listbox.delete(0, END)

Label(root, text="Renamer App", font=("Times", 35), width=20, anchor=W, justify=LEFT).grid(row=0, columnspan=3)

en = Entry(root, width=60)
en.grid(row=1, columnspan=3)
en.focus_set()

Button(root, text="Show Files", width=20, command=ls).grid(row=2, column=0)
Button(root, text="Count of Files", width=20, command=count).grid(row=3, column=0)
Button(root, text="Backup Files", width=20, command=backup).grid(row=4, column=0)
Button(root, text="Missing Extensions", width=20, command=missing).grid(row=5, column=0)
Button(root, text="Correct Extensions", width=20, command=correct).grid(row=2, column=1)
Button(root, text="Webp Convert", width=20, command=webpconv).grid(row=3, column=1)
Button(root, text="Replace Colon", width=20, command=colonrep).grid(row=4, column=1)
Button(root, text="Verify Files", width=20, command=verify).grid(row=5, column=1)
Button(root, text="Delete Backups", width=20, command=delete).grid(row=2, column=2)
Button(root, text="Find Duplicate", width=20, command=duplicate).grid(row=3, column=2)
Button(root, text="Find Similar Images", width=20, command=similar).grid(row=4, column=2)
Button(root, text="Show Stats", width=20, command=stats).grid(row=5, column=2)
Button(root, text="Top 10 Files", width=20, command=top).grid(row=2, column=3)
Button(root, text="Clear Log Output", width=20, command=clear).grid(row=3, column=3)
Button(root, text="", width=20, command="").grid(row=4, column=3)
Button(root, text="Exit", width=20, command="exit").grid(row=5, column=3)

listbox = Listbox(root, height=30, width=140)
listbox.xview_scroll(3, "pages")
listbox.yview_scroll(3, "pages")
listbox.grid(row=7, columnspan=6)

listbox.insert(END, "Log Output: ")

root.geometry("900x700")
root.mainloop()
