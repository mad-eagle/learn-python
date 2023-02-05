def encrypt(text):
    a = text.split(" ")
    str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str2 = "abcdefghijklmnopqrstuvwxyz"
    str = ""
    for b in text:
        for c in b:
            if c.isupper():
                str += str1[25-str1.find(c)]
            elif c.islower():
                str += str2[25-str2.find(c)]
            else:
                str += c
            
        
    return str

str = "I am Eagle"

ans = encrypt(str)
print(ans)
print(encrypt(ans))