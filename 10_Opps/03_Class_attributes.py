class Employee:
    company = "MicroSoft"
    def info(self):
        print(f"The Name of Worker is {self.name}")
        print(f"The Salary of Employee is {self.salary}")
        print(f"The Company of Employee is {self.company}")

shubham = Employee()
shubham.name = "Shubham Pilivkar"
shubham.salary = "100k"
shubham.company = "Google"
shubham.info()