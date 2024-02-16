import paramiko
import time

''' The script below did not work for our use case scenario'''
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#
# linux = {'hostname': '192.168.0.90', 'port': '22', 'username':'devops', 'password': 'Time4work!'}
# print(f'Connecting to {linux["hostname"]}')
# ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)
#
# # tuple unpacking the values that return from the exec_command() method
# stdin, stdout, stderr = ssh_client.exec_command('ip addr\n')
#
# # reads the output as bytes
# output = stdout.read()
# # to decode the bytes into a readeable string format
# output = output.decode()
# print(output)
#
# if ssh_client.get_transport().is_active() == True:
#     print('Closing connection')
#     ssh_client.close()

''' The script below modified by ChatGPT 4 worked'''

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

linux = {'hostname': '192.168.0.90', 'port': '22', 'username':'devops', 'password': 'Time4work!'}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

# Command with sudo and password
command = f'echo {linux["password"]} | sudo -S ip addr'
stdin, stdout, stderr = ssh_client.exec_command(command)

time.sleep(2)

# Read the output and error
output = stdout.read().decode()
error = stderr.read().decode()
print(output)
print(error)

# Command to show who is using the Linux instance
stdin, stdout, stderr = ssh_client.exec_command('who\n')

time.sleep(2)

# Read the output and error
output = stdout.read().decode()
error = stderr.read().decode()
print(output)
print(error)

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()


# Output: this script was run inside the belty VMs under the same network as the CentOS-Udemy-Server VM

# `C:\Users\devops\PycharmProjects\NetworkAutomation2\.venv\Scripts\python.exe C:\Users\devops\PycharmProjects\NetworkAutomation2\paramiko_execute_commands_linux2.py
# Connecting to 192.168.0.90
# 1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
#     link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
#     inet 127.0.0.1/8 scope host lo
#        valid_lft forever preferred_lft forever
#     inet6 ::1/128 scope host
#        valid_lft forever preferred_lft forever
# 2: ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
#     link/ether 00:50:56:ad:a1:38 brd ff:ff:ff:ff:ff:ff
#     inet 192.168.0.90/24 brd 192.168.0.255 scope global noprefixroute ens192
#        valid_lft forever preferred_lft forever
#     inet6 2601:447:d080:d5a0:a5a3:726a:5cfb:728c/64 scope global noprefixroute dynamic
#        valid_lft 3598sec preferred_lft 3598sec
#     inet6 fe80::2779:d7a2:4a48:28ff/64 scope link tentative noprefixroute dadfailed
#        valid_lft forever preferred_lft forever
#     inet6 fe80::39ff:1d9d:1d0e:3d7b/64 scope link noprefixroute
#        valid_lft forever preferred_lft forever
# 3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
#     link/ether 02:42:3e:47:f4:91 brd ff:ff:ff:ff:ff:ff
#     inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
#        valid_lft forever preferred_lft forever
#
# [sudo] password for devops:
# devops   tty1         2023-12-28 20:30
# Closing connection
#
# Process finished with exit code 0
