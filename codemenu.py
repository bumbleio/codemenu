import os
import platform


#log
# Next - add project files and list code for a project

root_directory = os.getcwd()
os_version = platform.system()

# check os version 
if os_version == 'Windows':
    project_directory = root_directory + '\projects'
else:
    project_directory = root_directory + '/projects'



def get_input():
    return int(input('PLease select menu item:'))

def list_settings():
    pass

def list_projects():
    project_list = os.listdir(path=project_directory)
    count = 1
    for project in project_list:
        print(str(count) + ': ' + project)
        count += 1



print('-------' * 3 )
print('1: Settings')
print('2: Show all Projects')
print('3: Hacker Rank')
print('4: Search projects by tag')
print('5: Projects raspberrypi.org ') 
print('6: Docker Files')
print('Cheat Sheets')
user_selection = (get_input())
if user_selection == 1:
    list_settings()
elif user_selection == 2:
    list_projects()
    








# Tags
# #empty_function with pass