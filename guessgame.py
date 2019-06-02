import random
import easygui

while True:
    computer = random.choice(["paper", "scissors", "stone"])
    #computer = "paper"
    #print(computer)

    message = "please make your choice:"
    player = easygui.buttonbox(msg = message, title = "choice", choices=("paper", "scissors", "stone", "end"))
    #print(player)

    if player == "end":
        break
    else:
        if player == "paper" and computer == "paper":
            result = "computer choose paper, you tie!"
        if player == "paper" and computer == "scissors":
            result = "computer choose scissors, you lose!"
        if player == "paper" and computer == "stone":
            result = "computer choose stone, you win! you are sooooo smart!"

        if player == "scissors" and computer == "paper":
            result = "computer choose paper, you win! you are sooooo smart!"
        if player == "scissors" and computer == "scissors":
            result = "computer choose scissors, you tie!"
        if player == "scissors" and computer == "stone":
            result = "computer choose stone, you lose!"

        if player == "stone" and computer == "paper":
            result = "computer choose paper, you lose!"
        if player == "stone" and computer == "scissors":
            result = "computer choose scissors, you win! you are sooooo smart!"
        if player == "stone" and computer == "stone":
            result = "computer choose stone, you tie!"
        easygui.msgbox(msg = result)