"""Module providing a File Operation in python"""

FileOPeration_jabber = open('Jabberwocky.txt','r')

for line in FileOPeration_jabber:
    print(line)
    print(line.lstrip)
