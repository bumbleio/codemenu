import random
import time

max_users = 4
count_down_secs = 10
roll = True
user_set = set() # this is a set for no duplicate names


def coin_flip():
    coinflip = ['head' , 'tail']
    return (random.choice(coinflip))

def get_user_selection():
    return input("Please make selection: ")

def select_spinner():
    pass

def add_user(new_user):
    print("User count on active table = " + str(len(user_set)))
    # should use list or tuble so stop duplicate names
    if len(user_set) < max_users:
        user_set.add(new_user)
    else:
        print("Maximun users reached on this table")
    
def list_active_users():
    print(user_set)

def remove_user(existing_user):
    user_set.remove(existing_user)

def check_user_exists():
    # check if user exists or not
    pass







while roll:
    print("---TwoUp Game---")
    print("")
    print("1: Add User")
    print("2: Remove User")
    print("3: List Active Users")
    print("r: Start Round")
    print("X: Exit Game")
    selection = get_user_selection()
    if selection == '1':
        user_name = input("add user name to play: ")
        add_user(user_name)
    elif selection == '2':
        user_name = input("reomve user from game: ")
        remove_user(user_name)
    elif selection == '3':
        list_active_users()
    elif selection == 'r':
        coin1 = coin_flip()
        coin2 = coin_flip()
        print(coin1 + " " + coin2)
    elif selection == 'X':
        break





### needs to learn asyncio module to allow users to join in the 20 second interval


