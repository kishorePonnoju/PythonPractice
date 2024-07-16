"""Module providing a File Operation in python"""

# FileOPeration_jabber = open('Jabberwocky.txt','r')

# for line in FileOPeration_jabber:
#     print(line)
#     print(line.lstrip)

with open('Jabberwocky.txt','r') as jabber:
    lines = jabber.readline()


print(lines) # readline will give as string
print(lines[-1:]) # Print the lines in reverse  order

with open('Jabberwocky.txt') as Jabber:
    text = Jabber.read()
    
print(text)

for character in reversed(text):
    print(character, end='')
    
    
with open('Jabberwocky.txt','r') as Jabbber:
    while True:
        line = Jabbber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break
        
print('*'* 80)

with open('Jabberwocky.txt','r') as Jabbber:
    for line in Jabbber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break