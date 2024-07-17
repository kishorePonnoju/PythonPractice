import os

host = input('Host / IP Address to Ping: ')

command = (f'ping -n 1 {host}')

responce = os.popen(command).read()

print(responce)