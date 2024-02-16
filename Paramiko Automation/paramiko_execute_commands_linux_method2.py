import paramiko
import time

''' The script below modified by ChatGPT 4 worked
This script focuses on running commands that require root access by using the sudo prefix in 
front of the command that requires root access.
 Only sudo group can execute commands as root.'''

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

linux = {'hostname': '192.168.0.90', 'port': '22', 'username':'devops', 'password': 'Time4work!'}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

# creating a new user
stdin, stdout, stderr = ssh_client.exec_command('sudo useradd u2\n', get_pty=True)
# inputting the password
stdin.write('Time4work!\n')
#making sure it has enough time to finish executing the command
time.sleep(2)

#executing command to display the linux users
stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n')
print(stdout.read().decode())
time.sleep(1)


if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()


# Output: this script was run inside the belty VMs under the same network as the CentOS-Udemy-Server VM

# `C:\Users\devops\PycharmProjects\NetworkAutomation2\.venv\Scripts\python.exe C:\Users\devops\PycharmProjects\NetworkAutomation2\paramiko_execute_commands_linux_method2.py
# Connecting to 192.168.0.90
# root:x:0:0:root:/root:/bin/bash
# bin:x:1:1:bin:/bin:/sbin/nologin
# daemon:x:2:2:daemon:/sbin:/sbin/nologin
# adm:x:3:4:adm:/var/adm:/sbin/nologin
# lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
# sync:x:5:0:sync:/sbin:/bin/sync
# shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
# halt:x:7:0:halt:/sbin:/sbin/halt
# mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
# operator:x:11:0:operator:/root:/sbin/nologin
# games:x:12:100:games:/usr/games:/sbin/nologin
# ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
# nobody:x:99:99:Nobody:/:/sbin/nologin
# systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
# dbus:x:81:81:System message bus:/:/sbin/nologin
# polkitd:x:999:998:User for polkitd:/:/sbin/nologin
# sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
# postfix:x:89:89::/var/spool/postfix:/sbin/nologin
# chrony:x:998:996::/var/lib/chrony:/sbin/nologin
# devops:x:1000:1000:devops:/home/devops:/bin/bash
# nixbld1:x:30001:30000:Nix build user 1:/var/empty:/sbin/nologin
# nixbld2:x:30002:30000:Nix build user 2:/var/empty:/sbin/nologin
# nixbld3:x:30003:30000:Nix build user 3:/var/empty:/sbin/nologin
# nixbld4:x:30004:30000:Nix build user 4:/var/empty:/sbin/nologin
# nixbld5:x:30005:30000:Nix build user 5:/var/empty:/sbin/nologin
# nixbld6:x:30006:30000:Nix build user 6:/var/empty:/sbin/nologin
# nixbld7:x:30007:30000:Nix build user 7:/var/empty:/sbin/nologin
# nixbld8:x:30008:30000:Nix build user 8:/var/empty:/sbin/nologin
# nixbld9:x:30009:30000:Nix build user 9:/var/empty:/sbin/nologin
# nixbld10:x:30010:30000:Nix build user 10:/var/empty:/sbin/nologin
# nixbld11:x:30011:30000:Nix build user 11:/var/empty:/sbin/nologin
# nixbld12:x:30012:30000:Nix build user 12:/var/empty:/sbin/nologin
# nixbld13:x:30013:30000:Nix build user 13:/var/empty:/sbin/nologin
# nixbld14:x:30014:30000:Nix build user 14:/var/empty:/sbin/nologin
# nixbld15:x:30015:30000:Nix build user 15:/var/empty:/sbin/nologin
# nixbld16:x:30016:30000:Nix build user 16:/var/empty:/sbin/nologin
# nixbld17:x:30017:30000:Nix build user 17:/var/empty:/sbin/nologin
# nixbld18:x:30018:30000:Nix build user 18:/var/empty:/sbin/nologin
# nixbld19:x:30019:30000:Nix build user 19:/var/empty:/sbin/nologin
# nixbld20:x:30020:30000:Nix build user 20:/var/empty:/sbin/nologin
# nixbld21:x:30021:30000:Nix build user 21:/var/empty:/sbin/nologin
# nixbld22:x:30022:30000:Nix build user 22:/var/empty:/sbin/nologin
# nixbld23:x:30023:30000:Nix build user 23:/var/empty:/sbin/nologin
# nixbld24:x:30024:30000:Nix build user 24:/var/empty:/sbin/nologin
# nixbld25:x:30025:30000:Nix build user 25:/var/empty:/sbin/nologin
# nixbld26:x:30026:30000:Nix build user 26:/var/empty:/sbin/nologin
# nixbld27:x:30027:30000:Nix build user 27:/var/empty:/sbin/nologin
# nixbld28:x:30028:30000:Nix build user 28:/var/empty:/sbin/nologin
# nixbld29:x:30029:30000:Nix build user 29:/var/empty:/sbin/nologin
# nixbld30:x:30030:30000:Nix build user 30:/var/empty:/sbin/nologin
# nixbld31:x:30031:30000:Nix build user 31:/var/empty:/sbin/nologin
# nixbld32:x:30032:30000:Nix build user 32:/var/empty:/sbin/nologin
# u2:x:30033:30033::/home/u2:/bin/bash
#
# Closing connection
#
# Process finished with exit code 0
