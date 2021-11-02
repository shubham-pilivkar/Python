class V2dVector:
    def __init__(self, i, j):
        self.iCap = i
        self.jCap = j
    def __str__(self):
        return f"{self.iCap}i + {self.jCap}j"
       
class V3dVector(V2dVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kCap = k
    def __str__(self):
        return f"{self.iCap}i + {self.jCap}i + {self.kCap}k"

v1 = V2dVector(5, 10)
v2 = V3dVector(5, 10, 15)
print(v1)
print(v2)
    