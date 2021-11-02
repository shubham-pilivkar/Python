def sumOfElement(n):
    if(n==1):
        return 1
    return n + sumOfElement(n-1)

S = sumOfElement(5)
print("The Sum of Number is:", S)