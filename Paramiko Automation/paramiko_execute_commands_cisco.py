import paramiko
import time

# sending commands

ssh_client = paramiko.SSHClient()


# method that automatically accepts the server host key before
# connecting to SSH server
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# to connect to the SSH daemon(GNS3) or SSH client (Putty)
router = {'hostname':'10.1.1.10', 'port': '22', 'username': 'admin', 'password': 'cisco'}

print(f'Connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)


# calling the invoke shell method of the SSH client
# this will request an interactive shell session on the channel.
shell = ssh_client.invoke_shell()

# to send a command use the send() method
# to show the full version information without requiring the user to press enter
shell.send('terminal length 0\n')
shell.send('sh ver\n')
shell.send('sh ip int br\n')
# give it time for the device to return the information after
# the command using sleep() method and passing an int as argument to convert to time
time.sleep(1)

# to show the output of the command from the device
# number of bytes to be received
output = shell.recv(10000)
# print(type(output))

# decoding the byte output into readeable format
output = output.decode('utf-8')
print(output)

# to check if connection is
# active it will return True if it established a connection
if ssh_client.get_transport().is_active() == True:
    # to close/disconnect the connection to the router use the close()
    print(f'Closing connection to {router["hostname"]}')
    ssh_client.close()

