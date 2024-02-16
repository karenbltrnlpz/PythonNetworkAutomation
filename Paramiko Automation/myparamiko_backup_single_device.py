import myparamiko as mp # myparamiko.py should be in the same directory with this script (or in sys.path)
import time


switch = {'server_ip':'10.1.1.1', 'server_port': '22', 'user': 'admin', 'passwd': 'cisco'}
client = mp.connect(**switch)
shell = mp.get_shell(client)

mp.send_command(shell, 'terminal length 0')
mp.send_command(shell, 'enable')
mp.send_command(shell, 'cisco')  # this is the enable command
mp.send_command(shell, 'show run')

# added delay to allow the switch to get the running config
# this is important to allow script to save the running config to the text file
time.sleep(3)

output = mp.show(shell) # getting rid of the 100k buffer to see if this script still shows
# processing the output
# print(output)
output_list = output.splitlines()

# starting from index 11 to output the commands to the text file to save the configuration
# aka list slicing
output_list = output_list[11:-1]
# print(output_list) it will join the output list with \n elements which is basically an enter blank space
output = '\n'.join(output_list)
print(output)

# creating the backup filename
from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

# creating the file name
file_name = f'{switch["server_ip"]}_{year}-{month}-{day}.txt'
print(file_name)

# writing the backup to the file
with open(file_name, 'w+') as f:
    f.write(output)

mp.close(client)
