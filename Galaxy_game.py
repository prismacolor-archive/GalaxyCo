from galaxy_func import *
from galaxy_items import *

playing = True
points = 0
budget = 500
item_list = []
level_one_menu = ["river", "tree", "cornfield", "mountain", "gold", "bumblebees"]


def play_game():
    while True:
        print("Welcome to GalaxyCo, learn to budget while building your own planet!")
        ready = input("When you're ready to play, press y.")
        if ready.lower() != "y":
            print("Sorry, enter y to play!")
            continue
        else:
            print("""Your starting budget is 500 booleans. 
            You must purchase three items for your planet but don't go over budget!""")
            item_count = 0

            while item_count < 3:
                print("Level 1 Menu:")
                for i in level_one_menu:
                    print(i)

                try:
                    item_purchased = input("What would you like to purchase?")

                    # if item is not in list, kick an error
                    if item_purchased not in level_one_menu:
                            print("Please enter a valid response")
                            continue

                except ValueError:
                    print("Please enter a valid response.")
                    continue

                else:
                    # adds item to list and one to item count
                    print('You have added "' + item_purchased + '" to your list.')
                    item_count += 1
                    item_list.append(item_purchased)

                    for item in galaxy_items_list:
                        if item_purchased == item.name:
                            purchase_item(budget, item)
                    continue

            # determine if EE has won the game.
            if budget < 0:
                print("Oh dear, you are flat broke. Your budget is {]".format(budget))
            else:
                print("Great job! You made your purchases and have {} left to spare!".format(budget))

        gameover = input("Would you like to play again? Y or N").lower()

        if gameover[0].lower() == 'y':
            continue

        else:
            print("Thanks for playing!")
            break
