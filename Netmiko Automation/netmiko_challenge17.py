from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException
import threading

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

# initiating threads list
threads = list()

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

    cmd = 'sh arp'
    # sending the sh arp command on each router via multithreading
    th = threading.Thread(target=execute, args=(cisco_device, cmd,))
    # adding each thread to the threads list
    threads.append(th)

# implementing threading
for th in threads:
    th.start()

for th in threads:
    th.join()

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge17.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# SSH connection established to 10.1.1.30:22
# Connected to 10.1.1.10
# Entering the enable mode...
# Interactive SSH session established
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.10               -   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.1              198   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.30             198   001e.4aed.eda0  ARPA   FastEthernet0/0
# Internet  10.1.1.20             198   0024.14eb.ef48  ARPA   FastEthernet0/0
# ****************************************
# Connected to 10.1.1.30
# Entering the enable mode...
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.1               80   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.10             198   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.20             174   0024.14eb.ef48  ARPA   FastEthernet0/0
# Internet  10.1.1.30               -   001e.4aed.eda0  ARPA   FastEthernet0/0
# ****************************************
# Connection timed out for 10.1.1.20. Device may be down or unreachable.
# ****************************************
#
# Process finished with exit code 0
#
# '''