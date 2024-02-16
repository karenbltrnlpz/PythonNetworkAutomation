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



# closing the connection to the device
ios.close()