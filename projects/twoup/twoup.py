import random
import time
import os

max_users = 4
count_down_secs = 10
roll = True
user_list = {}
house_list = {}
bet = 5
user_bets = {}
house_balance = int(1000)
#sum_of_bets_heads = 0
# sum_of_bets_tails = 0

def clear_screen():
    os.system('clear')
    print(" ")

def coin_flip():
    coinflip = ['head' , 'tail']
    return (random.choice(coinflip))

def get_user_selection():
    return input("Please make selection: ")

def validate_user(user):
    pass

def select_spinner():
    pass

def add_user(new_user, starting_balance=100):
    user_exists = check_user_exists(new_user)
    print(user_exists)   
    if user_exists == False:
    # should use list or tuble so stop duplicate names
        if len(user_list) < max_users:
            print("*******************adding user**********************")
            user_list.update({new_user: starting_balance})
            list_active_users()
        else:
            print("Maximun users reached on this table")
    else:
        print("user " + new_user + " already exists")

def list_active_users():
    print(user_list)

def remove_user(existing_user):
    user_list.pop(existing_user)
    user_bets.pop(existing_user)
    
def check_user_exists(user):
    if user in user_list:
        return True
    else:
        return False
   

def place_you_bets():
    # sets up peoples bet
    for user in user_list:
        heads_or_tails = input(user + " place your bet T for tails, H for heads: ")
        # vaidate heads or tails is selected
        user_bets.update({user : heads_or_tails})
        validate_bets(user, heads_or_tails)

def validate_bets(user , heads_or_tails):
    bet_value = user_bets[user]
    if bet_value != 'T' and bet_value != 'H'  :
        heads_or_tails = input(user + ' incorrect value please repeat: ')
        user_bets.update({user : heads_or_tails})
        validate_bets(user , heads_or_tails)
        
def reconcile_bets():
    # need to reset the house list each time new bets are placed
    reset_house_list(user_bets)
    sum_of_bets_heads = 0
    sum_of_bets_tails = 0
    print('User bets: ' + str(user_bets))
    for user, bet in user_bets.items():
        if bet == 'T':
            sum_of_bets_tails += 1
        elif bet == 'H':
            sum_of_bets_heads += 1
    bet_balance = sum_of_bets_tails - sum_of_bets_heads
    if bet_balance != 0:
        #abs function makes a negative number positive and keeps a positive number positive
        bet_balance_count = abs(int(bet_balance))
        for i in range(bet_balance_count):
            if int(bet_balance) > 0:
                user_bets.update({'house' + str(i) : 'H'})
                # house_list.update({'house' + str(i) : 0})
                print('***********adding house user*****************')
                house_list['house' + str(i)] = 0
            elif int(bet_balance) < 0:
                user_bets.update({'house' + str(i) : 'T'})
                # house_list.update({'house' + str(i) : 0})
                print('***********adding house user*****************')
                house_list['house' + str(i)] = 0

            # create house accounts with corresponding bets
        print ("final bets with house to balance pool : " + str(user_bets))
    else:
        print('balance even')


def determine_winners_losers(coin1, coin2):
    print(coin1 + " " + coin2)
    if coin1 == 'head' and coin2 == 'head':
        for user, bet in user_bets.items():
            if bet == 'H':
                print(user + " has won")
                if user.startswith("house"):
                    reconcile_house_balance(user, "won")
                else:
                    reconcile_user_balace(user , "won")
            else:

                print(user + " has lost")
                if user.startswith("house"):
                    reconcile_house_balance(user, "lost")
                else:
                    reconcile_user_balace(user , "lost")

    elif coin1 == 'tail' and coin2 == 'tail':
        for user, bet in user_bets.items():
            if bet == 'T':
                print(user + " has won")
                if user.startswith("house"):
                    reconcile_house_balance(user, "won")
                else:
                    reconcile_user_balace(user , "won")

            else:
                print(user + " has lost")
                if user.startswith("house"):
                    reconcile_house_balance(user, "lost")
                else:
                    reconcile_user_balace(user , "lost")
    else:
        print('no winner re-roll')
    

def reconcile_user_balace(user, result):
    if result == 'won':
        # Normal Users
        new_user_balance = int(user_list[user]) + 5
        print(new_user_balance)
        user_list[user] = new_user_balance
       
    elif result == 'lost':
        new_user_balance = int(user_list[user]) - 5
        print(new_user_balance)
        user_list[user] = new_user_balance


def reconcile_house_balance(user, result):

    if result == 'won':
        # House
        house_list[user] = int(house_list[user]) + 5
        print(house_list)
        
    elif result == 'lost':
         # House
        house_list[user] = int(house_list[user]) - 5
        print(house_list)



def reset_house_list(user_bets):
    print('****************** resetting house user list you new round *****************')
    house_list.clear()

    # this allows me to remove an element while iterating through the list
    for key in list(user_bets.keys()):
        print(key)
        if key.startswith("house"):

            print('remove user here ' + key)
            del user_bets[key]

    print(house_list)
    print(user_bets)




def list_active_bets():
    print(user_bets)

def list_house_user_balances():
    print(house_list)



while roll:
    print("---TwoUp Game---")
    print("")
    print("1: Add User")
    print("2: Remove User")
    print("3: List Active Users")
    print("4: List Active bets")
    print("5: List House User bets")
    # have to merge list active bets and place your bets
    print("p: PLace your bets")
    print("r: Start Round")
    print("X: Exit Game")
    selection = get_user_selection()
    print(selection)
    
    if selection == '1':
        clear_screen
        user_name = input("add user name to play: ")
        add_user(user_name)
    elif selection == '2':
        clear_screen
        user_name = input("remove user from game: ")
        remove_user(user_name)
    elif selection == '3':
        clear_screen
        list_active_users()
    elif selection == '4':
        clear_screen
        list_active_bets()
    elif selection == '5':
        clear_screen
        list_house_user_balances()   
    elif selection == 'p':
        clear_screen
        place_you_bets()
        reconcile_bets()
    elif selection == 'r':
        coin1 = coin_flip()
        coin2 = coin_flip()
        determine_winners_losers(coin1, coin2)
    elif selection == 'X':
        break

# Need to validate user deoenst already exist when added and validate that a user exists when removed
# add / subtract house winnings or loses to wallet


