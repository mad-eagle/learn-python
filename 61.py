class BasicDetails:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @property
    def show(self):
        return f"Name : {self.name}\nAge : {self.age}"

class Details(BasicDetails):
    @property
    def email(self):
        return f"{self.name}{self.age}@email.com"
    
a = BasicDetails("eagle",21)
b = Details("Codeleg",14)
print(a.show)
print("------------")
print(b.show)
print(b.email)