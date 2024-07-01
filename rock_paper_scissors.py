import random #random module used for to choose computer random things 

while True:
    choices = ["rock", "paper", "scissor"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissor: ").lower()
        
        if player == "rock":
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("You Lose")
            if computer == "scissor":
                print("computer: ", computer)
                print("player: ", player)
                print("You Win")
        elif player == "paper":
            if computer == "scissor":
                print("computer: ", computer)
                print("player: ", player)
                print("You Lose")
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("You Win")
        elif player == "scissor":
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("You Lose")
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("You Win")
    playAgain = input("Play Again: (yes|no)")
    if playAgain != "yes":
        break
print("GG. see ya!")