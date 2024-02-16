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
ios = driver('10.1.1.1', 'admin', 'cisco', optional_args=optional_args)
# we open the connection to communicate with the network device
ios.open()

ios.load_replace_candidate(filename='config_switch.txt')

diff = ios.compare_config()
# This will print the output of the compare.config()method which compares the difference
# between the configuration of the router and the configuration file.
# print(diff)

# If there are differences, commit changes using the commit_config() method
if len(diff):
    print(diff)
    print('Commit changes...')
    ios.commit_config()
    print('Done')
else:
    # otherwise if there are not differences, discard the changes.
    print('No changes required')
    ios.discard_config()

# closing the connection to the device
ios.close()

# '''
# NOTE: The output is from the Switch. In the video, the instructor runs it against
# the router. I tried all of the routers, but all returned an scp denied error'. When I
# ran the script against the Switch, I was able to get expected output of the compare_config()
# method.
#
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe C:\Users\belka\PycharmProjects\NetworkAutomation\Napalm\napalm_configuration_management.py
# +hostname CiscoRouter2
# +logging message-counter syslog
# +enable secret 5 $1$MRpp$bsCxXWA2moo3UJUSRg6F/0
# +dot11 syslog
# +ip source-route
# +ip cef
# +no ip domain lookup
# +ip domain name domain.com
# +no ipv6 cef
# +multilink bundle-name authenticated
# +voice-card 0
# +username admin password 7 13061E010803
# +archive
#  +log config
#   +hidekeys
# +interface FastEthernet0/0
#  +description connection to switch gig1/0/5
#  +ip address 10.1.1.20 255.255.255.0
#  +duplex full
#  +speed auto
# +interface FastEthernet0/1
#  +description connection to CiscoRouter1 fe0/1
#  +no ip address
#  +duplex auto
#  +speed auto
# +interface Serial0/1/0
#  +no ip address
#  +shutdown
#  +no fair-queue
# +interface FastEthernet0/3/0
#  +description connection to CiscoRouter3 fe0/1
#  +no ip address
#  +duplex auto
#  +speed auto
# router ospf 1
#  +log-adjacency-changes
# +router bgp 65002
#  +no synchronization
#  +bgp log-neighbor-changes
#  +neighbor 10.1.1.10 remote-as 65001
#  +neighbor 10.1.1.30 remote-as 65003
#  +no auto-summary
# +ip forward-protocol nd
# +control-plane
# line vty 0 4
#  +password 7 110A1016141D
# line vty 5 15
#  +password 7 110A1016141D
# +scheduler allocate 20000 1000
# -no service pad
# -hostname Switch
# -enable secret 5 $1$kqKQ$zMPpYCAax0u6Z07GMPKMR.
# -username admin privilege 15 password 7 060506324F41
# -username u3 secret 4 tnhtc92DXBhelxjYk8LWJrPV36S2i4ntXrpb4RFmfqY
# -username netmiko secret 4 tnhtc92DXBhelxjYk8LWJrPV36S2i4ntXrpb4RFmfqY
# -username admin1 privilege 15 secret 4 tnhtc92DXBhelxjYk8LWJrPV36S2i4ntXrpb4RFmfqY
# -aaa authentication login default local
# -aaa authorization exec default local none
# -switch 1 provision ws-c3750x-48
# -system mtu routing 1500
# -ip routing
# -no ip domain-lookup
# -ip domain-name net-auto.io
# -vtp domain MN550
# -vtp mode transparent
# -crypto pki trustpoint TP-self-signed-3799068416
#  -enrollment selfsigned
#  -subject-name cn=IOS-Self-Signed-Certificate-3799068416
#  -revocation-check none
#  -rsakeypair TP-self-signed-3799068416
# -crypto pki trustpoint TP-self-signed-1619049344
#  -enrollment selfsigned
#  -subject-name cn=IOS-Self-Signed-Certificate-1619049344
#  -revocation-check none
#  -rsakeypair TP-self-signed-1619049344
# -crypto pki certificate chain TP-self-signed-3799068416
#  -certificate self-signed 01
#   -3082022B 30820194 A0030201 02020101 300D0609 2A864886 F70D0101 05050030
#   -31312F30 2D060355 04031326 494F532D 53656C66 2D536967 6E65642D 43657274
#   -69666963 6174652D 33373939 30363834 3136301E 170D3131 30333330 30313239
#   -32365A17 0D323030 31303130 30303030 305A3031 312F302D 06035504 03132649
#   -4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D33 37393930
#   -36383431 3630819F 300D0609 2A864886 F70D0101 01050003 818D0030 81890281
#   -8100DE5A B4302E47 3113E057 6554831D EF9698B3 1598E5DB 89449C1A 7499B9B5
#   -CD0D4F92 D2FDA39D 68B18D2B 8BE7C369 BF066459 7A7CFB83 683D1EB6 C0802D46
#   -7D7B3239 BF75CEC4 E315B9E4 3F56EECE FCD67716 5FFE2951 8313E892 512CA828
#   -006E086E 1BA614DC 05C4CEB4 B0EB57D1 18D34BF5 F195061A 5D558706 2D1ED592
#   -AA770203 010001A3 53305130 0F060355 1D130101 FF040530 030101FF 301F0603
#   -551D2304 18301680 141532C4 9EE4CFB1 BFDDD0C4 53A59B5D 98F0FD55 51301D06
#   -03551D0E 04160414 1532C49E E4CFB1BF DDD0C453 A59B5D98 F0FD5551 300D0609
#   -2A864886 F70D0101 05050003 818100B6 C1B0D2BF 167AF7AA 4DD77A43 0BAE0253
#   -7B830F25 78A890CA C684E0BB 1EF260C1 36C57A3E 7B70667E 463BC2E4 A10AC383
#   -4D7D6F88 735710C7 E21EF172 2F50AAAD 56BCE630 8A0C4404 ED8AF715 D4E61917
#   -D9A5E7DE 0568F0CF 7B1EC5BB 7C6A6AF4 7E23729A 46961915 F0D05BE7 CBA5EB10
#   -F03C304E 30AA1570 29628FCC 3BFA48
#   -	quit
# -crypto pki certificate chain TP-self-signed-1619049344
# -license boot level ipservices
# -spanning-tree mode rapid-pvst
# -spanning-tree extend system-id
# -vlan internal allocation policy ascending
# -vlan 10,100,200,300,400,881-883
# -ip tftp source-interface Vlan1
# -ip ssh dh min size 2048
# -interface Loopback0
#  -ip address 1.1.1.1 255.255.255.255
# -interface FastEthernet0
#  -no ip address
#  -no ip route-cache
#  -shutdown
# -interface GigabitEthernet1/0/1
#  -description CONNECTION TO NETGEAR GW
#  -switchport access vlan 100
#  -switchport mode access
# -interface GigabitEthernet1/0/2
# -interface GigabitEthernet1/0/3
#  -switchport access vlan 200
#  -switchport mode access
# -interface GigabitEthernet1/0/4
# -interface GigabitEthernet1/0/5
#  -switchport access vlan 200
#  -switchport mode access
# -interface GigabitEthernet1/0/6
# -interface GigabitEthernet1/0/7
#  -switchport access vlan 200
#  -switchport mode access
# -interface GigabitEthernet1/0/8
# -interface GigabitEthernet1/0/9
#  -switchport access vlan 200
#  -switchport mode access
# -interface GigabitEthernet1/0/10
# -interface GigabitEthernet1/0/11
# -interface GigabitEthernet1/0/12
# -interface GigabitEthernet1/0/13
# -interface GigabitEthernet1/0/14
# -interface GigabitEthernet1/0/15
# -interface GigabitEthernet1/0/16
# -interface GigabitEthernet1/0/17
# -interface GigabitEthernet1/0/18
# -interface GigabitEthernet1/0/19
# -interface GigabitEthernet1/0/20
# -interface GigabitEthernet1/0/21
# -interface GigabitEthernet1/0/22
# -interface GigabitEthernet1/0/23
# -interface GigabitEthernet1/0/24
# -interface GigabitEthernet1/0/25
# -interface GigabitEthernet1/0/26
# -interface GigabitEthernet1/0/27
# -interface GigabitEthernet1/0/28
# -interface GigabitEthernet1/0/29
# -interface GigabitEthernet1/0/30
# -interface GigabitEthernet1/0/31
# -interface GigabitEthernet1/0/32
# -interface GigabitEthernet1/0/33
# -interface GigabitEthernet1/0/34
# -interface GigabitEthernet1/0/35
# -interface GigabitEthernet1/0/36
# -interface GigabitEthernet1/0/37
# -interface GigabitEthernet1/0/38
# -interface GigabitEthernet1/0/39
# -interface GigabitEthernet1/0/40
# -interface GigabitEthernet1/0/41
# -interface GigabitEthernet1/0/42
# -interface GigabitEthernet1/0/43
# -interface GigabitEthernet1/0/44
# -interface GigabitEthernet1/0/45
# -interface GigabitEthernet1/0/46
# -interface GigabitEthernet1/0/47
# -interface GigabitEthernet1/0/48
# -interface GigabitEthernet1/1/1
# -interface GigabitEthernet1/1/2
# -interface GigabitEthernet1/1/3
# -interface GigabitEthernet1/1/4
# -interface TenGigabitEthernet1/1/1
# -interface TenGigabitEthernet1/1/2
# -interface Vlan1
#  -ip address dhcp
#  -shutdown
# -interface Vlan100
#  -description INET
#  -ip address 192.168.1.254 255.255.255.0
# -interface Vlan200
#  -description MANAGEMENT LAB VLAN
#  -ip address 10.1.1.1 255.255.255.0
# router ospf 1
#  -default-information originate
#  -distance 60
# -ip route 0.0.0.0 0.0.0.0 192.168.1.1
# -access-list 1 permit any
# line vty 0 4
#  -password 7 121A0C041104
# line vty 5 15
#  -password 7 121A0C041104
# -ntp server devicehelper.cisco.com
#
# Process finished with exit code 0
#

# '''