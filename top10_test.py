# rewrite this function using arrays

import os

dir = "D:\Files\Claims\Mediassit\Test"

def fullpath():
        for root,dire,fname in os.walk(dir):
            for file in fname:
                yield (os.path.join(root, file))

def filesize(file):
    size = os.path.getsize(file)
    sizeinmb = size/1000000
    sizeflt = "{:.2f}".format(sizeinmb)
    #return sizeflt
    return size

x,y = [],[]
for file in fullpath():
        #relfile = os.path.relpath(file, en.get())
        relfile = os.path.relpath(file, dir)
        x.append(filesize(file))
        y.append(relfile)

if (len(x) < 10):
    c = len(x)
else:
    c = 10

for i in range(len(x)):
    a = 0
    for i in range(len(x)):
        if x[i] > a:
            a = x[i]
            b = i
    print(y[b], x[b])
    x.remove(x[b])
    y.remove(y[b])


        # Limit iterations to 10 or less in case lesser no of files
        #if (len(x) < 10):
        #    a = len(x)
        #else:
        #    a = 10
        #for i in range(a):
        #    key, value = max(x.items(), key = lambda p: p[1])
        #    sizeinmb = (value/1000000)
        #    sizeflt = "{:.2f}".format(sizeinmb)
        #    listbox.insert(END, key+" => "+sizeflt+"MB")
        #    x.pop((max(x, key=x.get)))
#listbox.insert(END, "--------------Done Top 10 Function--------------")
