# Delete 3 files without error
import os
from hashlib import md5

#dir = "D:\Files\Claims\Mediassit\Claim 2"
dir = "/home/aman/Desktop/test"

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
        x.append(hash)
        y.append(file)
a = len(x)
b = 1
for i in range(a):
    for j in range(i+1, a):
        if x[i] == x[j]:
            print("Duplicate Set", b,":")
            print(y[i])
            print(y[j])
            b += 1
            #if write():
            try:
                #listbox.insert(END, file+"("+filesize(file)+"MB)"+" deleted and Converted file saved as: "+fnpng+"("+filesize(fnpng)+"MB)")
                os.remove(y[j])
                print("Deleted duplicate file: ", y[j])
            except FileNotFoundError:
                print("File already deleted: ", y[j])
                pass
            #else:
                #listbox.insert(END, file+"("+filesize(file)+"MB)"+" WILL BE deleted"

#listbox.insert(END, "Duplicate Set:"+str(i))
