import os
import shutil

from_dir= "c:/Users/Roop/Downloads"
to_dir= "c:/Users/Roop/Desktop/Document_files"

list_of_files= os.listdir(from_dir)
print (list_of_files)

for file in list_of_files:
    name,extension=os.path.splitext(file)
    print(name,extension)
