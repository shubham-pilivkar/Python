class Employee:
    Company = "Google"
    Salary = 100
    location = "Delhi"
    
    # def changeSalary(self, salary): # it can Change the only Property of Object
    #     self.Salary = salary
    
    def changeClassSalary(self, salary): # it can Change The Property of Class
        self.__class__.Salary = salary  # and used To Modify Properties


e = Employee()
print(e.Salary)
e.changeClassSalary(200)
print(e.Salary)
print(Employee.Salary)


