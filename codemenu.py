import os
import platform


#log
# Next - clean up function list projects, once user selected projects it shoudl really list all files in teh project and allow the user to select one or all. 
# Right now it assumes there is ony one script file and it has teh same name as teh parent directory with .py extension

root_directory = os.getcwd()
os_version = platform.system()

# check os version and set project directory
if os_version == 'Windows':
    project_directory = root_directory + '\projects'
    hackerrank_directory = root_directory + '\hackerrank'
else:
    project_directory = root_directory + '/projects'
    hackerrank_directory = root_directory + '/hackerrank'



def get_input():
    return int(input('PLease select menu item:'))

def list_settings():
    pass

def list_projects(directory):
    project_list = os.listdir(path=directory)
    projectdict = {}
    count = 1
    print("Project list ")
    for project in project_list:
        print(str(count) + ': ' + project)
        projectdict[count] = project
        count += 1
    # Need to create dictionary number : directory name
    print(projectdict)
    project_number = int(input('Please select project by number'))
    project_directory_file = (projectdict.get(project_number))
    
    # this will wokr only for windows right now
    file_read = directory + '\\' + project_directory_file + '\\' + project_directory_file + '.py'
    open_file = open(file_read, 'r')
    print(open_file.read())

def show_code(dictionary):
    pass



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
    list_projects(project_directory)
elif user_selection == 3:
    list_projects(hackerrank_directory)
    










# Tags
# #empty_function with pass