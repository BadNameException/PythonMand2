# Oppgave 2 - unike password og brukernavn, telle totalt antall passord, telle antall passord knyttet til hver bruker
usernames = []
passwords = []

def readfile():

    username = []
    password = []
    uname = bool(True)
    file = open("passwordlist.txt", "r")
    while (1):
        char = file.read(1)
        if char == ":":
           u = "".join(username)
           usernames.append(u)
           print ("Bruker: " + u)
           username = []
           uname = False

        elif char == ";":
            p = "".join(password)
            passwords.append(p)
            print ("Passord: " + p)
            password = []
            uname = True

        elif not char: break
        else:
            if uname == True:
                username.append(char)
            else:
                 password.append(char)
    file.close()

# Oppgave 3 - formatering
def formatfile():
    file = open("formatted_passwordlist", "w")
    for line in file:
        print line,

# Oppgave 4 - feilhaandtering

readfile()