import os

files = os.listdir("files")

manager = {}


for file in files:
    fileName = file.split(".")

    if not fileName[1] in manager:
        os.rename(f"files/{file}",f"files/1.{fileName[1]}")
        manager[fileName[1]] = 1
    else:
        manager[fileName[1]] = manager[fileName[1]] + 1
        os.rename(f"files/{file}",f"files/{manager[fileName[1]]}.{fileName[1]}")

print(manager)
