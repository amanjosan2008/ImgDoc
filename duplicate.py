import os
import sys
from itertools import islice
from hashlib import md5

dir = sys.argv[1]

def fullpath(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield (os.path.join(path, file))

import collections

def hashfile():
    #validate()
    x = {}
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
    print(x)

    for k,v in x.items():
        print(k,v)

hashfile()
