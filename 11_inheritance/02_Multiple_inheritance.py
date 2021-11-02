class Company1:
    company = 'Google'
    eCode = 120
    def workingon(self):
        print("Self Driving Car Software")
        

class Company2:
    company = "Tesla"
    level = 0
    def workingon(self):
        print("Working on Design of car")
    def ImproveLevel(self):
        self.level = self.level + 1

class Company(Company1, Company2):
    company = "Google -Tesla"
    def Complete(self):
        print("The Complete Car is Formed")
        print(f"The Car Manifacture Company name is {self.company}")

c = Company()
c.Complete()
print(c.level)
c.ImproveLevel()
print(c.level)




