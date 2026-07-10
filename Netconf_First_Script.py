from ncclient import manager
from xml.dom.minidom import parseString

xe = {
    "host": "192.168.0.10",
    "port": "830",
    "username": "admin",
    "password": "admin123",    # Fixed: Added missing comma
    "hostkey_verify": False    # Cleaned up spacing
}

# Connect to the device via NETCONF
netconf = manager.connect(**xe)

print("\nNetconf Connection Established")

# Retrieve the running configuration
running_config = netconf.get_config(source="running")

# Fixed: Corrected the typo 'parsString.' to 'parseString()' and fixed the dot placement
pretty_output = parseString(running_config.xml).toprettyxml()
print(pretty_output)

# Good practice: Close the NETCONF session when done
netconf.close_session()
