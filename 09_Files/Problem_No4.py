from os import replace


with open("Problem_No4.txt", "r") as f:
    data = f.read()

with open("Problem_No4.txt", "w") as f2:
    f2.write(data.replace("Shubham", "Sunil"))
