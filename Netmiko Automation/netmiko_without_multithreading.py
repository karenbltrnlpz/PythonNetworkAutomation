from netmiko import ConnectHandler

# Getting the current timestamp, UNIX epoch to track time as the running total of seconds
import time
start = time.time()




# opening text file containing the devices' IPs and saving it to a list
with open('devices2.txt') as f:
    devices = f.read().splitlines()

for ip in devices:
    # Creating a dictionary with connection parameters
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'admin',
        'password': 'cisco',
        'port': 22, # optional, default 22
        'secret': 'cisco', # optional, default ''. This is the enable password
        'verbose': True # optional, default False
    }
    connection = ConnectHandler(**cisco_device)
    print('Entering the enable mode...')
    connection.enable()

    output = connection.send_command('sh run')

    # finding the name of the device using find_prompt() method
    prompt = connection.find_prompt()
    # getting rid of the hashtag using slicing to keep the name of the router
    # since the hashtag is at the end of the string, we do -1 after the colon to select
    # it and this will return a string without the hashtag
    hostname = prompt[0:-1]
    # print(hostname)

    # creating the backup filename
    from datetime import datetime

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day


    # creating the file name with date stamp
    filename = f'{hostname}_{year}-{month}-{day}_backup.txt'
    print(filename)

    # adding the configuration to the text file
    with open(filename, 'w') as backup_file:
        backup_file.write(output)
        print(f'Backup of {hostname} completed successfully')
        # printing hash signs to see the output clearer
        print('#' * 50)


    print('Closing connection...')
    connection.disconnect()

end = time.time()
print(f'Total execution time: {end - start}')

