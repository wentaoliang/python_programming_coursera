'''This is a python document,
   Week 2 mini-project/
   Assignment: Rock-paper-scissors-lizard-Spock'''
#helper functions
import random

def name_to_number(name):
    # converts five choices 'Rock-paper-scissors-lizard-Spock' a number
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else :
        return "error: 'input name doesn't match any rules.'"


def number_to_name(number):
    # converts a number in the range 0 to 4 into its corresponding name as a string
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "error:'input number doesn't match any rule.'"

def rspls(name):
    #converts name to player_number use name_to_number functions
    #compute random guess for comp_number using random.randrange
    #compute difference of player_number and comp_number mudulo five

    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)

    print "Player chooses" + " " +  name
    print "Computer chooses" + " " + number_to_name(comp_number)

    if (comp_number + 1) % 5 == player_number:
        print "Player wins!"
    elif (comp_number + 2) % 5 == player_number:
        print "Player wins!"
    elif comp_number == player_number:
        print "Player and computer tie!"
    else:
        print "Computer wins!"
    print ""

#test code below
rspls("rock")
rspls("Spock")
rspls("paper")
rspls("lizard")
rspls("scissors")
