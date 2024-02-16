import myparamiko as mp
from netmiko import ConnectHandler

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
#calling the enable method
print('Entering enable mode...')
connection.enable()

print('Sending configs from file...')
output = connection.send_config_from_file('ospf.txt')
print(output)

print('Closing connection')
connection.disconnect()

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_run_commands_from_file.py"
# SSH connection established to 10.1.1.1:22
# Interactive SSH session established
# Entering enable mode...
# Sending configs from file...
# configure terminal
# Enter configuration commands, one per line.  End with CNTL/Z.
# Switch(config)#router ospf 1
# Switch(config-router)#net 0.0.0.0 0.0.0.0 area 0
# Switch(config-router)#distance 60
# Switch(config-router)#default-information originate
# Switch(config-router)#end
# Switch#
# Closing connection
#
# Process finished with exit code 0
# '''