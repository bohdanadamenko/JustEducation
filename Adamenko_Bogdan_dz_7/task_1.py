import os
# list = [file for file in os.listdir() if file.endswith('.py')]
# print(list)

folder = 'project'
subfolder = 'app'
file_name = 'script.py'

path = [folder, subfolder, file_name]

print('\n'.join(path))