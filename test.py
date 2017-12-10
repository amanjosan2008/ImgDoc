
import os

dir = '/home/aman/Desktop'

x,y = [],[]

for root, subdir, files in os.walk(dir):
    for file in files:
        file, ext = os.path.splitext(file)
        x.append(ext)

y = set(x)
z = []

for i in y:
    for i in x:
        print (i)
