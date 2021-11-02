import random

def Game(Comp, You):
    if Comp == You:
         return None
    elif Comp == "S":
       if You == "W":
         return False
       elif You == "G":
         return True
    elif Comp == "W":
        if You == "G":
         return False
        elif You == "S":
         return True
    elif Comp == "G":
        if You == "S":
         return False
        elif You == "W":
         return True


You = input("Enter Your Choice Snake(S), Water(W), Gun(G):")
input = random.randint(1, 3)
if input == 1:
   Comp = "S"
elif input == 2:
   Comp = "W"
elif input == 3:
   Comp = "G"

win = Game(Comp, You)

print("The Computer Choice is:", Comp)
print("Your Choice is:", You)
if(win == None):
    print("The Match is Tie")
elif(win == True):
    print("You Are Win")
else:
    print("You Will Loose")



