from netmiko import ConnectHandler


# Creating a dictionary with connection parameters
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.10',
    'username': 'admin',
    'password': 'cisco',
    'port': 22, # optional, default 22
    'secret': 'cisco', # optional, default ''. This is the enable password
    'verbose': True # optional, default False
}
connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')
connection.enable()

output = connection.send_command('sh arp')
print(output)


print('Closing connection...')
connection.disconnect()

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge1.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Entering the enable mode...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.10               -   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.1                9   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.30               9   001e.4aed.eda0  ARPA   FastEthernet0/0
# Internet  10.1.1.20               9   0024.14eb.ef48  ARPA   FastEthernet0/0
# Closing connection...
#
# Process finished with exit code 0
#
# '''