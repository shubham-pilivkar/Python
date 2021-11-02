f = open("Problem_No1.txt", "r")
data = f.read()
if ("Twinkle" in data):
    print("Yes The Twinkle Name is Present in poem")
else:
    print("The Twinkle Name is Not Present in Poem")
f.close()
