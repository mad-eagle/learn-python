class MyClass:
    def __init__(self):
        self.publicVar = "I'm public"
        self._privateVar = "I'm private"
        self.__protectedVar = "I'm protected"

obj = MyClass() # creating object

print(obj.publicVar) # accessing public variable

print(obj._privateVar) # accessing private variable

print(obj._MyClass__protectedVar) # accessing procted variable