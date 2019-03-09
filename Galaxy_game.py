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
        # print instructions for how to play the game
        print("Welcome to GalaxyCo, learn to budget while building your own planet!")
        ready = input("When you're ready to play, press y.")
        if ready.lower() != "y":
            print("Sorry, enter y to play!")
            continue
        else:

            while playing:
                item_count = 0
                print("""Your current budget is 500 booleans. 
                You must purchase three items for your planet but don't go over budget!""")
                print("Level 1 Menu:")
                for i in level_one_menu:
                    print(i)

                try:
                    item_purchased = input("What would you like to purchase?")

                except ValueError:
                    print("Please enter a valid response.")
                    continue

                else:
                    if item_purchased == "":
                        print("Please enter a valid response")
                        continue
                    else:
                        # loop through menu one items
                        # if item does not match any items raise error
                        # if it does match append to list
                        # retrieve object and deduct cost from budget
                        # cost of item should be deducted from budget: def purchase_item()
                        print("You have added an " + item_purchased + " to your list.")
                        item_count += 1
                    # when item count == 3 break
                    if item_count == 3:
                        break

            # determine if EE has won the game.

        gameover = input("Would you like to play again? Y or N").lower()

        if gameover[0].lower() == 'y':
            continue

        else:
            print("Thanks for playing!")
            break
