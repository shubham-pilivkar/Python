text = input("Enter a Text: ")

if("Make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click This" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This Text is Spam")
else:
    print("This Text is Not Spam")