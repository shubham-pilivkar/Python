class Employee:
    salary = 5500
    Bonous = 500

    def ChangeSallary(self, sal, bon):
        self.__class__.salary = sal
        self.__class__.Bonous = bon

    @property
    def Total_Salary(self):
        TotalSalary = self.salary + self.Bonous
        return TotalSalary

E1 = Employee()
E1.ChangeSallary(10000, 5000)
print(E1.Total_Salary) # This is Not Call a Function Type 
                       # it is Call a Property Type