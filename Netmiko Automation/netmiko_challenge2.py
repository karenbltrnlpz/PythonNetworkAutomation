from netmiko import ConnectHandler

with open('challenge2_device.txt') as f:
    content_list = f.read().split(':')
    # print(content_list) # ['10.1.1.10', '22', 'admin', 'cisco', 'cisco']

# Creating a dictionary with connection parameters
cisco_device = {
    'device_type': 'cisco_ios',
    'host': content_list[0],
    'username': content_list[2],
    'password': content_list[3],
    'port': content_list[1], # optional, default 22
    'secret': content_list[4], # optional, default ''. This is the enable password
    'verbose': True # optional, default False
}
connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')
connection.enable()

output = connection.send_command('sh arp')
print(output)


print(f'Closing connection from {cisco_device["host"]}')
connection.disconnect()

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge2.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Entering the enable mode...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.10               -   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.1               21   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.30              21   001e.4aed.eda0  ARPA   FastEthernet0/0
# Internet  10.1.1.20              21   0024.14eb.ef48  ARPA   FastEthernet0/0
# Closing connection from 10.1.1.10
#netmio
# Process finished with exit code 0
# '''