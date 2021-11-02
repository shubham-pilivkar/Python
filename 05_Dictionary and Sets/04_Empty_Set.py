# This Represent a Dictnoary
# set = {}
# print(type(set))

# But we want a Empty Set
s = set()
s.add(10)
s.add(20)
s.add(30)
s.add(40)
s.add(50)
# s.add([60, 70]) We Cannot Add List into Set
s.add((30, 40))  # But We can Add Toupletes
print(s)
print(type(s))
