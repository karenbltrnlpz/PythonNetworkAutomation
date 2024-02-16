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
output_shipintbr = connection.send_command('sh ip int br')
output_shrun = connection.send_command('sh run')

#getting the hostname
prompt = connection.find_prompt()
print(prompt)
hostname = prompt[:-1]

#making the file names for each command
filename1 = f'{hostname}-interfaces.txt'
filename2 = f'{hostname}-running-config.txt'

#saving the command outputs to their files
with open(filename1, 'w') as f:
    f.write(output_shipintbr)

with open(filename2, 'w') as f:
    f.write(output_shrun)

print('Closing connection...')
connection.disconnect()

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge5.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Entering the enable mode...
# CiscoRouter1#
# Closing connection...
#
# Process finished with exit code 0
# '''