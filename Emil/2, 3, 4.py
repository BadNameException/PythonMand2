# Oppgave 2 - unike password og brukernavn, telle totalt antall passord, telle antall passord knyttet til hver bruker
usernames = []
passwords = []
pw_to_each_user = {}
conn = 0


def readfile():
    global conn
    username = []
    password = []
    uname = bool(True)
    file = open("passwordlist.txt", "r")
    while (1):
        char = file.read(1)
        if char == ":":
            u = "".join(username)
            usernames.append(u)
            conn = conn + 1
            username = []
            uname = False

        elif char == ";":
            p = "".join(password)
            passwords.append(p)
            password = []
            uname = True

        elif not char:
            break
        else:
            if uname == True:
                username.append(char)
            else:
                password.append(char)
    file.close()
    unique()
    formatfile()


def unique():  # Kode hentet fra:https://stackoverflow.com/questions/9835762
    seenpw = set()
    uniquepw = []

    for x in passwords:
        if x not in seenpw:
            uniquepw.append(x)
            seenpw.add(x)

    seenuser = set()
    uniqueuser = []
    counter = 0
    for z in usernames:
        if z not in seenuser:
            uniqueuser.append(x)
            seenuser.add(x)
            pw_to_each_user.setdefault(z, []).append(passwords[counter])
            counter += 1
            continue
        elif x in seenuser:
            pw_to_each_user.get(z, []).append(passwords[counter])
            counter += 1
            continue

    for y in pw_to_each_user:
        print "user: '" + y + "', passwords: " + str(pw_to_each_user.get(y))


    print ("\nAntall unike passord: " + str(uniquepw.__len__()))
    print ("Antall unike brukernavn: " + str(pw_to_each_user.__len__()))
    print ("Totalt antall passord (inkludert duplikater): " + str(passwords.__len__()))


# Oppgave 3 - formatering
def formatfile():
    file = open("formatted_passwordlist.txt", "w")
    for x in pw_to_each_user:
        line = x + ":"
        for y in pw_to_each_user.get(x):
            line = line + y + ","

        line = line[:-1] + "\n"
        file.write(line)


# Oppgave 4 - feilhaandtering

# min main-seksjon
readfile()
