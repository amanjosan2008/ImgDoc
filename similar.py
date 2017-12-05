#!/usr/bin/env python3

import sys, os
from PIL import Image
import imagehash

dir = sys.argv[1]

def fullpath():
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)):
            yield (os.path.join(dir, file))

x = []
y = []
for file in fullpath():
    hash = imagehash.whash(Image.open(file))
    x.append(file)
    y.append(hash)

for i in range(len(x)):
    for j in range(i+1, len(x)):
        if y[i]-y[j] < 8:
            print ("Dupes: ", x[i],"  ", x[j], " Factor: ", y[i]-y[j])
