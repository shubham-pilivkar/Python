num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))
num3 = int(input("Enter a Number: "))
num4 = int(input("Enter a Number: "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2 > num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print("The Greatest Number is: ", f1)
else:
    print("The Greatest Number is: ", f2)
