import random
print("Welcome to Rock, Paper, Scissor game!")
rules="This game has only 1 point, so the one who wins first, is the winner. This is a ROCK, PAPER, SCISSOR game in which you have to enter a choice and the computer will give it's choice. Press enter to start!"
print(rules)
start_game=input('Press enter to start playing: \t')
choices = ('S','R','P')
player = input("Enter R for rock, P for Paper or S for scissor")

print("Your choice: ", player)

cpu=random.choice(choices)
print("Computer: ", cpu)

if player == "S" and cpu == "P":
    print("Yay! You won")
elif player == "S" and cpu == "R":
    print("Ohh no, you lost!")
elif player == "S" and cpu == "S":
    print("Draw")
elif player == "R" and cpu == "P":
    print("You Lost")
elif player == "R" and cpu == "S":
    print("You won")
elif player == "R" and cpu == "R":
    print("Draw")
elif player == "P" and cpu == "S":
    print("You lost")
elif player == "P" and cpu == "R":
    print("You won")
elif player == "P" and cpu == "P":
    print("Draw")
else: 
    print("Error! Invalid input! Please try again")