from netmiko import ConnectHandler

# saving the IPs of each router in a list
routers = ['10.1.1.10', '10.1.1.20', '10.1.1.30']

#looping through the IP's of each router
for router in routers:
    # Creating a dictionary with connection parameters
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': router,
        'username': 'admin',
        'password': 'cisco',
        'port': 22, # optional, default 22
        'secret': 'cisco', # optional, default ''. This is the enable password
        'verbose': True # optional, default False
    }
    connection = ConnectHandler(**cisco_device)
    print('Entering the enable mode...')
    connection.enable()

    print('Sending command sh ip int br...')
    output = connection.send_command('sh ip int br')
    # print(output)

    # getting hostname from each router
    prompt = connection.find_prompt()
    hostname = prompt[:-1]

    #getting the current date
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    filename = f'{hostname}_{year}_{month}_{day}-interfaces.txt'
    with open(filename, 'w+') as f:
        print(f'Saving output to file: {filename}')
        f.write(output)

    connection.disconnect()
    print('*' *50)

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge12.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Entering the enable mode...
# Sending command sh ip int br...
# Saving output to file: CiscoRouter1_2024_1_9-interfaces.txt
# **************************************************
# SSH connection established to 10.1.1.20:22
# Interactive SSH session established
# Entering the enable mode...
# Sending command sh ip int br...
# Saving output to file: CiscoRouter2_2024_1_9-interfaces.txt
# **************************************************
# SSH connection established to 10.1.1.30:22
# Interactive SSH session established
# Entering the enable mode...
# Sending command sh ip int br...
# Saving output to file: CiscoRouter3_2024_1_9-interfaces.txt
# **************************************************
#
# Process finished with exit code 0
#
# '''