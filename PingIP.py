##This only runs on windows for the moment
import os


class PingIP:

    def pingLocalhost(self):
        os.system("ping localhost -n 1")

    def __init__(self):
        print("Attempting to ping localhost")
        self.pingLocalhost()

    def pingSubnet(self, ipaddress):
        splitIP = ipaddress.split(".")

        counter = 1
        while(counter < 255):
            addr = splitIP[0] + "." + splitIP[1] + "." + splitIP[2] + "." + str(counter)
            os.system("ping " + addr + " -n 1")
            counter +=1

Pinger = PingIP()
Pinger.pingSubnet("192.168.1.1")




