class Employee:
    salary = 5500
    Bonous = 500

    def ChangeSallary(self, sal, bon):
        self.__class__.salary = sal
        self.__class__.Bonous = bon

    def Total_Salary(self):
        TotalSalary = self.salary + self.Bonous
        print(f"The Total Salary Of This Month is {TotalSalary}")

E1 = Employee()
E1.ChangeSallary(10000, 5000)
E1.Total_Salary()
