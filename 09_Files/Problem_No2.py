def game():
   return 80

score = game()
with open("Problem_No2.txt", "r") as f:
    highScore = f.read()

if(highScore == ""):
    with open("Problem_No2.txt","w") as f:
        f.write(str(score))
elif (int(highScore) < score):
    with open("Problem_No2.txt", "w") as f:
      f.write(str(score))
