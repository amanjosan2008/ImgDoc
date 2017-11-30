#I'm working on a cleanup script for tv shows that I download.
#I want it to get the largest file in each folder, move/rename it and then delete that folder.

import os
import sys
from itertools import islice

dir = sys.argv[1]

def fullpath(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield (os.path.join(path, file))


#validate()
x = {}
#for file in fullpath(en.get()):
for file in fullpath(dir):
        filesize = (os.path.getsize(file))
        sizeinmb = (filesize/1000000)
        sizeflt = "{:.2f}".format(sizeinmb)
        x.update({file: sizeflt})

for i in range(3):
    key, value = max(x.items(), key = lambda p: p[1])
    print(key, " => ", value, "MB")
    x.pop((max(x, key=x.get)))
