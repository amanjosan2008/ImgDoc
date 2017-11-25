#!/usr/bin/env python3

import os, re, sys, glob
import imghdr, shutil
import subprocess, tarfile
from pathlib import Path

try:
    directory = sys.argv[1]
except:
    print("\nException occured: Full Directory path with images not defined.\n")
    sys.exit()

# Code for Archiving existing files & save list of files
print("---=========== Started backup of files =============---")

tar = tarfile.open("backup.tar.gz", "w:gz")
wr = open("file_list.txt", "w")
wr.write("List of files:\n\n")
x = 0

for name in glob.glob(os.path.join(directory, '*')):
    wr.write(name + '\n')
    tar.add(name)
    x += 1

wr.close()
tar.close()

print ("Initial No of Files: ", x)


# Code to add Ext if not present & remove double Ext
print("\n---=========== Started Unique extensions =============---\n")

for root, dirs, files in os.walk(directory):
    for name in files:
        file = root +"/"+ name

        # find double extensions
        fn1, ext1 = os.path.splitext(file)
        fn2, ext2 = os.path.splitext(fn1)
        ftype = imghdr.what(file)

        if ftype == None:
            print(file, "Unsupported file")
        else:
          newname = file +"."+ ftype
          if not ext1:
            filechk2 = Path(newname)
            if filechk2.is_file():
                print (filechk2, "File already EXISTS, not overwriting")
            else:
                shutil.move(file, newname)
                print (file, "has no ext, Appending:", ftype)
          else:
            if not ext2:
#                print("1 Extension only")
                continue
            elif ext2 == ext1:
                filechk = file.replace(ext1,ftype)
                filechk2 = Path(filechk)
                if filechk2.is_file():
                    print (filechk2, "File already EXISTS, not overwritting")
                else:
                    shutil.move(file, fn1.replace(ext2,ext1))
                    print (file, "has 2 Same ext, Removing:", ext2)
            elif ext2 != ext1:
                filechk = file.replace(ext1,ftype)
                filechk2 = Path(filechk)
                if filechk2.is_file():
                    print (filechk2, "File already EXISTS, not overwritting")
                else:
                    shutil.move(file, fn1.replace(ext2,ext1))
                    print (file, "has 2 Diff ext, Removing:", ext2)
            else:
                print ("Something wrong with file or logic")


# Code to Correct File Extensions
print("\n---=============== Started correcting extension ================---\n")

for root, dirs, files in os.walk(directory):
    for name in files:
        file = root+"/"+name

        # find the correct extension
        ftype = imghdr.what(file)
        ext = os.path.splitext(file)[1][1:]

        # find files with the (incorrect) extension to rename
        if ext:
            if ftype != ext:
                if ftype != None:
                  if (ftype == "jpeg") & (ext == "jpg"):
                    continue
#                    print(file, "File type is JPG/JPEG, ignoring")
                  else:
                    filechk = file.replace(ext,ftype)
                    filechk2 = Path(filechk)
                    if filechk2.is_file():
                        print (filechk2, "File already EXISTS, not overwritting")
                    else:
                        # rename the file
                        shutil.move(file, file.replace(ext,ftype))
                        print (file, ext, ("=>"), ftype)
                # in case it can't be determined, mention it in the output
                else:
                    if ext == "png":
                        filechk = file.replace(ext,"jpg")
                        filechk2 = Path(filechk)
                        if filechk2.is_file():
                            print (filechk2, "File already EXISTS, not overwritting")
                        else:
                            shutil.move(file, file.replace(ext,"jpg"))
                            print (file, "File type not determined for PNG =>", file.replace(ext,"jpg"))
                    else:
                        print(file, "Could not determine file type")
            else:
                continue
#                print(file, "Correct Extension")
        else:
            print(file, "No Extension detected")


# Code to convert WEBP to PNG
print("\n---================== Started WEBP to PNG conversion ===============---\n")

for root, dirs, files in os.walk(directory):
    for name in files:
        file = root + "/" + name

        fn, ext = os.path.splitext(file)
        if ext == ".webp":
            fnpng = fn + ".png"
            fpath = Path(fnpng)
            if fpath.is_file():
                print (fnpng, "File already EXISTS, not overwritting")
            else:
                conv = subprocess.Popen(["dwebp", file, "-o", fnpng], stdout=subprocess.PIPE)
                output, err = conv.communicate()
                rmfile = subprocess.Popen(["rm", file], stdout=subprocess.PIPE)
                output2, err2 = rmfile.communicate()
        else:
            continue
#            print (file, "File is not Webp, Skipping")


# Code to replace : with _ in file names
print("\n---=============== Started Colon replace space =============---\n")

for root, dirs, files in os.walk(directory):
    for name in files:
        file = root + "/" + name

        if re.search(r':', file):
            filechk = file.replace(":","_")
            filechk2 = Path(filechk)
            if filechk2.is_file():
                print (filechk2, "File already EXISTS, not overwriting")
            else:
                # rename the file
                shutil.move(file, file.replace(":","_"))
                print (file, ("Colon => "), file.replace(":","_"))
        else:
             continue
#            print(name, "  Colon Not Found in name")

print("\n---===================== All Done =======================---\n")


# Code to verify if any file missing, deleted, overwritten
y = 0

for name in glob.glob(os.path.join(directory, '*')):
    y += 1

print ("Initial No of Files: ", x)
print ("Final   No of Files: ", y)

if x == y:
    print("Operation completed successfully")
else:
    print("Operation failed, some files missing")
