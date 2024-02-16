from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException

# creating a function called execute taking in parameters
# 'device' and 'command'

def execute(device, command):
    try:
        connection = ConnectHandler(**device)
        print(f'Connected to {device["host"]}')
        print('Entering the enable mode...')
        connection.enable()
        print('Sending command...')
        output = connection.send_command(command)
        print(output)
        connection.disconnect()
    except NetmikoTimeoutException:
        print(f"Connection timed out for {device['host']}. Device may be down or unreachable.")
    except Exception as e:
        print(f"An error occurred with {device['host']}: {e}")
    finally:
        # print the following if no error was encountered
        print('*' * 40)

# saving router IPs in a list
routers = ['10.1.1.10', '10.1.1.20', '10.1.1.30']

# looping through the routers list
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

    # sending the sh arp command on each router sequentially
    execute(cisco_device, 'sh arp')



# ''' Output:
#
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge16.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Connected to 10.1.1.10
# Entering the enable mode...
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.10               -   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.1              179   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.30             179   001e.4aed.eda0  ARPA   FastEthernet0/0
# Internet  10.1.1.20             179   0024.14eb.ef48  ARPA   FastEthernet0/0
# ****************************************
# Connection timed out for 10.1.1.20. Device may be down or unreachable.
# ****************************************
# SSH connection established to 10.1.1.30:22
# Interactive SSH session established
# Connected to 10.1.1.30
# Entering the enable mode...
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.1               62   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.10             179   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.20             155   0024.14eb.ef48  ARPA   FastEthernet0/0
# Internet  10.1.1.30               -   001e.4aed.eda0  ARPA   FastEthernet0/0
# ****************************************
#
# Process finished with exit code 0
#
# '''