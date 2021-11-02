file1 = "Problem_No8.txt"
file2 = "problem_No8_Copy.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("The Two Files Are Identical")
else:
    print("The Two Files Are Not Identical")