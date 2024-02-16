from netmiko import ConnectHandler


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
connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')
connection.enable()

output_shipintbr = connection.send_command('sh ip int br')
print(f'Printing sh ip int br command:\n {output_shipintbr}')

print('#' *30)

output_shrun = connection.send_command('sh run')
print(f'Printing sh run command:\n {output_shrun}')


print('Closing connection...')
connection.disconnect()

# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge4.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Entering the enable mode...
# Printing sh ip int br command:
#  Interface                  IP-Address      OK? Method Status                Protocol
# FastEthernet0/0            10.1.1.10       YES NVRAM  up                    up
# FastEthernet0/1            unassigned      YES NVRAM  administratively down down
# Serial0/0/0                unassigned      YES NVRAM  administratively down down
# Serial0/1/0                unassigned      YES NVRAM  administratively down down
# ##############################
# Printing sh run command:
#  Building configuration...
#
# Current configuration : 1116 bytes
# !
# version 12.4
# service timestamps debug datetime msec
# service timestamps log datetime msec
# service password-encryption
# !
# hostname CiscoRouter1
# !
# boot-start-marker
# boot-end-marker
# !
# enable secret 5 $1$HB51$pj21oXJOUu6CZJPsteIrG0
# !
# aaa new-model
# !
# !
# !
# aaa session-id common
# !
# !
# ip cef
# !
# !
# no ip domain lookup
# ip domain name domain.com
# !
# !
# !
# !
# username admin password 7 0822455D0A16
# !
# !
# ip ssh version 2
# !
# !
# !
# !
# interface FastEthernet0/0
#  description connection to Switch gig1/0/7
#  ip address 10.1.1.10 255.255.255.0
#  duplex auto
#  speed auto
# !
# interface FastEthernet0/1
#  description connection to CiscoRouter2 f0/1
#  no ip address
#  shutdown
#  duplex auto
#  speed auto
# !
# interface Serial0/0/0
#  no ip address
#  shutdown
# !
# interface Serial0/1/0
#  no ip address
#  shutdown
# !
# router ospf 1
#  log-adjacency-changes
#  network 0.0.0.0 255.255.255.255 area 0
# !
# ip forward-protocol nd
# !
# no ip http server
# no ip http secure-server
# !
# !
# !
# control-plane
# !
# !
# !
# line con 0
# line aux 0
# line vty 0 4
#  password 7 110A1016141D
#  transport input ssh
# line vty 5 15
#  password 7 110A1016141D
#  transport input ssh
# !
# scheduler allocate 20000 1000
# !
# end
#
# Closing connection...
#
# Process finished with exit code 0
#
# '''