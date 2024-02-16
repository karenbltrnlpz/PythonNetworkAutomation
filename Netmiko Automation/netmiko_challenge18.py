import time
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


# creating a function called execute_concurrently taking in parameters
# 'device' and 'command' to call on it when I need to run commands
# in  with multithreading
def execute_concurrently(routers, command):
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
        th = threading.Thread(target=execute, args=(cisco_device, command,))
        # adding each thread to the threads list
        threads.append(th)

    # implementing threading
    for th in threads:
        th.start()

    for th in threads:
        th.join()

# creating a function called execute_sequentially taking in parameters
# 'device' and 'command' to call on it when I need to run commands
# in sequential manner
def execute_sequentially(routers, command):
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
        execute(cisco_device, command)



print('Running the script sequentially...')
#measuring the time it takes for the sequential execution
start_time = time.time()
execute_sequentially(routers, 'sh arp')
end_time = time.time()
print(f'Script execution time (SEQUENTIALLY): {end_time - start_time}')

print('$' *70)

print('Running the script concurrently...')
start_time1 = time.time()
execute_concurrently(routers, 'sh arp')
end_time1 = time.time()
print(f'Script execution time (CONCURRENTLY): {end_time1 - start_time1}')


# ''' Output: The following output was with 1 router off, the concurrent execution
# was three seconds faster and the sequential execution.
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge18.py"
# Running the script sequentially...
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Connected to 10.1.1.10
# Entering the enable mode...
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.10               -   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.1              220   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.30             220   001e.4aed.eda0  ARPA   FastEthernet0/0
# Internet  10.1.1.20             220   0024.14eb.ef48  ARPA   FastEthernet0/0
# ****************************************
# Connection timed out for 10.1.1.20. Device may be down or unreachable.
# ****************************************
# SSH connection established to 10.1.1.30:22
# Interactive SSH session established
# Connected to 10.1.1.30
# Entering the enable mode...
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.1              103   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.10             220   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.20             196   0024.14eb.ef48  ARPA   FastEthernet0/0
# Internet  10.1.1.30               -   001e.4aed.eda0  ARPA   FastEthernet0/0
# ****************************************
# Script execution time (SEQUENTIALLY): 13.591761350631714
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Running the script concurrently...
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# SSH connection established to 10.1.1.30:22
# Connected to 10.1.1.10
# Entering the enable mode...
# Interactive SSH session established
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.10               -   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.1              220   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.30             220   001e.4aed.eda0  ARPA   FastEthernet0/0
# Internet  10.1.1.20             220   0024.14eb.ef48  ARPA   FastEthernet0/0
# ****************************************
# Connected to 10.1.1.30
# Entering the enable mode...
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.1              103   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.10             220   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.20             196   0024.14eb.ef48  ARPA   FastEthernet0/0
# Internet  10.1.1.30               -   001e.4aed.eda0  ARPA   FastEthernet0/0
# ****************************************
# Connection timed out for 10.1.1.20. Device may be down or unreachable.
# ****************************************
# Script execution time (CONCURRENTLY): 10.005755186080933
#
# Process finished with exit code 0
#
#
# Output with all of the devices on:
#
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge18.py"
# Running the script sequentially...
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Connected to 10.1.1.10
# Entering the enable mode...
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.10               -   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.1              233   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.30             233   001e.4aed.eda0  ARPA   FastEthernet0/0
# Internet  10.1.1.20               2   0024.14eb.ef48  ARPA   FastEthernet0/0
# ****************************************
# SSH connection established to 10.1.1.20:22
# Interactive SSH session established
# Connected to 10.1.1.20
# Entering the enable mode...
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.1                2   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.10               2   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.20               -   0024.14eb.ef48  ARPA   FastEthernet0/0
# Internet  10.1.1.30               2   001e.4aed.eda0  ARPA   FastEthernet0/0
# ****************************************
# SSH connection established to 10.1.1.30:22
# Interactive SSH session established
# Connected to 10.1.1.30
# Entering the enable mode...
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.1              115   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.10             233   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.20               2   0024.14eb.ef48  ARPA   FastEthernet0/0
# Internet  10.1.1.30               -   001e.4aed.eda0  ARPA   FastEthernet0/0
# ****************************************
# Script execution time (SEQUENTIALLY): 4.580566644668579
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Running the script concurrently...
# SSH connection established to 10.1.1.20:22
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Interactive SSH session established
# SSH connection established to 10.1.1.30:22
# Connected to 10.1.1.20
# Entering the enable mode...
# Connected to 10.1.1.10
# Entering the enable mode...
# Interactive SSH session established
# Sending command...
# Sending command...
# Connected to 10.1.1.30
# Entering the enable mode...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.10               -   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.1              233   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.30             233   001e.4aed.eda0  ARPA   FastEthernet0/0
# Internet  10.1.1.20               2   0024.14eb.ef48  ARPA   FastEthernet0/0
# ****************************************
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.1                2   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.10               2   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.20               -   0024.14eb.ef48  ARPA   FastEthernet0/0
# Internet  10.1.1.30               2   001e.4aed.eda0  ARPA   FastEthernet0/0
# ****************************************
# Sending command...
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  10.1.1.1              115   689c.e271.2f42  ARPA   FastEthernet0/0
# Internet  10.1.1.10             233   0016.4741.8230  ARPA   FastEthernet0/0
# Internet  10.1.1.20               2   0024.14eb.ef48  ARPA   FastEthernet0/0
# Internet  10.1.1.30               -   001e.4aed.eda0  ARPA   FastEthernet0/0
# ****************************************
# Script execution time (CONCURRENTLY): 1.8252124786376953
#
# Process finished with exit code 0
#
# '''