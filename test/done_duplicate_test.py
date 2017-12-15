# Delete 3 files without error
import os
from hashlib import md5
import collections

dir = "D:\Files\Claims\Mediassit\Test"
#dir = "/home/aman/Desktop/test"

def filesize(file):
    size = os.path.getsize(file)
    sizeinmb = size/1000000
    sizeflt = "{:.2f}".format(sizeinmb)
    return sizeflt

x,y = [],[]
for root,dir,fname in os.walk(dir):
    for fpath in fname:
        file = os.path.join(root, fpath)
        afile = open(file, 'rb')
        hasher = md5()
        buf = afile.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(65536)
        afile.close()
        hash = hasher.hexdigest()
        y.append(hash)
        x.append(file)


a = 1
b = [item for item, count in collections.Counter(y).items() if count > 1]

for i in range(len(b)):
    print("Duplicate Set", a)
    a += 1
    c = 0
    for j in range(len(y)):
        if b[i] == y[j]:
            #if write():
            try:
                if c == 0:
                    c += 1
                else:
                    #listbox.insert(END, file+"("+filesize(file)+"MB)"+" deleted and Converted file saved as: "+fnpng+"("+filesize(fnpng)+"MB)")
                    os.remove(x[j])
                    print("Deleted duplicate file: ", x[j])
            except FileNotFoundError:
                print("File already deleted: ", x[j])
                pass
            #else:
                #listbox.insert(END, file+"("+filesize(file)+"MB)"+" WILL BE deleted"

#listbox.insert(END, "Duplicate Set:"+str(i))
