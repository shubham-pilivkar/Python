def divide(num):
    if num % 5 == 0:
        return num

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(filter(divide, list1))
print(a)