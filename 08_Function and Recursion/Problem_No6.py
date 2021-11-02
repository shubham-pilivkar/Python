def remove_Strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "  Shubham is   a good"
n = remove_Strip(this, "Shubham")
print(n)
