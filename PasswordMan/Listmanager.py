myfile = open("passwordlist.txt", "r")

file = myfile.read().split(";")

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

for key in filteredList:
    buriedArray = filteredList.get(key)
    print("The passwords for user " + key + " are: ")
    print(filteredList[key])
    print(key + " therefore has " + str(len(buriedArray)) + " password(s)")
    print()

print("There are " + str(counter) + " passwords in total")



