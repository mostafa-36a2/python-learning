import shutil
import os
test_src_folder = "/tmp/test_src_folder"
test_dst_folder = "/tmp/test_dst_folder"
test_file_name="test_file"
test_file_src_path = os.path.join(test_src_folder,test_file_name)
test_file_dst_path = os.path.join(test_dst_folder,test_file_name)
os.makedirs(test_src_folder,exist_ok=True)
os.makedirs(test_dst_folder,exist_ok=True)

with open(test_file_src_path,"w") as test_file:
    test_file.write("Test content")

if os.path.isfile(test_file_src_path):
    print("Test file created in src folder")
else:
    print("Test failed 1")
    exit()
    
# copy to test_dst_folder
res = shutil.copyfile(test_file_src_path,test_file_dst_path)

if os.path.isfile(test_file_src_path):
    print("Test file now moved out src folder")
else:
    print(f"Test failed 2, res = {res}")
    exit()


if os.path.isfile(test_file_dst_path):
    print("Test file moved successfully to dst folder")
else:
    print("Test failed 3")
    exit()

os.remove(test_file_src_path)
os.remove(test_file_dst_path)
os.removedirs(test_src_folder)
os.removedirs(test_dst_folder)