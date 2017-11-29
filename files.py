import shutil

try:
    shutil.rmtree("tmp")
    print("Deleted")
except:
    print("Backup not found")
