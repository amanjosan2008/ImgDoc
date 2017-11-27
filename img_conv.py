

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
