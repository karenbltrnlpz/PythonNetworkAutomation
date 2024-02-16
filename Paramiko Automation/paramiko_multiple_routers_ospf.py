import paramiko
import time


# # sending commands and securing passwords using getpass
# ssh_client = paramiko.SSHClient()
#
# # method that automatically accepts the server host key before
# # connecting to SSH server
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#
# # to connect to the SSH daemon(GNS3) or SSH client (Putty)
# router1 = {'hostname':'10.1.1.10', 'port': '22', 'username': 'admin', 'password': 'cisco'}
# router2 = {'hostname':'10.1.1.20', 'port': '22', 'username': 'admin', 'password': 'cisco'}
# router3 = {'hostname':'10.1.1.30', 'port': '22', 'username': 'admin', 'password': 'cisco'}
#
# routers = [router1, router2, router3]
#
# for router in routers:
#
#     print(f'Connecting to {router3["hostname"]}')
#     ssh_client.connect(**router3, look_for_keys=False, allow_agent=False)
#
#     # calling the invoke shell method of the SSH client
#     # this will request an interactive shell session on the channel.
#     shell = ssh_client.invoke_shell()
#
#     shell.send('enable\n')
#     shell.send('cisco\n') # enable password
#     shell.send('conf t\n')
#     shell.send('router ospf 1\n')
#     shell.send('net 0.0.0.0 0.0.0.0 area 0\n')
#     shell.send('end\n')
#     shell.send('terminal length 0\n') # output the results without manual enter command
#     shell.send('sh ip protocols\n')
#     time.sleep(2)
#     shell.send('copy r s\n')
#     time.sleep(2)
#
#     output = shell.recv(10000).decode()
#     print(output)
#
#     # to check if connection is
#     # active it will return True if it established a connection
#     if ssh_client.get_transport().is_active() == True:
#         # to close/disconnect the connection to the router use the close()
#         print(f'Closing connection to {router3["hostname"]}')
#         ssh_client.close()

''' Our implimentation of this script due our lab set up '''

# Define the switch and routers information
switch = {'hostname': '10.1.1.1', 'port': 22, 'username': 'admin', 'password': 'cisco'}
routers = [
    {'hostname': '10.1.1.10', 'password': 'cisco'},
    {'hostname': '10.1.1.20', 'password': 'cisco'},
    {'hostname': '10.1.1.30', 'password': 'cisco'}
]

# OSPF commands to be executed on routers
ospf_commands = [
    'enable\n',
    'cisco\n',  # This is the enable password, replace it with the actual one.
    'conf t\n',
    'router ospf 1\n',
    'net 0.0.0.0 0.0.0.0 area 0\n',
    'end\n',
    'wr\n'  # Save configuration
]

# Initialize the SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the switch
print(f'Connecting to switch {switch["hostname"]}')
ssh_client.connect(**switch, look_for_keys=False, allow_agent=False)
switch_shell = ssh_client.invoke_shell()

# Wait for the switch to be ready
time.sleep(2)

# Iterate over the routers and configure each one
for router in routers:
    print(f'Connecting to router {router["hostname"]} via switch')
    # SSH into the router from the switch
    switch_shell.send(f'ssh {router["hostname"]}\n')
    time.sleep(2)  # Wait for the ssh command to be processed

    # The switch will now ask for the router's password
    # Since we can't detect the prompt directly, we wait and then send the password.
    switch_shell.send(router["password"] + "\n")
    time.sleep(2)  # Wait for the password to be processed

    # Execute OSPF configuration commands on the router
    for cmd in ospf_commands:
        print(f'Sending command: {cmd.strip()}')
        switch_shell.send(cmd)
        time.sleep(1)  # Ensure the command is executed before sending the next one

    # Receive command output
    time.sleep(1)
    output = switch_shell.recv(65535).decode()
    print(output)

    # Exit out of the router's shell back to the switch's shell
    switch_shell.send("exit\n")
    time.sleep(1)

# Close the switch connection
print(f'Closing connection to switch {switch["hostname"]}')
ssh_client.close()

