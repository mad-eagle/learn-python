import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
bigLetter = letters.upper()
chars = letters + bigLetter + numbers

def randomText(length):
    text = ''
    for i in range(length):
        randomChar = random.choice(chars)
        text += randomChar
    return text

randomWord = randomText(6)

print(randomWord)