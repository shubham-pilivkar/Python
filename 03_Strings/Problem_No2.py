name = input("Enter Your Name:")
date = input("Enter a Date:")
latter = '''Dear <|Name|>,
You are Selected!
Date: <|Date|>'''
latter = latter.replace("<|Name|>", name)
latter = latter.replace("<|Date|>", date)
print(latter)
