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

dir = "D:\Files\Claims\Mediassit\Test"

def fullpath():
        for root,dire,fname in os.walk(dir):
            for file in fname:
                yield (os.path.join(root, file))

def similar():
    #if validate():
        x,y,z = [],[],[]
        for file in fullpath():
            try:
                hash = imagehash.whash(Image.open(file))
                x.append(file)
                y.append(hash)
            except OSError:
                pass

        for i in range(len(y)):
            for j in range(i+1, len(y)):
                print(i,j)
                print(y[i], y[j])
                if y[i] == y[j]:
                    z.append(y[i])


        print(len(x), len(y), len(z),z)

        for i in range(len(z)):
            for j in range(len(y)):
                if z[i] == y[j]:
                    if y[i]-y[j] < 8:
                        print(x[j], " Factor: ", y[i]-y[j])
                        #listbox.insert(END, "Dupes: "+ x[j] + " Factor: "+str(y[i]-y[j]))

similar()


#x=['a','b','c','d','e','f','g','h']
#y=[1,2,3,4,5,6,2,4]
#z=[]
#
#for i in range(len(y)):
#    for j in range(i+1, len(y)):
#        if y[i] == y[j]:
#            z.append(y[i])
#print(z)
#
#for i in range(len(z)):
#    for j in range(len(y)):
#        if z[i] == y[j]:
#                print(x[j])
#
