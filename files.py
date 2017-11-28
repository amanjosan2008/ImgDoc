import os
from collections import Counter

path1 = "D:\Files"

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
x = []
for file in files(path1):
    ext = os.path.splitext(file)[1][1:]
    x.append(ext)

print (Counter(x))
print (x[0])
print (x[1])
