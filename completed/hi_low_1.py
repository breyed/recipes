# A simple number guessing game.

import random

# Choose a random number between 1 and 100.
target = random.randint(1, 100)

# Let the user guess 8 times.
for _ in range(8):
	guess = int(input("What is your guess? "))
	if guess == target:
		print("Congratulations, you won!")
		exit()
	elif guess > target:
		print("Too high.")
	else:
		print("Too low.")

# After 8 wrong guesses, tell the user he lost the game.
print("Sorry. You're out of guesses. Maybe next time.")
