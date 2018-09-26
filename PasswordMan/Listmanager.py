myfile = open("passwordlist.txt", "r")

file = myfile.read().split(";")
print(file)

filteredList = {}
for entity in file:
    splitEntity = entity.split(":")
    key = splitEntity[0]
    value = splitEntity[1]
    if key not in filteredList:
        filteredList[key] = [value]
    else:
        filteredList[key].append(value)

for key in filteredList:
    print("The passwords for user " + key + " are: ")
    print(filteredList[key])
