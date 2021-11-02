def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

f = factorial(5)
print("The Factorial of Number is: "+ str(f))
