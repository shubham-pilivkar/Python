class Employee:
    company = "Microsoft"
    def info(self):
        print(f'''The Name of Company is {self.company} and Salary is {self.salary}''')
    
shubham = Employee()
shubham.company = "Google"
shubham.salary = "100k"
shubham.info()