#I'm working on a cleanup script for tv shows that I download.
#I want it to get the largest file in each folder, move/rename it and then delete that folder.

import os
import sys

biggest = ("", -1)
directory = sys.argv[1]

print "Searching", directory

def search(dir):
    global biggest
    for item in os.listdir(dir):
        item = dir + "/" + item
        if os.path.isdir(item):
            search(item)
        else:
            itemsize = os.path.getsize(item)
            if itemsize > biggest[1]:
                    biggest = (item, itemsize)

search(directory)
if biggest[1] != -1:
    print "Found: ", biggest
    # Do something with biggest
