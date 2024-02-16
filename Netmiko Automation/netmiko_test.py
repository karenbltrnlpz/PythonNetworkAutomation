from netmiko import Netmiko


''' Netmiko supports major networking devices. This library runs on top
os Paramiko. It is easier to code in, less line of code are required
to get a similar output compared to paramiko and less error prone.
However if you need to interface with a device that is not supported by 
Netmiko library, you can use Paramiko. Both Paramiko and Netmiko are libraries
that are used for devices that don't have an API to interface with. '''

# device = {
#     'host': '10.1.1.1',
#     'port': '22',
#     'username': 'admin',
#     'password': 'cisco',
#     'device_type': 'cisco_ios' # specifying the supported platform
# }
#
# # establishing a connection
# connection = Netmiko(**device)
# output = connection.send_command('sh ip int br')
# print(output)
#
# print('Closing connection')
# connection.disconnect()

# second method to connect to a device using Netmiko
from netmiko import ConnectHandler

# Creating a dictionary with connection parameters
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.1',
    'username': 'admin',
    'password': 'cisco',
    'port': 22, # optional, default 22
    'secret': 'cisco', # optional, default ''
    'verbose': True # optional, default False
}

# Using the constructor to create a Netmiko session
connection = ConnectHandler(**cisco_device)

output = connection.send_command('sh ip int br')
print(output)

print('Closing connection')
connection.disconnect()