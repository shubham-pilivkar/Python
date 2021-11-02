class Number:
    def __init__(self, num):
       self.num = num

    def __str__(self):
       print(f"Decimal NUmber: {self.num}")

    def __len__(self):
        return 1

n = Number(5)
print(n)
print(len(n))

