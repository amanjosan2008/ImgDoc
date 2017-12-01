import os
import sys
from itertools import islice
#from hashlib import md5
import hashlib

dir = sys.argv[1]

def fullpath(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield (os.path.join(path, file))


#validate()
x = []
#for file in fullpath(en.get()):
for file in fullpath(dir):
         hash = hashlib.sha256("a".encode('utf-8')).hexdigest()
         print(hash)
#        x.update({file: sizeflt})

#for i in range(3):
#    key, value = max(x.items(), key = lambda p: p[1])
#    print(key, " => ", value, "MB")
#    x.pop((max(x, key=x.get)))




#    hashes = defaultdict(list)
#    for fname in images[size]:
#        m = md5.new()
#        hashes[ m.update( file(fname,'rb').read(10000) ).digest() ] = fname
#    for k in hashes:
#       if len(hashes[k]) <= 1: continue
#       for fname in hashes[k][1:]:
#           print(fname)
