import random #random module used for to choose computer random things 

choices = ["rock", "paper", "scissor"]

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock, paper or scissor: ").lower()
    print("Please choose from rock, paper or scissor ")

print("computer: ", computer)
print("player: ", player)
print("result")