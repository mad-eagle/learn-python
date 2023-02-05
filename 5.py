# Decorator function
def modify(fx):
    def mfx():
        print("Start executing the function...")
        fx()
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

fun2()