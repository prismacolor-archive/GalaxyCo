#import galaxy_func
#import galaxy_items

# welcome message with instructions
# display the menu of things to choose from
# person should enter name of thing they wish to buy
# person should purchase three things

playing = True
budget = 500
points = 0
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

                    if item_purchased == "":
                        print("Please enter a valid response")
                        continue
                    # loop through menu one items
                    # if item does not match any items raise error

                except ValueError:
                    print("Please enter a valid response.")
                    continue

                else:
                            # if it does match append to list
                            # retrieve object and deduct cost from budget
                            # cost of item should be deducted from budget: def purchase_item()
                        print('You have added "' + item_purchased + '" to your list.')
                        item_count += 1
                        continue
                        # when item count == 3 break



            # determine if EE has won the game.

        gameover = input("Would you like to play again? Y or N").lower()

        if gameover[0].lower() == 'y':
            continue

        else:
            print("Thanks for playing!")
            break
