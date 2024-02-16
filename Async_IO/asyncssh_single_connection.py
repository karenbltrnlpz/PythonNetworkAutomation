import asyncio
import asyncssh

# connecting and running, we need the host, user name, password
# and the command we want to send to the server
async def connect_and_run(host, username, password, commands):
    # authenticate to remote ssh daemon, the value after the equal sign are
    # the arguments that are defined in the  connect_and_run function. Since we
    # don't use the known host file, we set it equal to none, but if you want to verify the identity
    # of the host, then we use the file.
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        # coroutine - running command to the Linux VM using the run method
        # result = await connection.run(command)
        # return result


        #2. To run multiple commands (list or tuple)
        # initiating a list to hold the results of each command
        results = []
        for cmd in commands:
            result = await connection.run(cmd)
            results.append(result)
        # outside the for loop, return the results list
        return results


commands = ('/usr/sbin/ip addr', 'who', 'uname -a')
results = asyncio.run(connect_and_run('192.168.0.90', 'devops', 'Time4work!', commands))

# since a list of results (outputs) is expected,
# we need to iterate over them
for result in results:
    # STDOUT is an attribute of the result object
    print(f'STDOUT:\n {result.stdout}')
    # STDERR is an attribute of the result object
    print(f'STDERR:\n {result.stderr}')