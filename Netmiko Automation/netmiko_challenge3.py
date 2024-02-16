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

# getting the prompt
prompt = connection.find_prompt()
# print(prompt)

# remove last char of the prompt (getting the hostname)
hostname = prompt[:-1]

print(f'Hostname is: {hostname}')

print('Closing connection...')
connection.disconnect()

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge3.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Hostname is: CiscoRouter1
# Closing connection...
#
# Process finished with exit code 0
# '''