import asyncio
import time

# SYNCHRONOUS
def sync_f():
    print('one ', end='')
    time.sleep(1)
    print('two ', end='')

# ASYNCHRONOUS
# this is an example of a coroutine
async def async_f():
    print('one ', end='')
    await asyncio.sleep(1)
    print('two ', end='')

# top level coroutine, aka application starting point
async def main():
    # creating a list of tasks consisting of 3 calls to coroutine async_f()
    # tasks = [async_f(), async_f(), async_f()]

    # you can also create a list comprehension to get the same result as the list above
    tasks = [async_f() for _ in range(3)]

    # scheduling the coroutine to run ASAP by gathering tasks using asyncio.gather()
    await asyncio.gather(*tasks)

# comparing asynchronous routine with synchronous in output and time

# to run the top level coroutine main() use asyncio.run(main())
print('Printing asynchronous output: \n')
start = time.time()
asyncio.run(main())
end = time.time()
print(f'Execution time (ASYNC): {end - start}')
print('\n')


print('Printing Synchronous output: \n')
start1 = time.time()
for _ in range(3):
    sync_f()
end1 = time.time()
print(f'Execution time (SYNC): {end1 - start1}')

# coroutines examples
# async def f():
#     pass #empty function
#
# # when f() is encountered and called inside g(), the g() function execution is suspended until f() returns
# async def g():
#     await f() # in other words 'pause here and come back to g() until f is ready'


# ''' Output:
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe C:\Users\belka\PycharmProjects\NetworkAutomation\Async_IO\implementing_asyncio.py
# Printing asynchronous output:
#
# one one one two two two Execution time (ASYNC): 1.011183500289917
#
#
# Printing Synchronous output:
#
# one two one two one two Execution time (SYNC): 3.001897096633911
#
# Process finished with exit code 0
#
# '''