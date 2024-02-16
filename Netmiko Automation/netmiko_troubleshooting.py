import time

from netmiko import ConnectHandler
import logging

# specifying which file to add logs to
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger('netmiko')

# Creating a dictionary with connection parameters
cisco_switch = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.1',
    'username': 'admin',
    'password': 'cisco',
    'port': 22, # optional, default 22
    'secret': 'cisco', # optional, default ''
    'verbose': True # optional, default False
}

# Using the constructor to create a Netmiko session,
# this is due to the fact that we have already passed in the 'secret' keyword in
# the cisco_device dictionary
connection = ConnectHandler(**cisco_switch)
# output = connection.send_command('sh ver')
# print(output)

connection.write_channel('show ver\n')
time.sleep(2)
output = connection.read_channel()
print(output)

print('Closing connection')
connection.disconnect()