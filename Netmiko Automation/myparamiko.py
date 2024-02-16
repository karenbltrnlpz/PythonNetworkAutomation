import paramiko
import time

''' This module is to help us keep things DRY. So we don't have to 
type out these commands for future automations and to prevent mistakes. '''

# creating a function to establish an SSH connection to a device and returning the ssh_client to use it independently with other functions
def connect(server_ip, server_port, user, passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=passwd,
                       look_for_keys=False, allow_agent=False)

    return ssh_client

# getting the shell and returning it to use it in the send command function
def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

# sending a command to the device via SSH to be executed
def send_command(shell, command, timeout=1):
    print(f'Sending command:  {command}')
    shell.send(command + '\n')
    time.sleep(timeout)

# returning the output of the commands that were send to the
# devices along with the number of bytes signified by n=10000 to read and decoded using decode() method
def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()


# closing the shell
def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()

if '__name__' == '__main__':
    switch = {'server_ip': '10.1.1.1', 'server_port': '22', 'user': 'admin', 'passwd': 'cisco'}
    client = connect(**switch)
    shell = get_shell(client)

    send_command(shell, 'enable')
    send_command(shell, 'cisco')
    send_command(shell, 'term len 0')
    send_command(shell, 'sh version')
    send_command(shell, 'sh ip int br')

    output = show(shell)
    print(output)


