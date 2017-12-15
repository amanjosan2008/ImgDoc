from tkinter import *
from tkinter import filedialog
import sys, glob, os, re
import tarfile
import imghdr, shutil
import subprocess
from pathlib import Path
import collections
#from collections import Counter
from PIL import Image
import PIL
from itertools import islice
from hashlib import md5
import imagehash

dir = "D:\Files\Claims\Mediassit\Test"
#dir = "/home/aman/Desktop/test"

def fullpath():
        for root,dire,fname in os.walk(dir):
            for file in fname:
                yield (os.path.join(root, file))

def similar():
    #if validate():
        x,y,z,a = [],[],[],1
        for file in fullpath():
            try:
                hash = imagehash.whash(Image.open(file))
                x.append(file)
                y.append(hash)
            except OSError:
                pass
        c = [item for item, count in collections.Counter(y).items() if count > 1]
        for i in range(len(c)):
            for j in range(i+1, len(c)):
                    if abs(c[i] - c[j]) < 8:
                        z.append(c[i])
        for i in range(len(z)):
            try:
                c.remove(z[i])
            except:
                pass
        for i in range(len(c)):
            print("Duplicate set:", a)
            a += 1
            for j in range(len(y)):
                if c[i]-y[j] < 8:
                    print(x[j], " Factor:", c[i]-y[j])
                    #listbox.insert(END, "Dupes: "+ x[j] + " Factor: "+str(y[i]-y[j]))

similar()

#def similar():
#    if validate():
#        x,y = [],[]
#        for file in fullpath():
#            try:
#                hash = imagehash.whash(Image.open(file))
#                x.append(file)
#                y.append(hash)
#            except OSError:
#                pass
#        a = 1
#        b = [item for item, count in collections.Counter(y).items() if count > 1]
#        for i in range(len(b)):
#            listbox.insert(END, "Duplicate set: "+ str(a))
#            for j in range(len(y)):
#                if b[i]-y[j] < 8:
#                    listbox.insert(END, x[j]+ " Factor: "+ str(b[i]-y[j]))
#        listbox.insert(END, "--------------Done Finding Similar Images--------------")
