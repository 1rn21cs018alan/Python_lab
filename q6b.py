import os      
import pathlib  
import zipfile

dirName = input("Enter Directory: ")
if not os.path.isdir(dirName):
    print("Directory doesn't exists")
    exit()
    
curDirectory = pathlib.Path(dirName)
with zipfile.ZipFile("ex.zip","w") as  f:
    for file_path in curDirectory.rglob("*"):  
        f.write(file_path, arcname=file_path.relative_to(curDirectory))
print(file_path)   

if os.path.isfile("ex.zip"):
    print("Zipped")
else:
    print("Error")
