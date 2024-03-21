print("Name : Jay Kumar\nURN : 2203844 ")
import random
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def play_game(initial_pot):
    pot = initial_pot
    max_pot = initial_pot
    rolls = 0

    while pot > 0:
        rolls += 1
        dice_sum = roll_dice()
        if dice_sum == 7:
            pot += 4
        else:
            pot -= 1
        max_pot = max(max_pot, pot)

    return rolls, max_pot
# Input the initial amount of money
initial_pot = float(input("Enter the initial amount of money: "))
# Play the game
rolls, max_pot = play_game(initial_pot)
# Print the results
print("Number of rolls:", rolls)
print("Maximum amount of money in the pot:", max_pot)
