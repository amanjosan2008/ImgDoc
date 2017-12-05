#!/usr/bin/env python3

from tkinter import *
import sys, glob, os, re
import tarfile
import imghdr, shutil
import subprocess
from pathlib import Path
from collections import Counter
from PIL import Image


dir = sys.argv[1]

def fullpath():
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)):
            yield (os.path.join(dir, file))

def filesize(file):
    size = os.path.getsize(file)
    sizeinmb = size/1000000
    sizeflt = "{:.2f}".format(sizeinmb)
    return sizeflt

def hugepng():
    #validate()
    x = {}
    for file in fullpath():
        fsz = (os.path.getsize(file))
        name, ext = os.path.splitext(file)
        # search huge PNG Files
        if (ext == ".png")|(ext == ".PNG") & (fsz > 10):
            fnpng = name + ".jpg"
            fpath = Path(fnpng)
            if fpath.is_file():
                print(file, "(",filesize(file),"MB)", ": File already EXISTS, not overwritting: ", fnpng, "(",filesize(fnpng),"MB)" )
                #listbox.insert(END, file+": File already EXISTS, not overwritting: "+fnpng)
            else:
                try:
                    im = Image.open(file).convert("RGB")
                    im.save(name + ".jpg", "jpeg")
                    if fpath.is_file():
                        print(file, "(",filesize(file),"MB)", " deleted and Converted file saved as: ", fnpng, "(",filesize(fnpng),"MB)")
                        os.remove(file)
                        #listbox.insert(END, file+" deleted and Converted file saved as: "+name+".jpg")
                    else:
                        print(file, ": Conversion to JPG failed")
                        #listbox.insert(END, file+": Conversion to JPG failed")
                except OSError as e:
                    print(file, ": Exception occured: ", str(e))
                    #listbox.insert(END, file+": Exception occured: "+str(e))
                    pass
                except:
                    print("Exception error occured when processing: ", file)
                    #listbox.insert(END, "Exception error occured when processing: "+file)
                    pass
        else:
            #File is not Webp, Skipping
            print(file, "Other file or small png")
            continue
    #listbox.insert(END, "--------------Done Webp Conversion--------------")

hugepng()
