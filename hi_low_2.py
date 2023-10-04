# A number guessing game with a user-specified range.


# Import the random and math modules.
import random
import math


# Prompt the user for the maximum number and read it.
max_target = int(input("What should the highest possible number be? "))

# Choose a random number from 1 and the maximum.

# Calculate the number of guesses to give the user.
max_guesses = int(math.log2(max_target) + 1)

# Do the following for the number of times the user can guess:

	# Tell the user how many guesses he has left.

	# Prompt the user for a number and read it. This is his guess.

	# If the guess is correct:

		# Tell the user that he won.

		# End the program.

	#  Otherwise, if the guess is too high:

		# Tell the user his guess was too high.

	#  Otherwise, if the guess is too low:

		# Tell the user his guess was too low.

# All guesses are used up. Tell the user he lost the game.
