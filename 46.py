import os

os.system("clear") # clear the screen 

currentWorkingDirectory = os.getcwd() # get current working directory

childs = os.listdir() # get all files name in list

# os.remove("test/1") # remote a file

testExist = os.path.exists("test")

child = ""   # create a string variable

for i , file in enumerate(childs):
    if i == len(childs)-1:
        child += file
    else:
        child += file+" , "


print("Current working directory :", currentWorkingDirectory) # print current working directory

print(child)  # print files names string variable

print(testExist)