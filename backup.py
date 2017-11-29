import tarfile
import glob, os

dir = "/home/aman/Desktop/test"

try:
    os.mkdir("tmp")
except Exception:
    pass

tar = tarfile.open(os.path.join("tmp/" + "backup.tar.gz"), "w:gz")

wr = open(os.path.join("tmp/" + "file_list.txt"), "w")
wr.write("List of files:\n\n")

for name in glob.glob(os.path.join(dir, '*')):
    wr.write(name + '\n')
    tar.add(name)

wr.close()
tar.close()
