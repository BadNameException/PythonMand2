# Catches an exception if the text file can't be opened.
try:
    myfile = open("passwordlist.txt", "r")
except:
    print("Could not open the text-file.")


file = myfile.read().split(";")
myfile.close()

filtered_list = {}
counter = 0
unique_password_list = []

for entity in file:
    # Check if the text file has any content.
    if len(file) == 0:
        print("The list of usernames and passwords are empty.")
        break
    split_entity = entity.split(":")
    key = split_entity[0]
    value = split_entity[1]
    if value not in unique_password_list:
        unique_password_list.append(value)
    if key not in filtered_list:
        filtered_list[key] = [value]
    else:
        filtered_list[key].append(value)
    counter += 1

for key in filtered_list:
    buried_array = filtered_list.get(key)
    print("The passwords for user " + key + " are: ")
    print(filtered_list[key])
    print(key + " therefore has " + str(len(buried_array)) + " password(s)")
    print()

print("There are " + str(counter) + " passwords in total")
print("\nThere are " + str(len(unique_password_list)) + " unique passwords. They are:")
for password in unique_password_list:
    print(password)


