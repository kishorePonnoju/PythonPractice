import os

command = 'ping -n 1 google.com'

result = os.system(command)

if result != 0:
    print("command is not successful")
else:
    print("Command is successful")