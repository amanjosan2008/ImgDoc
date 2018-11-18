This tool can be used to make life easy when managing huge collection of images downloaded from Internet.
This application will work completely in Linux(Ubuntu) & almost completely in Windows under Python 3 environment.

![](main.png)


Features:
- Count of Files
- Backup Files
- Missing Extensions
- Correct Extensions
- Webp Convert
- Replace Colon
- Verify Files
- Delete Backups
- Find Duplicate
- Find Similar Images
- Show Stats
- Top 10 Files
- Huge PNG Convertor


Requirements:
- Python3, Tkinter
- Sys, Glob, OS, RE
- Tarfile, Subprocess
- Imghdr, Shutil
- Pathlib, Itertools
- Collections, PIL
- Hashlib, Imagehash
- python-magic

For MacOSX:
- brew install libmagic

Current Issues:
- Duplicate, Similar, Search, Top Fn add => 90% + 10% ProgBar
- Add to Colonrep ==> Replace ' " , ? ` ~ ! @ # $ % ^ & * ; |
   List all files with special characters
   Option to replace with space or _
- FN subdir_mv stop if file exists in DUPS; do not delete other duplicate files
- Taskbar Icon in file
- Feature to append name_(1) in name if file exists
- Audio alert after long operation/Status bar red icon when Busy
- Save log file to:-  str(Path.home()) + "/imgdoc/image-ext-doctor.log"
- Windows/Mac Explore Fn not working; Replace Nautilus CLI cmd
- Search function different slash: if not (img == x[i]) in Windows only:
    D:/Files/Test/SmokyMountainCabinsWithViewsLarge.jpeg
    D:/Files/Test\SmokyMountainCabinsWithViewsLarge.jpeg
- Rewrite Correct Fn, remove Duplication; create sub-functions
- Open file on click in Listbox
- Fn to extract Zip Files & delete originals

New Features to be added:
