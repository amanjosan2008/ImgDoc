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
        # x = filenames, y = ImageHash
        x,y = [],[]
        for file in fullpath():
            try:
                hash = imagehash.whash(Image.open(file))
                x.append(file)
                y.append(hash)
            except OSError:
                pass

        # c = Initially will contain all unique fingerprints
        c = [item for item, count in collections.Counter(y).items() if count > 1]
        print("No of unique hash, c =",len(c))

        # z = Similar ranged fingerprints which should be ignored for grouping
        z = []
        for i in range(len(c)):
            for j in range(i+1, len(c)):
                    if abs(c[i] - c[j]) < 8:
                        z.append(c[i])

        print("Similar Hash, z =", len(z))

        # Remove Similar fingerprints from all fingerprints
        for i in range(len(z)):
            try:
                c.remove(z[i])
            except:
                pass

        print("Unique hash after removal of z, c =", len(c))

        for i in range(len(c)):
            print(c[i])
similar()
