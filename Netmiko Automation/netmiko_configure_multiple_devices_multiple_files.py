from netmiko import ConnectHandler

# opening devices text file
with open('devices.txt') as f:
    # reading the lines and adding them into a list
    devices = f.read().splitlines()

device_list = []

# iterate over the devices list which has our devices IP addresses
for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'admin',
        'password': 'cisco',
        'port': 22, # optional, default 22
        'secret': 'cisco', # optional, default ''
        'verbose': True # optional, default False
        }
    # appending the cisco device information to the empty list device_list
    device_list.append(cisco_device)

# printing the device list
# print(device_list)
# to stop the script at this point to see the contents of device_list
# exit(1)

# iterating through the device_list that contains the list of dictionaries
# with information of each router
for device in device_list:
    connection = ConnectHandler(**device)

    print(f"Entering enable mode on device {device}: ")
    connection.enable()

    # prompting the user for a configuration file
    file = input(f'Enter a configuration file (use a valid path) for {device["host"]}')

    print(f'Running commands from file: {file} on device: {device["host"]}:')
    # sending commands from the config file chosen by the user saving it to output
    output = connection.send_config_from_file(file)
    # printing the output
    print(output)

    print(f'Closing connection to {device["host"]}')
    connection.disconnect()

    # separating the output of each device using hashtags
    print('#' * 30)

''' Output of the script:
C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_configure_multiple_devices_multiple_files.py" 
SSH connection established to 10.1.1.10:22
Interactive SSH session established
Entering enable mode on device {'device_type': 'cisco_ios', 'host': '10.1.1.10', 'username': 'admin', 'password': 'cisco', 'port': 22, 'secret': 'cisco', 'verbose': True}: 
Enter a configuration file (use a valid path) for 10.1.1.10CiscoRouter1.txt
Running commands from file: CiscoRouter1.txt on device: 10.1.1.10
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
CiscoRouter1(config)#int loopback 1
CiscoRouter1(config-if)#ip address 1.1.1.1 255.255.255.255
CiscoRouter1(config-if)#exit
CiscoRouter1(config)#router ospf 1
CiscoRouter1(config-router)#network 0.0.0.0 0.0.0.0 area 0
CiscoRouter1(config-router)#distance 60
CiscoRouter1(config-router)#default-information originate
CiscoRouter1(config-router)#end
CiscoRouter1#
Closing connection to 10.1.1.10
##############################
SSH connection established to 10.1.1.20:22
Interactive SSH session established
Entering enable mode on device {'device_type': 'cisco_ios', 'host': '10.1.1.20', 'username': 'admin', 'password': 'cisco', 'port': 22, 'secret': 'cisco', 'verbose': True}: 
Enter a configuration file (use a valid path) for 10.1.1.20CiscoRouter2.txt
Running commands from file: CiscoRouter2.txt on device: 10.1.1.20
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
CiscoRouter2(config)#int loopback 2
CiscoRouter2(config-if)#ip address 2.2.2.2 255.255.255.255
CiscoRouter2(config-if)#exit
CiscoRouter2(config)#router ospf 1
CiscoRouter2(config-router)#network 0.0.0.0 0.0.0.0 area 0
CiscoRouter2(config-router)#distance 60
CiscoRouter2(config-router)#default-information originate
CiscoRouter2(config-router)#end
CiscoRouter2#
Closing connection to 10.1.1.20
##############################
SSH connection established to 10.1.1.30:22
Interactive SSH session established
Entering enable mode on device {'device_type': 'cisco_ios', 'host': '10.1.1.30', 'username': 'admin', 'password': 'cisco', 'port': 22, 'secret': 'cisco', 'verbose': True}: 
Enter a configuration file (use a valid path) for 10.1.1.30CiscoRouter3.txt
Running commands from file: CiscoRouter3.txt on device: 10.1.1.30
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
CiscoRouter3(config)#int loopback 3
CiscoRouter3(config-if)#ip address 3.3.3.3 255.255.255.255
CiscoRouter3(config-if)#exit
CiscoRouter3(config)#router ospf 1
CiscoRouter3(config-router)#network 0.0.0.0 0.0.0.0 area 0
CiscoRouter3(config-router)#distance 60
CiscoRouter3(config-router)#default-information originate
CiscoRouter3(config-router)#end
CiscoRouter3#
Closing connection to 10.1.1.30
##############################

Process finished with exit code 0

'''