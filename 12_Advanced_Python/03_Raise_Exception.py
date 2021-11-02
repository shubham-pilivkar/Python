def increment(num):
    try:
       return int(num)+1
    except:
        raise ValueError("You Enter a Some Different Number")

a = increment(55)
print(a)
