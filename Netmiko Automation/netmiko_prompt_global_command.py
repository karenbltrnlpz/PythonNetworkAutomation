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
prompt = connection.find_prompt()
if '>' in prompt:
    # sending enable command to enter privilege exe mode
    connection.enable()

output = connection.send_command('sh run')
print(output)

if not connection.check_config_mode():
    print(connection.check_config_mode())
    print(prompt)
    connection.config_mode()

print(connection.check_config_mode())
prompt = connection.find_prompt()
print(prompt)

# running command under global config mode, add 'do' in front
# checking to see if the user we want to add is already a user
find_user = connection.send_command('do sh run | i user')
print(find_user)
time.sleep(3) # giving it time for the user to read the output of the
# 'do sh run | i user' command

# if the user has not been created
if not 'u3' in find_user:
    # sending a command to the cisco device to create a new user
    # without having to enter the '\n' because the send_command takes care
    # of this for us
    connection.send_command('username u3 secret cisco')

# checking the users again to see if the new user has been added.
find_user = connection.send_command('do sh run | i user')
print(find_user)

# exiting config mode
connection.exit_config_mode()
# checking if we are still in global config mode, if not, this should
# return False.
print(connection.check_config_mode())

print('Closing connection')
connection.disconnect()