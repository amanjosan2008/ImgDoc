import os
import sys
import itertools
from hashlib import md5
from itertools import chain

dir = sys.argv[1]

def fullpath(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield (os.path.join(path, file))

def hashfile():
    #validate()
    x = {}
    y = {}
    #for file in fullpath(en.get()):
    for file in fullpath(dir):
        afile = open(file, 'rb')
        hasher = md5()
        buf = afile.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(65536)
        afile.close()
        hash = hasher.hexdigest()
        x.update({file: hash})
    for key, value in x.items():
        y.setdefault(value, set()).add(key)
    z = [values for key, values in y.items() if len(values) > 1]
    i = 1
    for s in z:
        print("Duplicate Set:",i)
        i += 1
        print ("\n".join(str(x) for x in s))

hashfile()
