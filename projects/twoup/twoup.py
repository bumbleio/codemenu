import random
import time

max_users = 4
count_down_secs = 10
roll = True
user_set = {} 
bet = 5
user_bets = {}
house_balance = int(1000)
#sum_of_bets_heads = 0
# sum_of_bets_tails = 0


def coin_flip():
    coinflip = ['head' , 'tail']
    return (random.choice(coinflip))

def get_user_selection():
    return input("Please make selection: ")

def select_spinner():
    pass

def add_user(new_user, starting_balance=100):
    print("User count on active table = " + str(len(user_set)))
    # should use list or tuble so stop duplicate names
    if len(user_set) < max_users:
        user_set.update({new_user: starting_balance})
    else:
        print("Maximun users reached on this table")
    
def list_active_users():
    print(user_set)

def remove_user(existing_user):
    user_set.pop(existing_user)
    user_bets.pop(existing_user)
    # remove 

def check_user_exists():
    # check if user exists or not
    pass


def place_you_bets():
    # sets up peoples bet
    for user in user_set:
        heads_or_tails = input(user + " place your bet T for tails, H for heads: ")
        # vaidate heads or tails is selected
        user_bets.update({user : heads_or_tails})
        validate_bets(user, heads_or_tails)
    print('final user bets ' + str(user_bets))


def validate_bets(user , heads_or_tails):
    bet_value = user_bets[user]
    if bet_value != 'T' and bet_value != 'H'  :
        heads_or_tails = input(user + ' incorrect value please repeat: ')
        user_bets.update({user : heads_or_tails})
        validate_bets(user , heads_or_tails)
        
def list_active_bets():
    sum_of_bets_heads = 0
    sum_of_bets_tails = 0
    print('final user bets ' + str(user_bets))
    for user, bet in user_bets.items():
        print("the best is: " + bet)
        if bet == 'T':
            sum_of_bets_tails += 1
        elif bet == 'H':
            sum_of_bets_heads += 1
    print('tailscount= ' + str(sum_of_bets_tails))
    print('headscount= ' + str(sum_of_bets_heads))
    bet_balance = sum_of_bets_tails - sum_of_bets_heads
    if bet_balance != 0:

    #abs function make a negative number positive and keeps a positive number positive
        bet_balance_count = abs(int(bet_balance))
        for i in range(bet_balance_count):
            print(i)
            if int(bet_balance) > 0:
                user_bets.update({'house' + str(i) : 'H'})
            elif int(bet_balance) < 0:
                user_bets.update({'house' + str(i) : 'T'})

            # create house accounts with corresponding bets
        print ("final bets are : " + str(user_bets))
    else:
        print('balance even')




# cover bets ie if all users one side they have to play against the house hence house needs enough to cover these situtaions
#  tally numbers of head bets and number of tails bets. if equal good if not house will have to cover...
#
#




while roll:
    print("---TwoUp Game---")
    print("")
    print("1: Add User")
    print("2: Remove User")
    print("3: List Active Users")
    print("4: List Active bets")
    print("r: Start Round")
    print("X: Exit Game")
    selection = get_user_selection()
    print(selection)
    
    if selection == '1':
        user_name = input("add user name to play: ")
        add_user(user_name)
    elif selection == '2':
        user_name = input("remove user from game: ")
        remove_user(user_name)
    elif selection == '3':
        list_active_users()
    elif selection == '4':
        list_active_bets()
    elif selection == 'r':
        place_you_bets()
        coin1 = coin_flip()
        coin2 = coin_flip()
        print(coin1 + " " + coin2)
    elif selection == 'X':
        break

### needs to learn asyncio module to allow users to join in the 20 second interval


