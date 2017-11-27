from PIL import Image
import glob, os

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile).convert("RGB")
    im.save(file + ".webp", "WEBP")
