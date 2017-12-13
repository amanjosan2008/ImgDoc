I have created this tool to make life easy when managing huge collection of images downloaded from Internet.
This application will work in both Linux & Windows under Python 3 environment.

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
- Python3
- Tkinter
- Sys
- Glob
- OS
- RE
- Tarfile
- Imghdr
- Shutil
- Subprocess
- Pathlib
- Collections
- PIL
- Itertools
- Hashlib
- Imagehash


Pending Tasks:

- Taskbar Icon in file
- If Ext == JPEG, rename to JPG
- Listbox auto scroll
- Append (1) in name if existing file
- Warn Existing backup/Overwriting
- Remove other special characters , ! ? #
- Search images similar to a selected image
- Audio alert after long operation/Status bar red icon when Busy
- Stats fn - Sort results
- Search function difference: if not (img == x[i]) Windows only:
    D:/Files/Claims/Mediassit/Test/SmokyMountainCabinsWithViewsLarge.jpeg
    D:/Files/Claims/Mediassit/Test\SmokyMountainCabinsWithViewsLarge.jpeg
- Duplicate Fn apply 3rd Array logic
