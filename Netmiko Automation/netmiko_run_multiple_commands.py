import time

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

# Using the constructor to create a Netmiko session,
# this is due to the fact that we have already passed in the 'secret' keyword in
# the cisco_device dictionary
connection = ConnectHandler(**cisco_device)

#calling the enable method
print('Entering enable mode...')
connection.enable()

#creating a new loopback interface and a new user
# commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret cisco']
# output = connection.send_config_set(commands)
# cmd = 'ip ssh version 2;access-list 1 permit any;ip domain-name network-automation.io'
# output = connection.send_config_set(cmd.split(';'))

cmd = '''ip ssh version 2
access-list 1 permit any
ip domain-name net-auto.io
'''
output = connection.send_config_set(cmd.split('\n'))
print(output)
print(connection.find_prompt())


connection.send_command('write memory')

print('Closing connection')
connection.disconnect()

# ''' Output using a list of commands:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_run_multiple_commands.py"
# SSH connection established to 10.1.1.1:22
# Interactive SSH session established
# Entering enable mode...
# configure terminal
# Enter configuration commands, one per line.  End with CNTL/Z.
# Switch(config)#int loopback 0
# Switch(config-if)#ip address 1.1.1.1 255.255.255.255
# Switch(config-if)#exit
# Switch(config)#username netmiko secret cisco
# Switch(config)#end
# Switch#
# Switch#
# Closing connection
#
# Process finished with exit code 0'''