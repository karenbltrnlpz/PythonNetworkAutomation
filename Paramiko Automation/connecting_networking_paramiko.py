import paramiko

ssh_client = paramiko.SSHClient()
# print(type(ssh_client))


# method that automatically accepts the server host key before
# connecting to SSH server
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# to connect to the SSH daemon(GNS3) or SSH client (Putty)
# ssh_client.connect(hostname='10.1.1.10', port='22', username='admin', password='cisco',
#                    look_for_keys=False, allow_agent=False)
router = {'hostname':'10.1.1.10', 'port': '22', 'username': 'admin', 'password': 'cisco'}

print(f'Connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

# to check if connection is
# active it will return True if it established a connection
print(ssh_client.get_transport().is_active())

# sending commands
# to close/disconnect the connection to the router use the close()
print(f'Closing connection to {router["hostname"]}')
ssh_client.close()

