a = 10
def Number():
    global a
    print(f"The Value of a is:{a}")
    a = 20
    print(f"The Value of a is:{a}")

Number()
print(f"The Value of a is: {a}")