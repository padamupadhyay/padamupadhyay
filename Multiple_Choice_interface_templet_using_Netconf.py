from ncclient import manager
from xml.dom.minidom import parseString

et = {
    'host': '10.120.2.13',
    'port': '830',
    'username': 'cisco',
    'password': 'admin123',
    'hostkey_verify': False, 
}


common_int_template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{name}</name>
            <description>{desc}</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:{type}</type>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>{ip}</ip>
                    <netmask>{mask}</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
"""

print("Attempting Connection with the Device via NETCONF...")
netconf = manager.connect(**et)

int_count = int(input("How many interfaces would you like to configure? "))

for interface in range(0, int_count):
    print(f"\n--- Configuring Interface {interface + 1} of {int_count} ---")
    int_type_choice = input("1. Physical Interface\n2. Logical Interface\nPlease Make a Choice (1/2): ")

    if int_type_choice == "1":
        # Fixed: Converted from dictionary style to variable assignment
        int_name = input('Enter your Interface name (e.g., GigabitEthernet1): ')
        int_desc = input('Enter Interface Description: ')
        int_ip = input('Enter Interface IP: ')
        int_mask = input('Enter Subnet Mask: ')
        int_type = "ethernetCsmacd"

        interface_payload = common_int_template.format(
            name=int_name,
            desc=int_desc,
            type=int_type,
            ip=int_ip,
            mask=int_mask
        )

        physical_int_config = netconf.edit_config(config=interface_payload, target="running")
        pretty_output = parseString(physical_int_config.xml).toprettyxml()
        print(pretty_output)

    elif int_type_choice == "2":
        int_name = input('Enter your Interface name (e.g., Loopback10): ')
        int_desc = input('Enter Interface Description: ')
        int_ip = input('Enter Interface IP: ')
        int_mask = input('Enter Subnet Mask: ')
        int_type = "softwareLoopback"  # Fixed: Proper IANA type for Loopbacks

        interface_payload = common_int_template.format(
            name=int_name,
            desc=int_desc,
            type=int_type,
            ip=int_ip,
            mask=int_mask
        )

        logical_int_config = netconf.edit_config(config=interface_payload, target="running")
        pretty_output = parseString(logical_int_config.xml).toprettyxml()
        print(pretty_output)

    else:
        print("Invalid Input Detected. Skipping this interface iteration.")


netconf.close_session()
print("\nSession closed successfully.")
