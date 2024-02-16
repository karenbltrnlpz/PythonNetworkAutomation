import time

from netmiko import ConnectHandler

# Connection parameters
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.1',
    'username': 'admin',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
    'verbose': True
}

# Establishing connection
connection = ConnectHandler(**cisco_device)
connection.enable()

# User input for interface
interface = input('Please enter the interface you want to check: ')
output = connection.send_command(f'sh ip int {interface}')
# print(output)

# Check if interface is down
if 'is down, line protocol is down' in output or 'is administratively down, line protocol is down' in output:
    print(f'{interface} is down.')
    # asking the user if they want to enable the interface they chose
    choice = input(f"Do you want to enable {interface}? (yes/no): ")
    # if they chose to enable by entering yes or y
    if choice.lower() in ['yes', 'y']:
        # entering configuration mode
        connection.config_mode()
        # saving commands to send to the device in a list, including no shut
        commands = [f'interface {interface}', 'no shut']
        #using the send_config_set() method to pass in the list of commands to device in config mode
        connection.send_config_set(commands)
        # exiting config mode using exit_config_mode() method
        connection.exit_config_mode()
        # informing the user that the interface was enabled
        print(f'{interface} has been enabled.')
        # pausing the script 4 seconds to give time to the device to update
        time.sleep(4)
        # sending command in privileged mode
        final_output = connection.send_command(f'sh ip int {interface}')
        # showing the user that the interface is up
        print(final_output)
    # if the user decides not to enable the interface
    elif choice.lower() in ['no', 'n']:
        #printing message
        print(f'No changes made to {interface}.')
        # sending command to the device to display the interface status
        nochoice_output = connection.send_command(f'sh ip int {interface}')
        # printing the results of the command
        print(nochoice_output)
# if the interface is already up
elif 'is up, line protocol is up' in output:
    #printing message to user informing so
    print(f'{interface} is up.')
    # sending command to the device to display the interface status
    upint_output = connection.send_command(f'sh ip int {interface}')
    # printing the results of the command
    print(upint_output)
# if the interface is neither down, down, or up, up
else:
    # sending command to the device to display the interface status
    f_output = connection.send_command(f'sh ip int {interface}')
    # printing the results of the command
    print(f_output)

# Disconnecting
print('Closing connection...')
connection.disconnect()

# ''' Sample output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\assignment_enable_interface_up_if_down.py"
# SSH connection established to 10.1.1.1:22
# Interactive SSH session established
# Please enter the interface you want to check: gig1/0/3
# gig1/0/3 is down.
# Do you want to enable gig1/0/3? (yes/no): y
# gig1/0/3 has been enabled.
# GigabitEthernet1/0/3 is up, line protocol is up
#   Inbound  access list is not set
# Closing connection...
#
# Process finished with exit code 0
#
# '''