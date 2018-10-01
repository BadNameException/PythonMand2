from platform import system as system_name
from subprocess import call as system_call

class PingIP:

    def pinglocalhost(self, os):
        # Selve kommandoen
        command = ["ping", os, "1", "localhost"]

        # Returnerer true dersom maskinen svarer paa pingen
        return system_call(command) == 0

    # Loopen begynne neste iterasjon naar den faar True eller False fra funksjonen (dvs det tar ganske lang tid...)
    def pingIPrange(self, os, ip):
        i = 0
        while i < 255:
            command = ["ping", os, "1", ip + "." + str(i)]
            i += 1
            print system_call(command) == 0


pingip = PingIP()

# Sjekker om det er windows eller unix
os = "-n" if system_name().lower() == "windows" else "-c"
pingip.pinglocalhost(os)
pingip.pingIPrange(os, "192.168.10")