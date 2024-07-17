import os 

directory = os.path.dirname(os.path.abspath(__file__))

print(directory)

file_name= 'os_test.txt'

file_path = os.path.join(directory,file_name)

with open (file_name,'w') as file :
    file.write('This os module is Cool')
    
with open (file_name,'r') as file:
    message = file.read()
    
print(message)
    