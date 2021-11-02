words = ["Monkay", "Donkay", "Tiger"]

with open("Problem_No55.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "Shubham")

with open("Problem_No55.txt", "w") as f2:
        f.write(content)

