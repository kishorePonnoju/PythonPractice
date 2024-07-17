import os

command = 'ping -c 1 google.com'

result = os.system(command)

if result != 0:
    print("command is not successful")
else:
    print(result)