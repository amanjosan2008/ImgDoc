from PIL import Image
import os, imagehash, sys

path = "/home/aman/Desktop/test"

image = sys.argv[1]
hash1 = imagehash.whash(Image.open(image))

x,y = [],[]
for root,subdir,fname in os.walk(path):
    for fpath in fname:
        file = os.path.join(root, fpath)
        hash = imagehash.whash(Image.open(file))
        x.append(file)
        y.append(hash)

for i in range(len(x)):
    if not (image == x[i]):
        if y[i]-hash1 < 8:
            print("Dupes: ", "Factor:", str(y[i]-hash1))
            print(x[i])
