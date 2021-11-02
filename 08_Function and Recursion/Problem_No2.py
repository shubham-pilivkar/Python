def convert(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

converter = convert(45)
print("The Tempereature in Fahrenheit is: ", converter)