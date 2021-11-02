def File(FileName):
    try:
      with open(FileName, "r") as i:
         print(i.read())
    except FileNotFoundError:
        print(f"The {FileName} this file is not Found")


File("1.txt")
File("2.txt")
File("3.txt")

