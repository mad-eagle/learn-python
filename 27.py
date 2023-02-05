def check(data):
    ansArrs = ("A","B","C","D","a","b","c","d")
    value = False
    if data[1] in ansArrs:
        match data[1]:
            case "A" :
                if data[0] == 0: value = True
            case "a" :
                if data[0] == 0: value = True
            case "B" :
                if data[0] == 1: value = True
            case "b" :
                if data[0] == 1: value = True
            case "C" :
                if data[0] == 2: value = True
            case "c" :
                if data[0] == 2: value = True
            case "D" :
                if data[0] == 3: value = True
            case "d" :
                if data[0] == 3: value = True
        return value    
    else: return "Invalid Input"

def kbc(data):
    print("*************************************************")
    print("*************************************************")
    print("                Welcome To KBC                   ")
    print("*************************************************")
    print("Question :",data["question"])
    print()
    print("       A :",data["Option"][0])
    print("       B :",data["Option"][1])
    print("       C :",data["Option"][2])
    print("       D :",data["Option"][3])
    print()
    answer = input("Give Answer in input as A , B , C or D : ")
    conditionCheck = check([data["index"] , answer])
    if conditionCheck == True:
        print("Sahi Jawab")
    elif not conditionCheck:
        print("Galat Jawab")
        print("Sahi Jawab hai :",data["Option"][data["index"]])
    else:
        print(conditionCheck)
        input("Click Enter to answer again :")
        kbc(data)
    
    
questions = [
    {
        "question":"ATM ka full form kya hai" ,
        "Option":["Any Time Money","Automated teller machine","Automatic teller machine","Automatic Transfer Money"] ,
        "index": 1
    } ,
    {
        "question":"USB ka full form kya hai" ,
        "Option":["Universal Serial Bus","Unique Serial Bus","Universal Secure Bus" , "Unified Serial Bus"] ,
        "index": 0
    } ,
    {
        "question":"PIN ka full forn kya hai" ,
        "Option":["Password Identification Number","Public Indentification Number","Private Identification Number","Personal Identification Number"] ,
        "index": 3
    }
]

for question in questions:
    kbc(question)