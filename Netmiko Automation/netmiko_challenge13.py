from netmiko import ConnectHandler


# creating a function called execute taking in parameters
# 'device' and 'command'

def execute(device, command):
    connection = ConnectHandler(**device)
    print('Entering the enable mode...')
    connection.enable()
    print('Sending command...')
    output = connection.send_command(command)
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
execute(cisco_device, 'sh ver')

# Creating a dictionary with connection parameters for linux
linux = {
    'device_type': 'linux',
    'host': '192.168.0.90',
    'username': 'admin',
    'password': 'cisco',
    'port': 22, # optional, default 22
    'secret': 'cisco', # optional, default ''. This is the enable password
    'verbose': True # optional, default False
}
execute(linux, 'ip addr')

# ''' Output: for the cisco device:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe "C:\Users\belka\PycharmProjects\NetworkAutomation\Netmiko Automation\netmiko_challenge13.py"
# SSH connection established to 10.1.1.10:22
# Interactive SSH session established
# Entering the enable mode...
# Sending command...
# Cisco IOS Software, 2800 Software (C2800NM-ADVSECURITYK9-M), Version 12.4(17), RELEASE SOFTWARE (fc1)
# Technical Support: http://www.cisco.com/techsupport
# Copyright (c) 1986-2007 by Cisco Systems, Inc.
# Compiled Fri 07-Sep-07 16:46 by prod_rel_team
#
# ROM: System Bootstrap, Version 12.4(1r) [hqluong 1r], RELEASE SOFTWARE (fc1)
#
# CiscoRouter1 uptime is 4 days, 13 hours, 55 minutes
# System returned to ROM by power-on
# System image file is "flash:c2800nm-advsecurityk9-mz.124-17.bin"
#
#
# This product contains cryptographic features and is subject to United
# States and local country laws governing import, export, transfer and
# use. Delivery of Cisco cryptographic products does not imply
# third-party authority to import, export, distribute or use encryption.
# Importers, exporters, distributors and users are responsible for
# compliance with U.S. and local country laws. By using this product you
# agree to comply with applicable laws and regulations. If you are unable
# to comply with U.S. and local laws, return this product immediately.
#
# A summary of U.S. laws governing Cisco cryptographic products may be found at:
# http://www.cisco.com/wwl/export/crypto/tool/stqrg.html
#
# If you require further assistance please contact us by sending email to
# export@cisco.com.
#
# Cisco 2811 (revision 53.50) with 249856K/12288K bytes of memory.
# Processor board ID FTX1001C14X
# 2 FastEthernet interfaces
# 2 Serial interfaces
# 1 Virtual Private Network (VPN) Module
# DRAM configuration is 64 bits wide with parity enabled.
# 239K bytes of non-volatile configuration memory.
# 62720K bytes of ATA CompactFlash (Read/Write)
#
# Configuration register is 0x2102
#
#
# Process finished with exit code 0
#
# Output for the linux command: this is from the CentOS 7 VM:
#
# '''