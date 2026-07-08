from netmiko import ConnectHandler

R1 = {
    "device_type" : "cisco_ios"
    "ip" : "10.250.0.4"
    "username" : "admin"
    "password" : "addmin@123"
}

ssh_connection = ConnectHandler(**R1)

print("SSH to the device is successfull")

commands = ["interface loopback 10" , "ip address 172.16.299.1" , "description loopback" , "no shutdown"]

loopback = ssh_connection.send_command(commands)
print(loopback)

int_brief = ssh_connection.send_command("show ip int brief")

print(int_brief)

