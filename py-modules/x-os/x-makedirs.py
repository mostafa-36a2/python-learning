import os

folder = "/tmp/test_folder/here/it/is"
os.makedirs(folder)
if os.path.isdir(folder):
    print("makedirs done.")
else:
    print("makedirs failed.")
    
input("Press any key to continue ....")

with open(os.path.join(folder,"file1"),"w") as file:
    file.write("test content")
    
try:
    os.removedirs(folder)
except OSError as ose:
    if ose.errno == 39 and ose.strerror == "Directory not empty":
        print("Failed to removedir, because folder is not empty")

if not os.path.isdir(folder):
    print("removedirs done.")
else:
    print("removedirs failed.")