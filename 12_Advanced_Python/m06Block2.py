def Sum(a, b):
    result = a + b
    return result

print(__name__)
if __name__ == '__main__':
   a1 = int(input("Enter a First Number:"))
   a2 = int(input("Enter a Second Number:"))
   result = Sum(a1, a2)
   print(f"The Sum of Two Numbers is {result}")