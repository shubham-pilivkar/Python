def Divide(a, b):
    try:
        result = a / b
        print(f"The Division Of Two Numbers is {result}")
    except ZeroDivisionError:
        print("You Enter a Number Which is Not Divisible")
        print("Please Try Again Later")
    
a = int(input("Enter a First Number:"))
b = int(input("Enter a Second Number:"))
Divide(a, b)