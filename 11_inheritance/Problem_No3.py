class Employee:
    Salary = 12345
    increament = 500
    
    @property
    def SalaryAfterIncreament(self):
        return self.Salary * self.increament
    
    @SalaryAfterIncreament.setter
    def SalaryAfterIncreament(self, Sai):
        self.increament = Sai / self.Salary

e = Employee()
print(e.SalaryAfterIncreament)

print(e.increament)
e.SalaryAfterIncreament = 2000
print(e.increament)
