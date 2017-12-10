# Delet 3 files without error
import os
from hashlib import md5

dir = "D:\Files\Claims\Mediassit\Claim 2"

def filesize(file):
    size = os.path.getsize(file)
    sizeinmb = size/1000000
    sizeflt = "{:.2f}".format(sizeinmb)
    return sizeflt

x,y = [],[]
for root,dir,fname in os.walk(dir):
    for fpath in fname:
        file = os.path.join(root, fpath)


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
