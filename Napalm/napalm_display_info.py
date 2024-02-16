from napalm import get_network_driver
import json

# to connect to a network device, we need to import the network driver
# from the napalm library and create a driver object
# specify the device that you are connecting to, in this example Cisco is 'ios'
driver = get_network_driver('ios')
#creating another object
# if you do not want the password hard coded, use the getpass module to retrieve the
# password dynamically
# to pass in the enable password which in this case is cisco
optional_args = {'secret': 'cisco'}
ios = driver('10.1.1.10', 'admin', 'cisco', optional_args=optional_args)
# we open the connection to communicate with the network device
ios.open()

# get_arp_table returns a list of dictionaries for each arp entry of the router
output = ios.get_arp_table()

# iterating through the output list
# for item in output:
#     print(item)

# to display the output in a 'prettier' readeable manner, we can use the json module
# json dumps will return a string and takes  list of dictionaries as an argument and returns a string
# other arguments: sort_keys, sorts the keys, indent to indent information; you do this by specifying the
# number of spaces used for indentation
dump = json.dumps(output, sort_keys=True, indent=4)
# print(dump)

# to save the information in json format to a file
with open('arp.txt', 'w+') as f:
    f.write(dump)

# closing the connection to the device
ios.close()

# '''
# Output: C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe C:\Users\belka\PycharmProjects\NetworkAutomation\Napalm\napalm_display_info.py
# {'interface': 'FastEthernet0/0', 'mac': '00:16:47:41:82:30', 'ip': '10.1.1.10', 'age': -1.0}
# {'interface': 'FastEthernet0/0', 'mac': '68:9C:E2:71:2F:42', 'ip': '10.1.1.1', 'age': 76.0}
# {'interface': 'FastEthernet0/0', 'mac': '00:1E:4A:ED:ED:A0', 'ip': '10.1.1.30', 'age': 77.0}
# {'interface': 'FastEthernet0/0', 'mac': '00:24:14:EB:EF:48', 'ip': '10.1.1.20', 'age': 84.0}
#
# Process finished with exit code 0

# #
# With Json dumps, sorting and indentation:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe C:\Users\belka\PycharmProjects\NetworkAutomation\Napalm\napalm_display_info.py
# {'interface': 'FastEthernet0/0', 'mac': '00:16:47:41:82:30', 'ip': '10.1.1.10', 'age': -1.0}
# {'interface': 'FastEthernet0/0', 'mac': '68:9C:E2:71:2F:42', 'ip': '10.1.1.1', 'age': 86.0}
# {'interface': 'FastEthernet0/0', 'mac': '00:1E:4A:ED:ED:A0', 'ip': '10.1.1.30', 'age': 87.0}
# {'interface': 'FastEthernet0/0', 'mac': '00:24:14:EB:EF:48', 'ip': '10.1.1.20', 'age': 94.0}
# [
#     {
#         "age": -1.0,
#         "interface": "FastEthernet0/0",
#         "ip": "10.1.1.10",
#         "mac": "00:16:47:41:82:30"
#     },
#     {
#         "age": 86.0,
#         "interface": "FastEthernet0/0",
#         "ip": "10.1.1.1",
#         "mac": "68:9C:E2:71:2F:42"
#     },
#     {
#         "age": 87.0,
#         "interface": "FastEthernet0/0",
#         "ip": "10.1.1.30",
#         "mac": "00:1E:4A:ED:ED:A0"
#     },
#     {
#         "age": 94.0,
#         "interface": "FastEthernet0/0",
#         "ip": "10.1.1.20",
#         "mac": "00:24:14:EB:EF:48"
#     }
# ]
#
# Process finished with exit code 0
#
# # '''