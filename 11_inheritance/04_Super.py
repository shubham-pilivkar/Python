class Boy:
    std = 5
    def __init__(self):
        print("This is an Boy Class \n")

    def Skills(self):
        print("Know Basic Of Addition and Substraction")
        print("Konw Basic About Science")

class Student(Boy):
    std = 10
    def __init__(self):
        super().__init__()
        print("This is an Student Class\n")

    def Skills(self):
        super().Skills()
        print("Konw about algebra and Geometry")
        print("Basic idea about science")
    
class Programmer(Student):
    std = 13
    def __init__(self):
        super().__init__()
        print("This is an Programmer Class\n")
    def Skills(self):
        super().Skills()
        print("Java Programming")
        print("Python Programming")

P = Programmer()
print(P.std)
P.Skills()