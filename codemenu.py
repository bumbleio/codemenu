import os

root_directory = os.getcwd()
# This currently only works on windows. Slash will need to change for unix
# need to put a if OS windows then or unix
project_directory = root_directory + '\projects'


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
print('3: ???????')
user_selection = (get_input())
if user_selection == 1:
    list_settings()
elif user_selection == 2:
    list_projects()
    








# Tags
# #empty_function with pass