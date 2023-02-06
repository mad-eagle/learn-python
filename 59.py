# Decorator function
def modify(fx):
    def mfx(*args):
        print("Start executing the function...")
        fx(*args)
        print("Done execution the function...")
    return mfx

# Executing decorator function with normal method
#################################################
def fun1():
    print("First processing...")

modify(fun1)()  # executing with normal method


# Execuing with @ keyword methord
#################################################
@modify         # using keyword before function
def fun2():
    print("Second Processing...")

# Accepting argunents
#################################################
@modify
def add(*args):
    value = 0
    for i in args:
        value += i
    print(f"Addition of values : {value}")

add(1,2,3,4,5)