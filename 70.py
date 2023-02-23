class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    # Making alternate constructor using class method
    @classmethod
    def secondConstructor(self,string):
        str = string.split(":")
        return self(str[0],str[1])

    def show(self):
        return f"{self.name}'s salary : {self.salary}"

e1 = Employee("Eagle" , "5000") # this object made by normal constructor
e2 = Employee.secondConstructor("Codeleg:1000") # this object made by alternate constructor

print(e1.show())
print(e2.show())