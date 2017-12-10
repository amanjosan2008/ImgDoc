import os

dir = "D:\Files\Data\Claims\done"

x = []
y = []
z = []

for root, subdir, files in os.walk(dir):
    for file in files:
        fname, ext = os.path.splitext(file)
        x.append(ext)

y = set(x)

for i in y:
    a = 0
    for y in x:
        a += 1
    z.append(a)
print(z)
