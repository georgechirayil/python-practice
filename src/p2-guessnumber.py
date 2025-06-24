# This program select a number between 1 and
# 10 and allows a user (player) to guess what
# it is
choice = 7  # The number selected by the computer 


# Prompt the user, indicating what is expected 
print ("Please guess a number between 1 and 10: ")

# Read the player's input from the keyboard 
playerchoice = int(input()) # convert from string


# Print the outcome of the game.
if choice == playerchoice:
    print("You win!)
else:
    print("Sorry' you lose.")

