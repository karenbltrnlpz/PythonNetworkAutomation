from netmiko import ConnectHandler

# opening text file containing the devices' IPs and saving it to a list
with open('devices.txt') as f:
    devices = f.read().splitlines()

for ip in devices:
    # Creating a dictionary with connection parameters
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'admin',
        'password': 'cisco',
        'port': 22, # optional, default 22
        'secret': 'cisco', # optional, default ''. This is the enable password
        'verbose': True # optional, default False
    }
    connection = ConnectHandler(**cisco_device)
    print('Entering the enable mode...')
    connection.enable()

    output = connection.send_command('sh run')

    # finding the name of the device using find_prompt() method
    prompt = connection.find_prompt()
    # getting rid of the hashtag using slicing to keep the name of the router
    # since the hashtag is at the end of the string, we do -1 after the colon to select
    # it and this will return a string without the hashtag
    hostname = prompt[0:-1]
    # print(hostname)

    # creating the backup filename
    from datetime import datetime

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day


    # creating the file name with date stamp
    filename = f'{hostname}_{year}-{month}-{day}_backup.txt'
    print(filename)

    # adding the configuration to the text file
    with open(filename, 'w') as backup_file:
        backup_file.write(output)
        print(f'Backup of {hostname} completed successfully')
        # printing hash signs to see the output clearer
        print('#' * 50)


    print('Closing connection...')
    connection.disconnect()

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_backup_routers.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Entering the enable mode...
# CiscoRouter1_2024-1-4_backup.txt
# Backup of CiscoRouter1 completed successfully
# ##################################################
# Closing connection...
# SSH connection established to 10.1.1.20:22
# Interactive SSH session established
# Entering the enable mode...
# CiscoRouter2_2024-1-4_backup.txt
# Backup of CiscoRouter2 completed successfully
# ##################################################
# Closing connection...
# SSH connection established to 10.1.1.30:22
# Interactive SSH session established
# Entering the enable mode...
# CiscoRouter3_2024-1-4_backup.txt
# Backup of CiscoRouter3 completed successfully
# ##################################################
# Closing connection...
#
# Process finished with exit code 0
# '''