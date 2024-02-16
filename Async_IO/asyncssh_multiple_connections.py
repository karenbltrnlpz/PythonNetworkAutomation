import asyncio
import asyncssh

#authenticating and running, where host is the IP address of the remote ssh daemon
async def run_client(host, username, password, command):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        return await connection.run(command)

# defining top level coroutine which is the async app's starting point
# the coroutine will take a list of hosts and call or await the run
# client for each host in other words, this coroutine will spawn a
# task for each SSH connection
async def run_multiple_clients(hosts):
    # creating an empty list for the tasks
    tasks = []

    # iterating over the hosts calling the run client coroutine and adding
    # the newly created task to the list
    for host in hosts:
        # a host in the hosts list is a dictionary that has the host, username, password, and
        # command as keys
        task = run_client(host['host'], host['username'], host['password'], host['command'])
        # adding the task to the tasks list
        tasks.append(task)

    #scheduling the coroutines to run ASAP by gathering the
    # tasks using the gather method and return any exceptions, by default
    # the second argument is False. The gather method returns a list of aggregate values
    # we need to iterate over them
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # to put a number to the task
    i = 0
    for result in results:
        # adding the task number to each task by increments of 1
        #e.g first task will be 1, the second will be 2 and so on
        i +=1
        # handling if there were exceptions (error at runtime)
        if isinstance(result, Exception):
            # telling the user which task failed
            print(f'Task {i} failed: {str(result)}')
            # if there is an error on Linux, code 0 means there was no error
        elif result.exit_status != 0:
            print(f'Task {i} exited with status: {result.exit_status}')
            print(result.stderr, end='')
        else:
            print(f'Task {i} succeeded:')
            print(result.stdout, end='')

        # to see each iteration clearly
        print('#' *50)

# creating a list of dictionaries that hold the information on multiple hosts
# since I only have one host, I will spawn an SSH session on the same host and send a different
# command
hosts = [
    {'host': '192.168.0.90', 'username': 'devops', 'password': 'Time4work!', 'command': 'who'},
    {'host': '192.168.0.90', 'username': 'devops', 'password': 'Time4work!', 'command': 'uname -a'},
    {'host': '192.168.0.90', 'username': 'devops', 'password': 'Time4work!', 'command': '/usr/sbin/ip addr'}
]

# initiating the top level coroutine with run()
asyncio.run(run_multiple_clients(hosts))
