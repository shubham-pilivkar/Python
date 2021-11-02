a = int(input("Enter a Number:"))

try: 
    with open("Table.txt", "w") as w:
        list = [a*i for i in range(1, 11)]
        w.write(str(list))
except Exception as e:
    print("This is an Exception Occurs")