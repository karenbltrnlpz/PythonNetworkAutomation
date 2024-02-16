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

print('Sending commands from file...')
# the send_config_from_file method takes in the name of the file that
# has the commands and enters config mode and sends the commands line by line
output = connection.send_config_from_file('rip-config_router1.txt')
print(output)

print(f'Closing connection from {cisco_device["host"]} ...')
connection.disconnect()

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge10.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Entering the enable mode...
# Sending commands from file...
# configure terminal
# Enter configuration commands, one per line.  End with CNTL/Z.
# CiscoRouter1(config)#ip ssh version 2
# CiscoRouter1(config)#router rip
# CiscoRouter1(config-router)#version 2
# CiscoRouter1(config-router)#net 10.0.0.0
# CiscoRouter1(config-router)#net 192.168.0.0
# CiscoRouter1(config-router)#distance 150
# CiscoRouter1(config-router)#redistribute ospf 1
# CiscoRouter1(config-router)#end
# CiscoRouter1#
# Closing connection from 10.1.1.10 ...
#
# Process finished with exit code 0
# '''