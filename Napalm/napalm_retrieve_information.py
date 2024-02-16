import json

import napalm
from napalm import get_network_driver

# to connect to a network device, we need to import the network driver
# from the napalm library and create a driver object
# specify the device that you are connecting to, in this example Cisco is 'ios'
driver = get_network_driver('ios')
#creating another object
# if you do not want the password hard coded, use the getpass module to retrieve the
# password dynamically
# to pass in the enable password which in this case is cisco
optional_args = {'secret': 'cisco'}
ios = driver('10.1.1.20', 'admin', 'cisco', optional_args=optional_args)
# we open the connection to communicate with the network device
ios.open()

#getting general facts about the device
output = ios.get_facts()
#convert the output to a string via json
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

# retrieving the arp table
output1 = ios.get_arp_table()
#convert the output to a string via json
dump1 = json.dumps(output1, sort_keys=True, indent=4)
print(dump1)

# getting information about the device's interfaces
output3 = ios.get_interfaces()
#convert the output to a string via json
dump2 = json.dumps(output3, sort_keys=True, indent=4)
print(dump2)

# getting granular information about the device's interfaces
output4 = ios.get_interfaces_counters()
#convert the output to a string via json
dump3 = json.dumps(output4, sort_keys=True, indent=4)
print(dump3)

# getting granular information about the device's interfaces such as if IPs were
# configured
output5 = ios.get_interfaces_ip()
#convert the output to a string via json
dump4 = json.dumps(output5, sort_keys=True, indent=4)
print(dump4)

# getting information about the BGP neighbors
output6 = ios.get_bgp_neighbors()
#convert the output to a string via json
dump5 = json.dumps(output6, sort_keys=True, indent=4)
print(dump5)


# closing the connection to the device
ios.close()

# ''' Output for CiscoRouter3:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe C:\Users\belka\PycharmProjects\NetworkAutomation\Napalm\napalm_retrieve_information.py
# {
#     "fqdn": "CiscoRouter3.domain.com",
#     "hostname": "CiscoRouter3",
#     "interface_list": [
#         "FastEthernet0/0",
#         "FastEthernet0/1",
#         "Serial0/1/0"
#     ],
#     "model": "2811",
#     "os_version": "2800 Software (C2800NM-IPBASEK9-M), Version 15.1(4)M12a, RELEASE SOFTWARE (fc1)",
#     "serial_number": "FTX1147A1JJ",
#     "uptime": 1063140.0,
#     "vendor": "Cisco"
# }
# [
#     {
#         "age": 114.0,
#         "interface": "FastEthernet0/0",
#         "ip": "10.1.1.1",
#         "mac": "68:9C:E2:71:2F:42"
#     },
#     {
#         "age": 29.0,
#         "interface": "FastEthernet0/0",
#         "ip": "10.1.1.10",
#         "mac": "00:16:47:41:82:30"
#     },
#     {
#         "age": 69.0,
#         "interface": "FastEthernet0/0",
#         "ip": "10.1.1.20",
#         "mac": "00:24:14:EB:EF:48"
#     },
#     {
#         "age": -1.0,
#         "interface": "FastEthernet0/0",
#         "ip": "10.1.1.30",
#         "mac": "00:1E:4A:ED:ED:A0"
#     }
# ]
# {
#     "FastEthernet0/0": {
#         "description": "connection to Switch gig1/0/9",
#         "is_enabled": true,
#         "is_up": true,
#         "last_flapped": -1.0,
#         "mac_address": "00:1E:4A:ED:ED:A0",
#         "mtu": 1500,
#         "speed": 100.0
#     },
#     "FastEthernet0/1": {
#         "description": "connection to Switch f/0/3/0",
#         "is_enabled": true,
#         "is_up": true,
#         "last_flapped": -1.0,
#         "mac_address": "00:1E:4A:ED:ED:A1",
#         "mtu": 1500,
#         "speed": 100.0
#     },
#     "Serial0/1/0": {
#         "description": "",
#         "is_enabled": false,
#         "is_up": false,
#         "last_flapped": -1.0,
#         "mac_address": "",
#         "mtu": 1500,
#         "speed": 1.536
#     }
# }
# {
#     "FastEthernet0/0": {
#         "rx_broadcast_packets": 355012,
#         "rx_discards": 0,
#         "rx_errors": 0,
#         "rx_multicast_packets": 0,
#         "rx_octets": 42978273,
#         "rx_unicast_packets": 357469,
#         "tx_broadcast_packets": -1,
#         "tx_discards": 0,
#         "tx_errors": 0,
#         "tx_multicast_packets": -1,
#         "tx_octets": 25819137,
#         "tx_unicast_packets": 245738
#     },
#     "FastEthernet0/1": {
#         "rx_broadcast_packets": 10294,
#         "rx_discards": 0,
#         "rx_errors": 0,
#         "rx_multicast_packets": 0,
#         "rx_octets": 3870544,
#         "rx_unicast_packets": 10294,
#         "tx_broadcast_packets": -1,
#         "tx_discards": 0,
#         "tx_errors": 0,
#         "tx_multicast_packets": -1,
#         "tx_octets": 8008572,
#         "tx_unicast_packets": 74520
#     },
#     "Serial0/1/0": {
#         "rx_broadcast_packets": 0,
#         "rx_discards": 0,
#         "rx_errors": 0,
#         "rx_multicast_packets": 0,
#         "rx_octets": 0,
#         "rx_unicast_packets": 0,
#         "tx_broadcast_packets": -1,
#         "tx_discards": 0,
#         "tx_errors": 0,
#         "tx_multicast_packets": -1,
#         "tx_octets": 0,
#         "tx_unicast_packets": 0
#     }
# }
# {
#     "FastEthernet0/0": {
#         "ipv4": {
#             "10.1.1.30": {
#                 "prefix_length": 24
#             }
#         }
#     }
# }
# {
#     "global": {
#         "peers": {
#             "10.1.1.10": {
#                 "address_family": {
#                     "ipv4 unicast": {
#                         "accepted_prefixes": -1,
#                         "received_prefixes": -1,
#                         "sent_prefixes": -1
#                     }
#                 },
#                 "description": "",
#                 "is_enabled": true,
#                 "is_up": false,
#                 "local_as": 65003,
#                 "remote_as": 65001,
#                 "remote_id": "0.0.0.0",
#                 "uptime": -1
#             },
#             "10.1.1.20": {
#                 "address_family": {
#                     "ipv4 unicast": {
#                         "accepted_prefixes": 0,
#                         "received_prefixes": 0,
#                         "sent_prefixes": 0
#                     }
#                 },
#                 "description": "",
#                 "is_enabled": true,
#                 "is_up": true,
#                 "local_as": 65003,
#                 "remote_as": 65002,
#                 "remote_id": "10.1.1.20",
#                 "uptime": 146
#             }
#         },
#         "router_id": "10.1.1.30"
#     }
# }
#
# Process finished with exit code 0
#
# ###########################
# Output for CiscoRouter2
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe C:\Users\belka\PycharmProjects\NetworkAutomation\Napalm\napalm_retrieve_information.py
# {
#     "fqdn": "CiscoRouter2.domain.com",
#     "hostname": "CiscoRouter2",
#     "interface_list": [
#         "FastEthernet0/0",
#         "FastEthernet0/1",
#         "Serial0/1/0",
#         "FastEthernet0/3/0"
#     ],
#     "model": "2811",
#     "os_version": "2800 Software (C2800NM-ADVENTERPRISEK9-M), Version 12.4(24)T5, RELEASE SOFTWARE (fc3)",
#     "serial_number": "FTX1305A1DN",
#     "uptime": 662640.0,
#     "vendor": "Cisco"
# }
# [
#     {
#         "age": 133.0,
#         "interface": "FastEthernet0/0",
#         "ip": "10.1.1.1",
#         "mac": "68:9C:E2:71:2F:42"
#     },
#     {
#         "age": 46.0,
#         "interface": "FastEthernet0/0",
#         "ip": "10.1.1.10",
#         "mac": "00:16:47:41:82:30"
#     },
#     {
#         "age": -1.0,
#         "interface": "FastEthernet0/0",
#         "ip": "10.1.1.20",
#         "mac": "00:24:14:EB:EF:48"
#     },
#     {
#         "age": 79.0,
#         "interface": "FastEthernet0/0",
#         "ip": "10.1.1.30",
#         "mac": "00:1E:4A:ED:ED:A0"
#     }
# ]
# {
#     "FastEthernet0/0": {
#         "description": "connection to switch gig1/0/5",
#         "is_enabled": true,
#         "is_up": true,
#         "last_flapped": -1.0,
#         "mac_address": "00:24:14:EB:EF:48",
#         "mtu": 1500,
#         "speed": 100.0
#     },
#     "FastEthernet0/1": {
#         "description": "connection to CiscoRouter1 fe0/1",
#         "is_enabled": true,
#         "is_up": false,
#         "last_flapped": -1.0,
#         "mac_address": "00:24:14:EB:EF:49",
#         "mtu": 1500,
#         "speed": 100.0
#     },
#     "FastEthernet0/3/0": {
#         "description": "connection to CiscoRouter3 fe0/1",
#         "is_enabled": true,
#         "is_up": true,
#         "last_flapped": -1.0,
#         "mac_address": "00:23:33:81:20:73",
#         "mtu": 1500,
#         "speed": 100.0
#     },
#     "Serial0/1/0": {
#         "description": "",
#         "is_enabled": false,
#         "is_up": false,
#         "last_flapped": -1.0,
#         "mac_address": "",
#         "mtu": 1500,
#         "speed": 1.536
#     }
# }
# {
#     "FastEthernet0/0": {
#         "rx_broadcast_packets": 220010,
#         "rx_discards": 0,
#         "rx_errors": 0,
#         "rx_multicast_packets": -1,
#         "rx_octets": 26715557,
#         "rx_unicast_packets": 221711,
#         "tx_broadcast_packets": -1,
#         "tx_discards": 0,
#         "tx_errors": 0,
#         "tx_multicast_packets": -1,
#         "tx_octets": 15609257,
#         "tx_unicast_packets": 151120
#     },
#     "FastEthernet0/1": {
#         "rx_broadcast_packets": 0,
#         "rx_discards": 0,
#         "rx_errors": 0,
#         "rx_multicast_packets": -1,
#         "rx_octets": 0,
#         "rx_unicast_packets": 0,
#         "tx_broadcast_packets": -1,
#         "tx_discards": 0,
#         "tx_errors": 0,
#         "tx_multicast_packets": -1,
#         "tx_octets": 9180,
#         "tx_unicast_packets": 147
#     },
#     "FastEthernet0/3/0": {
#         "rx_broadcast_packets": 0,
#         "rx_discards": 0,
#         "rx_errors": 0,
#         "rx_multicast_packets": -1,
#         "rx_octets": 1498181,
#         "rx_unicast_packets": 4072,
#         "tx_broadcast_packets": -1,
#         "tx_discards": 0,
#         "tx_errors": 0,
#         "tx_multicast_packets": -1,
#         "tx_octets": 2729387,
#         "tx_unicast_packets": 26056
#     },
#     "Serial0/1/0": {
#         "rx_broadcast_packets": 0,
#         "rx_discards": 0,
#         "rx_errors": 0,
#         "rx_multicast_packets": -1,
#         "rx_octets": 0,
#         "rx_unicast_packets": 0,
#         "tx_broadcast_packets": -1,
#         "tx_discards": 0,
#         "tx_errors": 0,
#         "tx_multicast_packets": -1,
#         "tx_octets": 0,
#         "tx_unicast_packets": 0
#     }
# }
# {
#     "FastEthernet0/0": {
#         "ipv4": {
#             "10.1.1.20": {
#                 "prefix_length": 24
#             }
#         }
#     }
# }
# {
#     "global": {
#         "peers": {
#             "10.1.1.10": {
#                 "address_family": {
#                     "ipv4 unicast": {
#                         "accepted_prefixes": -1,
#                         "received_prefixes": -1,
#                         "sent_prefixes": -1
#                     }
#                 },
#                 "description": "",
#                 "is_enabled": true,
#                 "is_up": false,
#                 "local_as": 65002,
#                 "remote_as": 65001,
#                 "remote_id": "0.0.0.0",
#                 "uptime": -1
#             },
#             "10.1.1.30": {
#                 "address_family": {
#                     "ipv4 unicast": {
#                         "accepted_prefixes": 0,
#                         "received_prefixes": 0,
#                         "sent_prefixes": 0
#                     }
#                 },
#                 "description": "",
#                 "is_enabled": true,
#                 "is_up": true,
#                 "local_as": 65002,
#                 "remote_as": 65003,
#                 "remote_id": "10.1.1.30",
#                 "uptime": 728
#             }
#         },
#         "router_id": "10.1.1.20"
#     }
# }
#
# Process finished with exit code 0
#
# '''
