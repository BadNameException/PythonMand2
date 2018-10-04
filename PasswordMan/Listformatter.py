# Catches an exception if the text file can't be opened.
try:
    myfile = open("passwordlist.txt", "r")
except:
    print("Could not open the text-file.")

file = myfile.read().split(";")
myfile.close()

counter = 0
filteredList = {}
for entity in file:
    splitEntity = entity.split(":")
    key = splitEntity[0]
    value = splitEntity[1]
    if key not in filteredList:
        filteredList[key] = [value]
    else:
        filteredList[key].append(value)
    counter += 1


newfile = open("formattedpwlist.txt", "w+")

for key in filteredList:
    newfile.write("Passwords for the user " + key + ": \n")
    for value in filteredList[key]:
        newfile.write(value + ", ")
    newfile.write("\n" + "\n")
newfile.close()

"""
This format is better than the original as it is a lot easier to read.
It is also more searchable for humans as it does not duplicate usernames.
"""