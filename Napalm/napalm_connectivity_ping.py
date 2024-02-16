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
ios = driver('10.1.1.10', 'admin', 'cisco', optional_args=optional_args)
# we open the connection to communicate with the network device
ios.open()

output = ios.ping(destination='10.1.1.30', count=2, source='1.1.1.1')
ping = json.dumps(output, sort_keys=True, indent=4)
print(ping)


# closing the connection to the device
ios.close()

# '''
# Output: From a non-existent IP/device
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe C:\Users\belka\PycharmProjects\NetworkAutomation\Napalm\napalm_connectivity_ping.py
# {
#     "success": {
#         "packet_loss": 2,
#         "probes_sent": 2,
#         "results": [],
#         "rtt_avg": 0.0,
#         "rtt_max": 0.0,
#         "rtt_min": 0.0,
#         "rtt_stddev": 0.0
#     }
# }
#
# Process finished with exit code 0
#
# Output from an existing device in this case CiscoRouter3:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe C:\Users\belka\PycharmProjects\NetworkAutomation\Napalm\napalm_connectivity_ping.py
# {
#     "success": {
#         "packet_loss": 0,
#         "probes_sent": 2,
#         "results": [
#             {
                    # first packet
#                 "ip_address": "10.1.1.30",
#                 "rtt": 0.0
#             },
#             {
                    # second packet
#                 "ip_address": "10.1.1.30",
#                 "rtt": 0.0
#             }
#         ],
#         "rtt_avg": 2.0,
#         "rtt_max": 4.0,
#         "rtt_min": 1.0,
#         "rtt_stddev": 0.0
#     }
# }
#
# Process finished with exit code 0
# '''