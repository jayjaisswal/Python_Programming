import random

def play_lucky_sevens(initial_pot):
  """
  Simulates playing Lucky Sevens until the pot is empty.

  Args:
      initial_pot: The starting amount of money in the pot.

  Returns:
      A tuple containing the number of rolls taken and the maximum pot size.
  """
  pot = initial_pot
  max_pot = pot
  num_rolls = 0

  # Loop until the pot is empty
  while pot > 0:
    # Roll the dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    roll_sum = die1 + die2

    # Check if the player wins or loses
    if roll_sum == 7:
      pot += 4
    else:
      pot -= 1

    # Update max pot
    max_pot = max(max_pot, pot)

    num_rolls += 1

  return num_rolls, max_pot

# Get the initial pot amount from the user
initial_pot = int(input("Enter the initial pot amount: "))

# Play the game and get results     
num_rolls, max_pot = play_lucky_sevens(initial_pot)

print("It took", num_rolls, "rolls to empty the pot.")
print("The maximum amount of money in the pot was:", max_pot)
