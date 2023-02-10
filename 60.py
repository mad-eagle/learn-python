class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def showName(self):
        print(f"name is : {self.name}")
    
    @property
    def showAge(self):
        return f"{self.name}'s age is : {self.age}"

    @showAge.setter
    def showAge(self , arr):
        print("Setting now")
        self.name = arr[0]
        self.age = arr[1]

a = person("eagle",21)
print(a.showAge)
a.name = "shani"
print(a.showAge)
a.showAge = ["Codeleg" , 14]
print(a.showAge)