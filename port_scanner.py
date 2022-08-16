import pyfiglet
import sys
import socket
from datetime import datetime

#Print a pretty headline, formatted by the pyfiglet module
app_banner = pyfiglet.figlet_format("PORT SCANNER")
print(app_banner)

#Save user input in variable
target = input(str("Target IP: "))

#Display options in formatted banner
print("-" * 50)
print("There are 4 options: \n")
print("[1] Well-known ports (1023)")
print("[2] Registered ports (49151)")
print("[3] All ports (65535)")
print("[4] Custom number (your choice)")
print("-" * 50)

#User enters an option and input is saved
user_option = input("Option Number(1/2/3/4): ")

#Set port_range variable depending on user_option
print("-" * 50)
if(user_option == "1"):
    print("Scanning 1023 ports...")
    port_range = 1023
elif(user_option == "2"):
    print("Scanning 49151 ports...")
    port_range = 49151
elif(user_option == "3"):
    print("Scanning 65535 ports...")
    port_range = 65535
elif(user_option == "4"):
    port_range = input("Maximum number of ports to scan: ")
    print("Scanning {} ports...".format(port_range))
else:
    print("Not a valid option. Enter 1, 2, 3, or 4")
    sys.exit()

#Informational text
print("Scanning target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

#Scan from ports 1 - {port_range} and return open ports (ports that we can connect to)
try:

    for port in range(1,int(port_range)): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target, port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting...")
    sys.exit()

except socket.error:
    print("\n Host not responding...")
    sys.exit()


