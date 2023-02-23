class Employee:
    company = "Eagle pvt ltd"
    def __init__(self , name):
        self.name = name

    def show(self):
        return f"Name is {self.name} : company is {self.company}"
    
    @classmethod # the "classmethod" decorator change the first argument from instance to class
    def changeCompany(self,companyName):
        self.company = companyName

emp1 = Employee("eagle")
emp2 = Employee("codeleg")

print(emp1.show())
print(emp2.show())

emp1.changeCompany("Eagle International")

print(emp1.show())
print(emp2.show())

emp2.changeCompany("Eagle Umpire")

print(emp1.show())
print(emp2.show())