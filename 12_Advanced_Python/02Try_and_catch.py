try:
    a = input("Enter a Number: ")
    a = int(a)
    b = int(1 / a)
    print(b)
except ValueError:
    print("You Enter a Some incorrect Value")
    print("Please Correct it ")
except ZeroDivisionError:
    print("You Enter Number is Zero")
    print("Soo Zero is Not Divide By Any Number")
except Exception:
    print("There is SomeThing Exception is Occur")

print("Thanks for Using This Code")