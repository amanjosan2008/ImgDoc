#!/usr/bin/env python3

from tkinter import *
import sys, glob, os, re
import tarfile
import imghdr, shutil
import subprocess
from pathlib import Path

root = Tk()

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def ls():
    for file in files(en.get()):
        Label(root, text=file, width=50, anchor=W, justify=LEFT).pack()

def count():
        leng = len([name for name in os.listdir(en.get()) if os.path.isfile(os.path.join(en.get(), name))])
        Label(root, text="Count: "+str(leng), width=50, anchor=W, justify=LEFT).pack()

def backup():
    tar = tarfile.open("backup.tar.gz", "w:gz")
    wr = open("file_list.txt", "w")
    wr.write("List of files:\n\n")
    for name in glob.glob(os.path.join(en.get(), '*')):
        wr.write(name + '\n')
        tar.add(name)
    wr.close()
    tar.close()
    Label(root, text="Backup Done", width=50, anchor=W, justify=LEFT).pack()

def missing():
    for rootdir, dirs, files in os.walk(en.get()):
        for name in files:
            file = rootdir +"/"+ name
            fn, ext = os.path.splitext(file)
            ftype = imghdr.what(file)
            if ftype == None:
                Label(root, text=file + "Unsupported file", width=50, anchor=W, justify=LEFT).pack()
            else:
                newname = file +"."+ ftype
                if not ext:
                    filechk = Path(newname)
                    if filechk.is_file():
                        Label(root, text=file+": File already EXISTS, not overwriting: "+str(filechk), width=50, anchor=W, justify=LEFT).pack()
                    else:
                        shutil.move(file, newname)
                        Label(root, text=file+": has no ext, Appending: "+ftype, width=50, anchor=W, justify=LEFT).pack()
                else:
                    continue
    Label(root, text="Done adding missing extensions", width=50, anchor=W, justify=LEFT).pack()

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
                                Label(root, text=file+": File already EXISTS, not overwritting: "+filechk2, width=50, anchor=W, justify=LEFT).pack()
                            else:
                                # rename the file
                                shutil.move(file, file.replace(ext,ftype))
                                Label(root, text=file+ext+("=>")+ftype, width=50, anchor=W, justify=LEFT).pack()
                    else:
                        if ext == "png":
                            filechk = file.replace(ext,"jpg")
                            filechk2 = Path(filechk)
                            if filechk2.is_file():
                                Label(root, text=file+": File already EXISTS, not overwritting: "+filechk2, width=50, anchor=W, justify=LEFT).pack()
                            else:
                                shutil.move(file, file.replace(ext,"jpg"))
                                Label(root, text=file+": File type not determined for PNG => "+file.replace(ext,"jpg"), width=50, anchor=W, justify=LEFT).pack()
                        else:
                            Label(root, text=file+": Could not determine file type.", width=50, anchor=W, justify=LEFT).pack()
                else:
                    # Correct Extension
                    continue
            else:
                Label(root, text=file+": No Extension detected, Run Missing Extensions function.", width=50, anchor=W, justify=LEFT).pack()
    Label(root, text="Done correcting extensions", width=50, anchor=W, justify=LEFT).pack()

def webpconv():
    for rootdir, dirs, files in os.walk(en.get()):
        for name in files:
            file = rootdir + "/" + name

            fn, ext = os.path.splitext(file)
            if ext == ".webp":
                fnpng = fn + ".png"
                fpath = Path(fnpng)
                if fpath.is_file():
                    print ()
                    Label(root, text=file+": File already EXISTS, not overwritting: "+fnpng, width=50, anchor=W, justify=LEFT).pack()
                else:
                    conv = subprocess.Popen(["dwebp", file, "-o", fnpng], stdout=subprocess.PIPE)
                    output, err = conv.communicate()
                    rmfile = subprocess.Popen(["rm", file], stdout=subprocess.PIPE)
                    output2, err2 = rmfile.communicate()
                    Label(root, text=file+" Some Webp conv output, Need to create function", width=50, anchor=W, justify=LEFT).pack()
            else:
                continue
                #File is not Webp, Skipping
    Label(root, text="Done Webp Conversion", width=50, anchor=W, justify=LEFT).pack()

def colonrep():
    for rootdir, dirs, files in os.walk(en.get()):
        for name in files:
            file = rootdir + "/" + name
            if re.search(r':', file):
                filechk = file.replace(":","_")
                filechk2 = Path(filechk)
                if filechk2.is_file():
                    Label(root, text=file+": File already EXISTS, not overwriting: "+filechk2, width=50, anchor=W, justify=LEFT).pack()
                else:
                    # rename the file
                    shutil.move(file, file.replace(":","_"))
                    Label(root, text=file+(" Colon => ")+file.replace(":","_"), width=50, anchor=W, justify=LEFT).pack()
            else:
                #Colon not found in name
                continue
    Label(root, text="Done Colon Replace with Space", width=50, anchor=W, justify=LEFT).pack()

def verify():
    Label(root, text="verify Function Under Construction", width=50, anchor=W, justify=LEFT).pack()
def delete():
    Label(root, text="delete Function Under Construction", width=50, anchor=W, justify=LEFT).pack()
def duplicate():
    Label(root, text="duplicate Function Under Construction", width=50, anchor=W, justify=LEFT).pack()
def similar():
    Label(root, text="similar Function Under Construction", width=50, anchor=W, justify=LEFT).pack()
def stats():
    for file in files(en.get()):
        ext = os.path.splitext(file)[1][1:]
        if ext == "jpg":

        if ext == "jpg":

        if ext == "jpg":

        if ext == "jpg":

        if ext == "jpg":

        if ext == "jpg":

        if ext == "jpg":
        Label(root, text=ext, width=50, anchor=W, justify=LEFT).pack()



    Label(root, text="Done Stats", width=50, anchor=W, justify=LEFT).pack()

Label(root, text="Renamer App", font=("Times", 35), width=20, anchor=W, justify=LEFT).pack()

en = Entry(root, width=60)
en.pack()
en.focus_set()

Button(root, text="ls", width=20, command=ls).pack()
Button(root, text="Count", width=20, command=count).pack()
Button(root, text="Backup Files", width=20, command=backup).pack()
Button(root, text="Missing Extensions", width=20, command=missing).pack()
Button(root, text="Correct Extensions", width=20, command=correct).pack()
Button(root, text="Webp Convert", width=20, command=webpconv).pack()
Button(root, text="Replace Colon", width=20, command=colonrep).pack()
Button(root, text="Verify Files", width=20, command=verify).pack()
Button(root, text="Delete Backups", width=20, command=delete).pack()
Button(root, text="Find Duplicate", width=20, command=duplicate).pack()
Button(root, text="Find Similar Images", width=20, command=similar).pack()
Button(root, text="Stats", width=20, command=stats).pack()
Button(root, text="Exit App", width=20, command="exit").pack()

root.geometry("800x800")
root.mainloop()
