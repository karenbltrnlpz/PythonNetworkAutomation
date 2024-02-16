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

#entering global configuration mode
print('Entering global configuration mode...')
connection.config_mode()

# executing commands
print('Creating a new user')
newuser = connection.send_command('username admin2 secret cisco')

print('Exiting config mode')
connection.exit_config_mode()

print('Saving the configuration...')
connection.send_command('write')

print(f'Closing connection from {cisco_device["host"]} ...')
connection.disconnect()

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge7.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Entering the enable mode...
# Entering global configuration mode...
# Creating a new user
# Exiting config mode
# Saving the configuration...
# Closing connection from 10.1.1.10 ...
#
# Process finished with exit code 0
#
# '''