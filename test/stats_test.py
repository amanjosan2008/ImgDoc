
#SORT RESULTS

import os

dir = "D:\Files\Data\Claims"

x = []
for root, subdir, files in os.walk(dir):
    for file in files:
        ext = os.path.splitext(file)[1][1:]
        x.append(ext)
y = set(x)
for i in y:
    print(i, x.count(i))
