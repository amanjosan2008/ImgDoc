

#version      Pillow 3.0.0
#--- TKINTER support available
#--- JPEG support available
#--- ZLIB (PNG/ZIP) support available
#--- FREETYPE2 support available
#--- WEBP support available


import imghdr
from PIL import Image

im = Image.open("unnamed.webp").convert("RGB")
im.save("test.jpg","jpeg")

----------------------------------------------------

from PIL import Image
import glob, os

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile).convert("RGB")
    im.save(file + ".webp", "WEBP")
