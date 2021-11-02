num = int(input("Enter a Number: "))
if(num>1):
  for i in range(2, num):
    if(num % 2 == 0):
        isPrime = False
        break
    else:
        isPrime = True
else:
    isPrime = False
    
if(isPrime):
    print("The Given Number is prime")
else:
    print("The Given Number is Not Prime")
