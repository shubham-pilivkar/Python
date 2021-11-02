class Employee:
    company = "Microsoft"
    def companyName(self):
        print(f"The Name of Company is {self.company}")

class Progremmer1(Employee):
    language = "Python"
    def WorkingOn(self):
        print(f"Working on a Youtube with language {self.language}")

class Progremmer2(Employee):
    language = "Java"
    def WorkingOn(self):
        print(f"Working on a Google With Language {self.language}")

    
c = Employee()
c.companyName()

p1 = Progremmer1()
p1.WorkingOn()

p2 = Progremmer2()
p2.WorkingOn()

