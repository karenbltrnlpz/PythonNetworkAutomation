import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


linux = {'hostname': '192.168.0.90', 'port': '22', 'username':'devops', 'password': 'Time4work!'}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('cat /etc/passwd\n')
time.sleep(1)

shell.send('sudo cat /etc/shadow\n')
shell.send('Time4work!\n')
time.sleep(1)


output = shell.recv(10000)
# print(type(output))
output = output.decode('utf-8')
print(output)


if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()

# Output: this script was run inside the belty VMs under the same network as the CentOS-Udemy-Server VM
#
# You were correct about the failing sudo /etc/shaodow command  - i had incorrect password. My output was this:
# `C:\Users\devops\PycharmProjects\NetworkAutomation2\.venv\Scripts\python.exe C:\Users\devops\PycharmProjects\NetworkAutomation2\paramiko_execute_commands_linux.py
# Connecting to 192.168.0.90
#
# cat /etc/passwd
# [devops@localhost ~]$ cat /etc/passwd
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
# [devops@localhost ~]$ sudo cat /etc/shadow
# Time4work!
# [sudo] password for devops:
# root:$6$9i4n8QBP180bOete$vtGReCjW9Kk5O7XB8B8PxsU41q2nqQh3.eXkhPwGrfp0gh2XhTHFUSrZtCq2DTfTHejacrM5cpajw26YnZUmm0::0:99999:7:::
# bin:*:18353:0:99999:7:::
# daemon:*:18353:0:99999:7:::
# adm:*:18353:0:99999:7:::
# lp:*:18353:0:99999:7:::
# sync:*:18353:0:99999:7:::
# shutdown:*:18353:0:99999:7:::
# halt:*:18353:0:99999:7:::
# mail:*:18353:0:99999:7:::
# operator:*:18353:0:99999:7:::
# games:*:18353:0:99999:7:::
# ftp:*:18353:0:99999:7:::
# nobody:*:18353:0:99999:7:::
# systemd-network:!!:19586::::::
# dbus:!!:19586::::::
# polkitd:!!:19586::::::
# sshd:!!:19586::::::
# postfix:!!:19586::::::
# chrony:!!:19586::::::
# devops:$6$U.S4IkChIww1DHUq$95SQuosuBr4cI0XwFIsS//iI/4GwnJ9fQ8XDTkltRyMaxeRVHTsz9Uzc4jtj4EbEXeMEL5BlV.JTpabLAWXE8.::0:99999:7:::
# nixbld1:!:19609::::::
# nixbld2:!:19609::::::
# nixbld3:!:19609::::::
# nixbld4:!:19609::::::
# nixbld5:!:19609::::::
# nixbld6:!:19609::::::
# nixbld7:!:19609::::::
# nixbld8:!:19609::::::
# nixbld9:!:19609::::::
# nixbld10:!:19609::::::
# nixbld11:!:19609::::::
# nixbld12:!:19609::::::
# nixbld13:!:19609::::::
# nixbld14:!:19609::::::
# nixbld15:!:19609::::::
# nixbld16:!:19609::::::
# nixbld17:!:19609::::::
# nixbld18:!:19609::::::
# nixbld19:!:19609::::::
# nixbld20:!:19609::::::
# nixbld21:!:19609::::::
# nixbld22:!:19609::::::
# nixbld23:!:19609::::::
# nixbld24:!:19609::::::
# nixbld25:!:19609::::::
# nixbld26:!:19609::::::
# nixbld27:!:19609::::::
# nixbld28:!:19609::::::
# nixbld29:!:19609::::::
# nixbld30:!:19609::::::
# nixbld31:!:19609::::::
# nixbld32:!:19609::::::
# [devops@localhost ~]$
# Closing connection
#
# Process finished with exit code 0
# `
