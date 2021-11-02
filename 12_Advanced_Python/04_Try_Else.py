try:
    a = input("Enter a Number: ")
    a = int(a)
    b = 1 / a
    print(f"Divide Number 1 by {a} result is: {b}")
except Exception as e:
    print(e)
    print("The Number is Not Sucessfully Divide by Zero")
else:
    print("The Number is Sucessfully Divide by number")

