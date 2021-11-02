def maximum(num1, num2, num3):
    if(num1> num2 & num1> num3):
        return num1
    elif(num2 > num3):
        return num2
    else:
      return num3

max = maximum(10, 30, 90)
print("The Maximum Of Three Number is:", max)
