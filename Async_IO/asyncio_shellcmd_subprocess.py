import asyncio

# to run commands coroutine
async def run(cmd):
    # this returns an instance of the process class, process is a high level
    # wrapper that allows communications with sub processes and watches for their completion
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    #calling the wrapper with the communicate method, this returns a tuple with 2
    # elements STD Out and STD EWR. This reads data from standard output and standard error
    # and waits for the process to terminate
    stdout, stderr = await proc.communicate()

    # returning the status of the execution for linux, returns 0 if no
    # errors and if an error occurred another code would return. The proc object
    # will returm this status code via the returncode method
    print(f'{cmd} exited with status code: {proc.returncode}')

    # getting the output of the command if there is any
    if stdout:
        # stdout is of data type bytes and using the
        # decode method to print it in UTF-8 text readable format
        print(f'STDOUT:\n{stdout.decode("UTF-8")}')

    # getting the output error of the command if there is any
    if stderr:
        print(f'STDERR:\n{stderr.decode("UTF-8")}')

# defining the top level coroutine, the starting point of the
# script that takes in a tuple of commands as an argument
async def main(cmds):
    # creating empty list of tasks
    tasks = []
    # iterating over the commands list:
    for cmd in cmds:
        # appending each command to the tasks list and calling the async run
        # function passing in each command
        tasks.append(run(cmd))

    # scheduling the routine to run ASAP by gathering the tasks
    await asyncio.gather(*tasks)

# # tuple of random Linux commands
# linux_cmds = ('ip addr', 'ls', 'who')
# # starting the script passing in the main async function with linux_cmds as parameter
# asyncio.run(main(linux_cmds))

# tuple of random Windows commands
windows_cmds = ('ipconfig', 'dir', 'route dir', 'arp -a')
# starting the script passing in the main async function with windows_cmds as parameter
asyncio.run(main(windows_cmds))

# ''' Windows commands output:
#
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe C:\Users\belka\PycharmProjects\NetworkAutomation\Async_IO\asyncio_shellcmd_subprocess.py
# dir exited with status code: 0
# STDOUT:
#  Volume in drive C is Windows-SSD
#  Volume Serial Number is A468-C9B8
#
#  Directory of C:\Users\belka\PycharmProjects\NetworkAutomation\Async_IO
#
# 01/10/2024  03:03 PM    <DIR>          .
# 01/10/2024  10:05 AM    <DIR>          ..
# 01/10/2024  02:21 PM           254,115 asyncio_aiohttp_web_scraper.py
# 01/10/2024  03:03 PM             2,230 asyncio_shellcmd_subprocess.py
# 01/10/2024  02:14 PM            18,282 google.com.txt
# 01/10/2024  10:49 AM             1,954 implementing_asyncio.py
# 01/10/2024  02:14 PM            52,264 python.org.txt
# 01/10/2024  02:14 PM           179,910 stackoverflow.com.txt
#                6 File(s)        508,755 bytes
#                2 Dir(s)  360,839,208,960 bytes free
#
# ipconfig exited with status code: 0
# STDOUT:
#
# Windows IP Configuration
#
#
# Ethernet adapter Ethernet 2:
#
#    Connection-specific DNS Suffix  . :
#    Link-local IPv6 Address . . . . . : fe80::7941:2bd8:e13a:f74a%18
#    IPv4 Address. . . . . . . . . . . : 192.168.56.1
#    Subnet Mask . . . . . . . . . . . : 255.255.255.0
#    Default Gateway . . . . . . . . . :
#
# Wireless LAN adapter Local Area Connection* 1:
#
#    Media State . . . . . . . . . . . : Media disconnected
#    Connection-specific DNS Suffix  . :
#
# Wireless LAN adapter Local Area Connection* 2:
#
#    Media State . . . . . . . . . . . : Media disconnected
#    Connection-specific DNS Suffix  . :
#
# Ethernet adapter VMware Network Adapter VMnet1:
#
#    Connection-specific DNS Suffix  . :
#    Link-local IPv6 Address . . . . . : fe80::70fa:ef37:babb:31e9%21
#    IPv4 Address. . . . . . . . . . . : 192.168.228.1
#    Subnet Mask . . . . . . . . . . . : 255.255.255.0
#    Default Gateway . . . . . . . . . :
#
# Ethernet adapter VMware Network Adapter VMnet8:
#
#    Connection-specific DNS Suffix  . :
#    Link-local IPv6 Address . . . . . : fe80::7b42:ecd8:a0c1:8328%13
#    IPv4 Address. . . . . . . . . . . : 192.168.232.1
#    Subnet Mask . . . . . . . . . . . : 255.255.255.0
#    Default Gateway . . . . . . . . . :
#
# Wireless LAN adapter Wi-Fi:
#
#    Connection-specific DNS Suffix  . :
#    Link-local IPv6 Address . . . . . : fe80::8048:d593:be33:1b92%17
#    IPv4 Address. . . . . . . . . . . : 192.168.1.13
#    Subnet Mask . . . . . . . . . . . : 255.255.255.0
#    Default Gateway . . . . . . . . . : 192.168.1.254
#
# Ethernet adapter Bluetooth Network Connection:
#
#    Media State . . . . . . . . . . . : Media disconnected
#    Connection-specific DNS Suffix  . :
#
# route dir exited with status code: 1
# STDERR:
#
# Manipulates network routing tables.
#
# ROUTE [-f] [-p] [-4|-6] command [destination]
#                   [MASK netmask]  [gateway] [METRIC metric]  [IF interface]
#
#   -f           Clears the routing tables of all gateway entries.  If this is
#                used in conjunction with one of the commands, the tables are
#                cleared prior to running the command.
#
#   -p           When used with the ADD command, makes a route persistent across
#                boots of the system. By default, routes are not preserved
#                when the system is restarted. Ignored for all other commands,
#                which always affect the appropriate persistent routes.
#
#   -4	       Force using IPv4.
#
#   -6           Force using IPv6.
#
#   command      One of these:
#                  PRINT     Prints  a route
#                  ADD       Adds    a route
#                  DELETE    Deletes a route
#                  CHANGE    Modifies an existing route
#   destination  Specifies the host.
#   MASK         Specifies that the next parameter is the 'netmask' value.
#   netmask      Specifies a subnet mask value for this route entry.
#                If not specified, it defaults to 255.255.255.255.
#   gateway      Specifies gateway.
#   interface    the interface number for the specified route.
#   METRIC       specifies the metric, ie. cost for the destination.
#
# All symbolic names used for destination are looked up in the network database
# file NETWORKS. The symbolic names for gateway are looked up in the host name
# database file HOSTS.
#
# If the command is PRINT or DELETE. Destination or gateway can be a wildcard,
# (wildcard is specified as a star '*'), or the gateway argument may be omitted.
#
# If Dest contains a * or ?, it is treated as a shell pattern, and only
# matching destination routes are printed. The '*' matches any string,
# and '?' matches any one char. Examples: 157.*.1, 157.*, 127.*, *224*.
#
# Pattern match is only allowed in PRINT command.
# Diagnostic Notes:
#     Invalid MASK generates an error, that is when (DEST & MASK) != DEST.
#     Example> route ADD 157.0.0.0 MASK 155.0.0.0 157.55.80.1 IF 1
#              The route addition failed: The specified mask parameter is invalid. (Destination & Mask) != Destination.
#
# Examples:
#
#     > route PRINT
#     > route PRINT -4
#     > route PRINT -6
#     > route PRINT 157*          .... Only prints those matching 157*
#
#     > route ADD 157.0.0.0 MASK 255.0.0.0  157.55.80.1 METRIC 3 IF 2
#              destination^      ^mask      ^gateway     metric^    ^
#                                                          Interface^
#       If IF is not given, it tries to find the best interface for a given
#       gateway.
#     > route ADD 3ffe::/32 3ffe::1
#
#     > route CHANGE 157.0.0.0 MASK 255.0.0.0 157.55.80.5 METRIC 2 IF 2
#
#       CHANGE is used to modify gateway and/or metric only.
#
#     > route DELETE 157.0.0.0
#     > route DELETE 3ffe::/32
#
# arp -a exited with status code: 0
# STDOUT:
#
# Interface: 192.168.232.1 --- 0xd
#   Internet Address      Physical Address      Type
#   192.168.232.254       00-50-56-eb-b6-cc     dynamic
#   192.168.232.255       ff-ff-ff-ff-ff-ff     static
#   224.0.0.5             01-00-5e-00-00-05     static
#   224.0.0.7             01-00-5e-00-00-07     static
#   224.0.0.22            01-00-5e-00-00-16     static
#   224.0.0.251           01-00-5e-00-00-fb     static
#   224.0.0.252           01-00-5e-00-00-fc     static
#   239.255.255.250       01-00-5e-7f-ff-fa     static
#   255.255.255.255       ff-ff-ff-ff-ff-ff     static
#
# Interface: 192.168.1.13 --- 0x11
#   Internet Address      Physical Address      Type
#   192.168.1.1           34-98-b5-5c-8b-2e     dynamic
#   192.168.1.3           3c-06-30-28-23-85     dynamic
#   192.168.1.6           2c-9e-00-71-6a-c0     dynamic
#   192.168.1.7           3c-06-30-13-c2-15     dynamic
#   192.168.1.8           d0-c2-4e-16-97-74     dynamic
#   192.168.1.254         68-9c-e2-71-2f-41     dynamic
#   192.168.1.255         ff-ff-ff-ff-ff-ff     static
#   224.0.0.5             01-00-5e-00-00-05     static
#   224.0.0.7             01-00-5e-00-00-07     static
#   224.0.0.22            01-00-5e-00-00-16     static
#   224.0.0.251           01-00-5e-00-00-fb     static
#   224.0.0.252           01-00-5e-00-00-fc     static
#   239.255.255.250       01-00-5e-7f-ff-fa     static
#
# Interface: 192.168.56.1 --- 0x12
#   Internet Address      Physical Address      Type
#   192.168.56.255        ff-ff-ff-ff-ff-ff     static
#   224.0.0.5             01-00-5e-00-00-05     static
#   224.0.0.7             01-00-5e-00-00-07     static
#   224.0.0.22            01-00-5e-00-00-16     static
#   224.0.0.251           01-00-5e-00-00-fb     static
#   224.0.0.252           01-00-5e-00-00-fc     static
#   239.255.255.250       01-00-5e-7f-ff-fa     static
#
# Interface: 192.168.228.1 --- 0x15
#   Internet Address      Physical Address      Type
#   192.168.228.254       00-50-56-ee-c0-cc     dynamic
#   192.168.228.255       ff-ff-ff-ff-ff-ff     static
#   224.0.0.5             01-00-5e-00-00-05     static
#   224.0.0.7             01-00-5e-00-00-07     static
#   224.0.0.22            01-00-5e-00-00-16     static
#   224.0.0.251           01-00-5e-00-00-fb     static
#   224.0.0.252           01-00-5e-00-00-fc     static
#   239.255.255.250       01-00-5e-7f-ff-fa     static
#   255.255.255.255       ff-ff-ff-ff-ff-ff     static
#
#
# Process finished with exit code 0
#
#  Output from Linux VM:
# C:\Users\devops\PycharmProjects\NetworkAutomation2\.venv\Scripts\python.exe "C:\Users\devops\PycharmProjects\NetworkAutomation2\Asyncio Automation\asyncio_shellcmd_subprocess.py"
# Command output from 192.168.0.90:
# SSH connection failed to 192.168.0.90: Process exited with non-zero exit status 127
# Command output from 192.168.0.90:
# devops   tty1         2023-12-28 20:30
# devops   pts/0        2024-01-10 16:05 (192.168.0.93)
#
# Process finished with exit code 0
# '''