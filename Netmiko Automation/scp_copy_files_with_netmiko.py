from netmiko import ConnectHandler
from netmiko import file_transfer

# Creating a dictionary with connection parameters
cisco_switch = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.1',
    'username': 'admin1',
    'password': 'cisco',
    'port': 22, # optional, default 22
    'secret': 'cisco', # optional, default ''
    'verbose': True # optional, default False
}

connection = ConnectHandler(**cisco_switch)

transfer_output = file_transfer(connection, source_file='ospf.txt', dest_file='ospf1.txt', file_system='flash:',
                                direction='put', overwrite_file=True)

print(transfer_output)

connection.disconnect()

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\scp_copy_files_with_netmiko.py"
# SSH connection established to 10.1.1.1:22
# Interactive SSH session established
# {'file_exists': True, 'file_transferred': True, 'file_verified': True}
#
# Process finished with exit code 0
# '''