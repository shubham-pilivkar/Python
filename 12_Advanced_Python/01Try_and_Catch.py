while(True):
    print("Enter q For Exit a Loop")
    a = input("Enter a Number: ")
    if a == "q":
        break
    try:
        a = int(a)
        if a>10:
            print("The Number is Greater Than 10")
        print("You Enter Number is:", a)
    except Exception as e:
        print(f"The Exception is {e}")

print("Thanks For Playing This Game")