# print(3+3)
# print(3-3)
# print(3*3)
# print(3/3)
# print(3**3)

a = int(input("Enter First Number : "))
b = int(input("Enter second Number : "))
c = input("Enter Character : ")

if c == "+" : print(a+b)
elif c == "-" : print(a-b)
elif c == "*" : print(a*b)
elif c == "/" : print(a/b)
elif c == "**" : print(a**b)
elif c == "//" : print(a//b)
else : print("Invalid Character")