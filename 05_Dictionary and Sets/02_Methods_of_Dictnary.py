myDict = {"Shubham": "Coder",
        "Sunil": "IAS",
        "Key": "Value", 
        "Harry": "Code",
        "Marks": [10, 20, 30],
        10: 20,
        "List": [1, 2, 3]}

# Add New Values in Dictnoray
addDict = {"Ganesh": "Farmastist",
           "Shanker": "Friend",
           "Darshana": " Friend",
           "Sunil": "BestFriend"}
myDict.update(addDict)

# Print The Keys in Dictnory
print("The Keys in Dictnory: ", myDict.keys())

# Print The Values in Dictnoary
print("The Values in Dictnory: ", myDict.values())

# Print The Total Element in Dictnory
print("The Total Items is:", myDict.items())

# Get The Values 
# it Shows a error when The Key is Not Present
print(myDict["Shubham"]) 
# but The Get Method Cannot Throw Error it shows None
print(myDict.get("Shubham"))