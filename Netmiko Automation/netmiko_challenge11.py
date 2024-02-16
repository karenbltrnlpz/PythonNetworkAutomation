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
    print(output)

    connection.disconnect()
    print('*' *50)

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge11.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Entering the enable mode...
# Sending command sh ip int br...
# Interface                  IP-Address      OK? Method Status                Protocol
# FastEthernet0/0            10.1.1.10       YES NVRAM  up                    up
# FastEthernet0/1            unassigned      YES NVRAM  administratively down down
# Serial0/0/0                unassigned      YES NVRAM  administratively down down
# Serial0/1/0                unassigned      YES NVRAM  administratively down down
# **************************************************
# SSH connection established to 10.1.1.20:22
# Interactive SSH session established
# Entering the enable mode...
# Sending command sh ip int br...
# Interface                  IP-Address      OK? Method Status                Protocol
# FastEthernet0/0            10.1.1.20       YES NVRAM  up                    up
# FastEthernet0/1            unassigned      YES NVRAM  administratively down down
# Serial0/1/0                unassigned      YES NVRAM  administratively down down
# FastEthernet0/3/0          unassigned      YES NVRAM  up                    up
# **************************************************
# SSH connection established to 10.1.1.30:22
# Interactive SSH session established
# Entering the enable mode...
# Sending command sh ip int br...
# Interface                  IP-Address      OK? Method Status                Protocol
# FastEthernet0/0            10.1.1.30       YES NVRAM  up                    up
# FastEthernet0/1            unassigned      YES NVRAM  up                    up
# Serial0/1/0                unassigned      YES NVRAM  administratively down down
# **************************************************
#
# Process finished with exit code 0
# '''