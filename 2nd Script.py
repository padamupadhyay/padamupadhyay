from telnetlib import Telnet
import time  # Imported time for small delays

R1 = "172.19.0.5"
username = "admin"
password = "admin123"

# Establish connection
tn = Telnet(R1)
time.sleep(1)  # Give the router a second to prompt for username

# Send Login Credentials
tn.write(username.encode("ascii") + b"\n")
time.sleep(1)
tn.write(password.encode("ascii") + b"\n")
time.sleep(1)

print("Connection Successful")

# Multi-line commands string (Fixed commands and added subnet masks)
commands = """
configure terminal
interface loopback 10
ip address 192.168.19.1 255.255.255.255
description loopback 10
no shutdown
interface loopback 20
ip address 192.168.19.2 255.255.255.255
description loopback 20
no shutdown
end
exit
"""

# Send all commands
tn.write(commands.encode("ascii") + b"\n")
time.sleep(2)  # Give the router time to process everything

# Read and print the output
print(tn.read_all().decode("ascii"))
