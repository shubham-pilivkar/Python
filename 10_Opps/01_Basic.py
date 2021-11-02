class SumOfNumber:
    def sum(self):
        result = self.a + self.b
        return result

num = SumOfNumber()
num.a = 10
num.b = 20
s = num.sum()
print("The Sum of Two Numbers is:", s)
