from netmiko import ConnectHandler


routers = ['10.1.1.10', '10.1.1.20', '10.1.1.30']

# creating a function called execute taking in parameters
# 'device' and 'command'

def execute(device, command):
    connection = ConnectHandler(**device)
    print('Entering the enable mode...')
    connection.enable()
    print('Sending command...')
    output = connection.send_command(command)
    print(output)
    connection.disconnect()
    print('*' * 40)

# looping through the routers list
for router in routers:

    # Creating a dictionary with connection parameters
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': router,
        'username': 'admin',
        'password': 'cisco',
        'port': 22, # optional, default 22
        'secret': 'cisco', # optional, default ''. This is the enable password
        'verbose': True # optional, default False
    }

    # sending the sh arp command on each router sequentially
    execute(cisco_device, 'sh arp')

# Creating a dictionary with connection parameters for linux
# linux = {
#     'device_type': 'linux',
#     'host': '192.168.0.90',
#     'username': 'admin',
#     'password': 'cisco',
#     'port': 22, # optional, default 22
#     'secret': 'cisco', # optional, default ''. This is the enable password
#     'verbose': True # optional, default False
# }
# execute(linux, 'ip addr')

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge15.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Entering the enable mode...
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.10               -   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.1              164   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.30             164   001e.4aed.eda0  ARPA   FastEthernet0/0
# Internet  10.1.1.20             164   0024.14eb.ef48  ARPA   FastEthernet0/0
# ****************************************
# SSH connection established to 10.1.1.20:22
# Interactive SSH session established
# Entering the enable mode...
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.1               96   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.10             164   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.20               -   0024.14eb.ef48  ARPA   FastEthernet0/0
# Internet  10.1.1.30             140   001e.4aed.eda0  ARPA   FastEthernet0/0
# ****************************************
# SSH connection established to 10.1.1.30:22
# Interactive SSH session established
# Entering the enable mode...
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.1               47   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.10             164   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.20             140   0024.14eb.ef48  ARPA   FastEthernet0/0
# Internet  10.1.1.30               -   001e.4aed.eda0  ARPA   FastEthernet0/0
# ****************************************
#
# Process finished with exit code 0
# '''