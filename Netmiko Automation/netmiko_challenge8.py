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

# executing commands
print('Creating an access list...')
commands = ['access-list 101 permit tcp any any eq 80', 'access-list 101 permit tcp any any eq 443',
'access-list 101 deny ip any any']
# the send_config_set command takes care of entering the global config mode
acl = connection.send_config_set(commands)

# print('Exiting config mode')
# connection.exit_config_mode()

sh_acl = connection.send_command('sh access-lists')
print(sh_acl)

print(f'Closing connection from {cisco_device["host"]} ...')
connection.disconnect()

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge8.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Entering the enable mode...
# Creating an access list...
# Exiting config mode
# Extended IP access list 101
#     10 permit tcp any any eq www
#     20 permit tcp any any eq 443
#     30 deny ip any any
# Closing connection from 10.1.1.10 ...
#
# Process finished with exit code 0
# '''