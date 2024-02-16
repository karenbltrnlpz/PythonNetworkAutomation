import myparamiko as mp
import getpass

password = getpass.getpass()

ssh_client = mp.connect('192.168.0.90', 22, 'devops', password)
remote_connection = mp.get_shell(ssh_client)
mp.send_command(remote_connection, 'sudo useradd -m - d /home/panda2 -s /bin/bash panda2')
mp.send_command(remote_connection, password)
users = mp.send_command(remote_connection, 'cat /etc/passwd')

print(users.decode())
mp.close(ssh_client)