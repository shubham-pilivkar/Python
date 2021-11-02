class Complex:
    def __init__(self, i, j):
        self.real = i
        self.imaginary = j

    def __add__(self, c):
        return Complex(self.real + c.real, self.imaginary + c.imaginary)
    
    def __mul__(self, c):
        MulReal = self.real * c.real - self.imaginary * c.imaginary
        MulImg = self.real * c.imaginary + self.imaginary * c.real
        return Complex(MulReal, MulImg)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(3, 2)
c2 = Complex(1, 7)
print(c1 + c2)
print(c1 * c2)