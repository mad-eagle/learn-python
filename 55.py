import os , random

# rock     ==  A
# paper    ==  B
# scissor  ==  C

os.system("clear")

def identify(a):
    match a:
        case "a" : return "Rock"
        case "b" : return "Paper"
        case "c" : return "Scissor"

def check(a,b):
    if a == "a":
        return 1 if b == "c" else 2
    elif a == "b":
        return 1 if b == "a" else 2
    else:
        return 1 if b == "b" else 2

print("----------------------------------------")
print("Welcome in Rock paper scissor game")
print("----------------------------------------")
print("Choose you what you want :")
print("A : Rock")
print("B : Paper")
print("C : Scissor")
print("----------------------------------------")

do = True
value = ""
win = None
values = [ "A" , "a" , "B" , "b" , "C" , "c"]
computerValue = random.choice(["a","b","c"])

while not value in values or do:
    value = input("Enter : ")
    value = value.lower()
    do = False
    print("Invalid Input" , "Try Again\n") if not value in values else None

while value == computerValue:
    computerValue = random.choice(["a","b","c"])

print("----------------------------------------")
print(f"Computer : {identify(computerValue)}\nYou : {identify(value)}   ")
print("----------------------------------------")

print("You won") if check(value,computerValue) == 1 else print("Computer Won")
print("----------------------------------------")
print("----------------------------------------")