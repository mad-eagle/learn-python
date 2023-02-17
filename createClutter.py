import random
import os

def randomText(length,space=False):
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = " 1234567890 "
    bigLetter = letters.upper()

    def chars():
        return letters+bigLetter+numbers if space else letters

    text = ''.join(random.choice(chars()) for i in range(length))

    return text.strip()

def getRandomFileName():
    fileName = randomText(random.randint(3,10),True)
    fileExt = randomText(random.randint(1,4))
    return f"{fileName}.{fileExt}"

if not os.path.exists("files"):
    os.mkdir("files")

for i in range(10000):
    fileName = f"files/{getRandomFileName()}"
    with open( fileName , "w") as file:
        file.write(f"This is file {i+1}.")