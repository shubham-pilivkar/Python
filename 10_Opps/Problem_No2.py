class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The Square of Number {self.num} is {self.num **2}")

    def squareRoot(self):
        print(f"The Square root of Number {self.num} is {self.num **3}")

    def cube(self):
        print(f"The Cube of Number {self.num} is {float(self.num **0.5)}")

s = Calculator(3)
s.square()
s.squareRoot()
s.cube()


