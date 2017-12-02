#!/usr/bin/env python3

#from tkinter import *
#import sys, glob, os, re
#import tarfile
#import imghdr, shutil
#import subprocess
#from pathlib import Path
#from collections import Counter

#dir = sys.argv[1]


some_dict = {"firstname":"Albert","nickname":"Albert","surname":"Likins","username":"Angel"}

rev_multidict = {}
for key, value in some_dict.items():
     rev_multidict.setdefault(value, set()).add(key)


print([key for key, values in rev_multidict.items() if len(values) > 1])
