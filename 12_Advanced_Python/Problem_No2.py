list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
for index, list in enumerate(list1):
    if index == 2 or index == 4 or index == 6:
        print(f"The Element at index {index+1} is {list}")