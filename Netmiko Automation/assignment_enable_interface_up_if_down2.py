import time
from netmiko import ConnectHandler

# Connection parameters
cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.1',
    'username': 'admin',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
    'verbose': True
}
# Establishing connection
net_connect = ConnectHandler(**cisco_device)
prompter = net_connect.find_prompt()
if '>' in prompter:
    net_connect.enable()

interface = input('Enter the interface you want to enable:')
output = net_connect.send_command('sh ip interface ' + interface)

if 'invalid input detected' in output:
    print('You entered an invalid interface')
else:
    # selecting/saving the first line of the output
    first_line = output.splitlines()[0]
    if not 'up' in first_line:
        print('The interface is down. Enabling the interface...')
        commands = ['interface ' + interface, 'no shut', 'exit' ]
        output = net_connect.send_config_set(commands)
        print(output)
        print('#' * 40)
        print('The interface has been enabled')
    else:
        print('Interface ' + interface + ' is already enabled')


# Disconnecting
print('Closing connection...')
net_connect.disconnect()

# ''' Sample output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\assignment_enable_interface_up_if_down2.py"
# SSH connection established to 10.1.1.1:22
# Interactive SSH session established
# Enter the interface you want to enable:gig1/0/3
# The interface is down. Enabling the interface...
# configure terminal
# Enter configuration commands, one per line.  End with CNTL/Z.
# Switch(config)#interface gig1/0/3
# Switch(config-if)#no shut
# Switch(config-if)#exit
# Switch(config)#end
# Switch#
# ########################################
# The interface has been enabled
# Closing connection...
#
# Process finished with exit code 0
# '''