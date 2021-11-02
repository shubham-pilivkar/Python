myDict = { "Key": "Value",
    "Shubham": "Coder",
    "Marks": "100",
    "List": "[1, 2, 3]", 
    "list": {'Shubham':'Sunil'}
}
print(myDict["Key"])
print(myDict["Shubham"])
print(myDict["Marks"])

# It Can Be Change or Muttable 
myDict["List"] = [10, 20, 30]
print(myDict["List"])

print(myDict['list'])
print(myDict['list']['Shubham'])