from ncclient import manager
from xml.dom.minidom import parseString

device = {
    'host': '10.255.1.10',
    'port': '830',
    'username': 'admin',
    "password": 'admin123',
    "hostkey_verify": False,   
}

netconf = manager.connect(**device)
print('Connection Established Successfully')

# Gathering inputs
interface_details = {
    'int_name': input('Enter your Interface name: '),
    'int_desc': input('Enter Interface Description: '),
    'int_ip': input('Enter Interface IP: '),
    'int_mask': input('Enter Subnet: ')
}

# XML Payload Template using standard IETF models
interface_template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{name}</name>
            <description>{desc}</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
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


interface_payload = interface_template.format(
    name=interface_details['int_name'],
    desc=interface_details['int_desc'],
    ip=interface_details['int_ip'],
    mask=interface_details['int_mask']
)

# Send edit_config request
interface_config = netconf.edit_config(config=interface_payload, target="running")

# Fixed: Corrected parseString and toprettyxml typos
pretty_output = parseString(interface_config.xml).toprettyxml()
print(pretty_output)

netconf.close_session()
