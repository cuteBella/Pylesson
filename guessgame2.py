import random
import easygui

while True:
    # paper = 0, scissors = 1, stone = 2
    intComputer = random.randrange(0, 3)

    message = "please make your choice:"
    strPlayer = easygui.buttonbox(msg = message, title = "choice", choices=("paper", "scissors", "stone", "end"))

    if strPlayer == "end":
        break
    else:
        choices = ["paper", "scissors", "stone"]
        intPlayer = choices.index(strPlayer)
        a = intPlayer - intComputer
        result = ["tie", "win", "lose"]
        message = "computer choose " + choices[intComputer] + ", you " + result[a % 3]
        easygui.msgbox(msg = message)