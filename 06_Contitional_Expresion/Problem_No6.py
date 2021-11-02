m = int(input("Enter a marks: "))

if(m>=90 and m<=100):
    Grade = "O"
elif(m>=80 and m<90):
    Grade = "A" 
elif(m>=70 and m<80):
    Grade = "B"
elif(m>=60 and m<70):
    Grade = "C"
elif(m>=50 and m<60):
    Grade = "D"
else:
    Grade = "F"

print("The Gread You Have is: ", Grade)
