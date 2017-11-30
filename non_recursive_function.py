#!/usr/bin/env python3

import os, sys, imghdr

dir = sys.argv[1]

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def fullpath(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield (os.path.join(path, file))


for file in fullpath(dir):
    print(file)

for file in files(dir):
    print(file)


files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]

for file in files:
    print(file)
