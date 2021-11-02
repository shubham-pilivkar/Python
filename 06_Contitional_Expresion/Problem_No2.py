m1 = int(input("Enter The Marks Of Subject 1: "))
m2 = int(input("Enter The Marks Of Subject 2: "))
m3 = int(input("Enter The Marks Of Subject 3: "))
sum = m1 + m2 + m3
avg = int(sum / 3)

if(m1 < 33 or m2 < 33 or m3 < 33):
    print("You Are Fail Due to in One Subject Your marks is less than 33")

if(avg < 40):
    print("You Are Fail Due to Your Percentage is Less than 40")
    print("Your Percentage is: ", avg)
else:
    print("You Are Pass")
    print("Your Percentage is: ", avg)
