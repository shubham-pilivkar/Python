def sumOfElement(marks):
    Sum = sum(marks)
    avg = Sum / len(marks)
    return avg

list1 = [1, 2, 3, 4, 5]
print("The Length of list1 is:", len(list1))
Sum1 = sumOfElement(list1)
print("The Average of Element is: ", Sum1)

list2 = [10, 20, 30, 40, 50]
print("The Length of List2 is:", len(list2))
sum2 = sumOfElement(list2)
print("The Average of Number is:", sum2)