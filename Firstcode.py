import time
import telnetlib

router = "10.250.0.8"
username = "admin"  # Fixed: changed from 'usename'
password = "Password"

tn = telnetlib.Telnet(router)

# Read until the login prompts appear to keep things stable
tn.read_until(b"Username: ")
tn.write(username.encode("ascii") + b"\n")

tn.read_until(b"Password: ")
tn.write(password.encode("ascii") + b"\n")

print("Telnet successful")
time.sleep(1)  # Brief pause to let the router prompt load

# Configuration commands
tn.write(b"configure terminal\n")
tn.write(b"interface loopback 10\n")
tn.write(b"ip address 10.1.1.1 255.255.255.255\n")  # Fixed: Added the subnet mask
tn.write(b"description Loopback interface\n")      # Fixed: Typo in 'Loopback'
tn.write(b"no shutdown\n")
tn.write(b"end\n")
tn.write(b"exit\n")  # Crucial: Closes the session so read_all() knows when to stop

# Read and print the output
print(tn.read_all().decode("ascii"))  # Fixed: Typo changed from 'acsii'
