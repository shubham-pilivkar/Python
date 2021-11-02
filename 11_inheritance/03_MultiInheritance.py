class Boy:
    std = 5
    def Skills(self):
        print("Know Basic Of Addition and Substraction")
        print("Konw Basic About Science")
        
class Student(Boy):
    std = 10
    def Skills(self):
        print("Konw about algebra and Geometry")
        print("Basic idea about science")
    
class Programmer(Student):
    std = 13
    def Skills(self):
        print("Java Programming")
        print("Python Programming")

P = Programmer()
print(P.std)
P.Skills()
