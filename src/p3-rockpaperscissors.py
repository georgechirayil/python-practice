choice = "paper"  # Computer chooses paper.
print("rock-paper-scissors: type here:     ")
player = input ()

while player == choice:
    print ("Game is a tie. Please try again.")
    
player = input()
if player == "rock":
    if choice == "scissors":
        print ("Congratulations. You win.")
    else:
        print ("Sorry - Computer wins.")
elif player == "paper":
    if choice == "scissors":
        print ("Sorry - computer wins.")
    else:
        print ("Congratulations. You win.")
elif player == "scissors":
    if choice == "rock":
        print ("Sorry computer wins.")
    else: 
        print ("Congratulations You win.")
else:
    print ("Error: select one of: rock,paper,scissors")