import time

import myparamiko # myparamiko.py should be in the same directory with this script (or in sys.path)

# Define the switch and routers information
switch = {'server_ip': '10.1.1.1', 'server_port': 22, 'user': 'admin', 'passwd': 'cisco'}
routers = [
    {'hostname': '10.1.1.10', 'password': 'cisco'},
    {'hostname': '10.1.1.20', 'password': 'cisco'},
    {'hostname': '10.1.1.30', 'password': 'cisco'}
]

# Sh run commands to be executed on the routers
# sh_run_commands = [
#     'terminal length 0\n',
#     'enable\n',
#     'cisco\n',  # this is the enable command,
#     'show run\n'
# ]

# creating a list of dictionaries (of devices)
#routers = [router1, router2, router3]

# iterating over the list (over the devices) and backup the config
for router in routers:
    client = myparamiko.connect(**switch)
    switch_shell = myparamiko.get_shell(client)

    myparamiko.send_command(switch_shell, f'ssh {router["hostname"]}', 3)
    myparamiko.send_command(switch_shell, router["password"], 3)  # The '\n' is appended within the function


    print(f'Sending commands: ')
    myparamiko.send_command(switch_shell, 'terminal length 0', 3)
    myparamiko.send_command(switch_shell, 'enable', 3)
    myparamiko.send_command(switch_shell, 'cisco', 3)
    myparamiko.send_command(switch_shell, 'show run', 3)
    time.sleep(3)



    output = myparamiko.show(switch_shell)

    # processing the output
    # print(output)
    output_list = output.splitlines()
    output_list = output_list[11:-1]
    # print(output_list)
    output = '\n'.join(output_list)
    # print(output)

    # creating the backup filename
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    file_name = f'{router["hostname"]}_{year}-{month}-{day}.txt'
    print(file_name)

    # writing the backup to the file
    with open(file_name, 'w') as f:
        f.write(output)

myparamiko.close(client)

