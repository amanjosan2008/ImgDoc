import os
import sys
import itertools
from hashlib import md5

dir = sys.argv[1]

def fullpath(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield (os.path.join(path, file))

def hashfile():
    #validate()
    x = []
    y = []
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
        x.append(file)
        y.append(hash)

    a = len(x)
    b = len(x)-1
    for i in range(a):
        print(i, a, b)
        if (i < b):
            print("True")
            print(y[i])
            print(y[i+1])
            if y[i] == y[i+1]:
                print(i)
                print(y[i])
                print(x[i])
        else:
            print("False")


    #for k,v in x.items():
    #    print(k,v)

hashfile()
