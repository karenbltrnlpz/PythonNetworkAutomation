from netmiko import ConnectHandler


# creating a function called execute taking in parameters
# 'device' and 'command'

def execute(device, command_list):
    connection = ConnectHandler(**device)
    print('Entering the enable mode...')
    connection.enable()
    print('Sending command...')
    output = connection.send_config_set(command_list)
    print(output)
    connection.disconnect()

# Creating a dictionary with connection parameters
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.10',
    'username': 'admin',
    'password': 'cisco',
    'port': 22, # optional, default 22
    'secret': 'cisco', # optional, default ''. This is the enable password
    'verbose': True # optional, default False
}

# saving configs to a list to remove rip routing
# protocol, configuring IP address on interface loopback 0, and
# running a show command to show the configuration for int loopback 0
cmd = ['no router rip', 'int loopback 0',
       'ip address 1.1.1.1 255.255.255.255',
       'end', 'sh ip int loopback 0']

execute(cisco_device, cmd)

# Creating a dictionary with connection parameters for linux
# linux = {
#     'device_type': 'linux',
#     'host': '192.168.0.90',
#     'username': 'admin',
#     'password': 'cisco',
#     'port': 22, # optional, default 22
#     'secret': 'cisco', # optional, default ''. This is the enable password
#     'verbose': True # optional, default False
# }
# execute(linux, 'ip addr')

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge14.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Entering the enable mode...
# Sending command...
# configure terminal
# Enter configuration commands, one per line.  End with CNTL/Z.
# CiscoRouter1(config)#no router rip
# CiscoRouter1(config)#int loopback 0
# CiscoRouter1(config-if)#ip address 1.1.1.1 255.255.255.255
# CiscoRouter1(config-if)#end
# CiscoRouter1#sh ip int loopback 0
# Loopback0 is up, line protocol is up
#   Internet address is 1.1.1.1/32
#   Broadcast address is 255.255.255.255
#   Address determined by setup command
#   MTU is 1514 bytes
#   Helper address is not set
#   Directed broadcast forwarding is disabled
#   Multicast reserved groups joined: 224.0.0.5
#   Outgoing access list is not set
#   Inbound  access list is not set
#   Proxy ARP is enabled
#   Local Proxy ARP is disabled
#   Security level is default
#   Split horizon is enabled
#   ICMP redirects are always sent
#   ICMP unreachables are always sent
#   ICMP mask replies are never sent
#   IP fast switching is enabled
#   IP fast switching on the same interface is disabled
#   IP Flow switching is disabled
#   IP CEF switching is enabled
#   IP CEF Fast switching turbo vector
#   IP multicast fast switching is enabled
#   IP multicast distributed fast switching is disabled
#   IP route-cache flags are Fast, CEF
#   Router Discovery is disabled
#   IP output packet accounting is disabled
#   IP access violation accounting is disabled
#   TCP/IP header compression is disabled
#   RTP/IP header compression is disabled
#   Policy routing is disabled
#   Network address translation is disabled
#   BGP Policy Mapping is disabled
#   WCCP Redirect outbound is disabled
#   WCCP Redirect inbound is disabled
#   WCCP Redirect exclude is disabled
# CiscoRouter1#
#
# Process finished with exit code 0
#
# '''