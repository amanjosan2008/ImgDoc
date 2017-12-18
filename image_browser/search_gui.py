import PIL
import os, imagehash, sys
from tkinter import *
from tkinter import filedialog

root = Tk()

path = "/home/aman/Desktop/test"

currdir = os.getcwd()
img = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select an image')

hash1 = imagehash.whash(PIL.Image.open(img))

x,y = [],[]
for root,subdir,fname in os.walk(path):
    for fpath in fname:
        file = os.path.join(root, fpath)
        hash = imagehash.whash(PIL.Image.open(file))
        x.append(file)
        y.append(hash)

for i in range(len(x)):
    if not (img == x[i]):
        if y[i]-hash1 < 8:
            print(x[i], "Factor:", str(y[i]-hash1))
