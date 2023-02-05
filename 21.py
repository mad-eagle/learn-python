def first(a="Eagle",b="Gamer"):
    return a+" "+b

# first()

def second(*tpl):
    print(tpl)
    print(type(tpl))

# second(1,2,3)

def third(**dic):
    print(dic)
    print(type(dic))

third(name="Eagle",age=20,hobby="Hacking")
