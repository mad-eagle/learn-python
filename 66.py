class Employee:
    def __init__(self,name):
        self.name =  name # this is Instance variable
        Employee.noOfEmployees = Employee.noOfEmployees + 1
    
    city = "mumbai" # this is class variable
    noOfEmployees = 0 # this is class variable
    

    
    def showDetails(self):
        print(f"Employee is {self.name}")

print(Employee.noOfEmployees)

emp1 = Employee("Atul")
emp2 = Employee("Eagle")
emp3 = Employee("Codeleg")

emp1.showDetails()
Employee.showDetails(emp1)

print("No. of Employees" , Employee.noOfEmployees)