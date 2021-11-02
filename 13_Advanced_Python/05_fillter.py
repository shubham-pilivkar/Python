def greater(num):
    if num>5:
        return True
    else:
        return False

list1 = [1, 5, 10, 15, 20, 25]
result = list(filter(greater, list1))
print(result)