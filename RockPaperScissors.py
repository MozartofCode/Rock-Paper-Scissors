"""
A Rock, Paper, Scissors Game (Against the computer)
@Language: Python

@author: Bertan Berker
"""

import random
import time

OPTIONS = ["r", "p", "s"]

MOVES = {"r": "Rock", "p": "Paper", "s": "Scissors"}

SCORE = {"Player": 0, "Computer": 0}


def init():
    """
    Initializes and explains the game
    :return: the name of the player
    """

    print("Welcome to the World of Rock, Paper, Scissors")
    print("-" * 100)
    player_name = input("My name is Apollo. What is your name?: ")
    print("-" * 100)
    print("Nice to meet you " + player_name)
    print("-" * 100)
    print("Let's start the game. The one who gets to 2 points wins!")
    print("-" * 100)

    return player_name


def is_game_over():
    """
    :return: Returns true if the game is over (meaning either the player or the computer achieved 2 points)
    """

    return SCORE["Player"] == 2 or SCORE["Computer"] == 2


def combinations(player, computer, player_name):
    """
    The game is played and the moves are printed. In addition, the scoring is updated in accordance to
    the winner of the round

    :param player: Players move (r, p, s)
    :param computer: Computers move (r, p, s)
    :param player_name: Name of the player

    :return: None
    """

    print(MOVES[player] + " vs " + MOVES[computer])

    if computer == player:
        print("Tie, No points for anyone.")

    elif computer == OPTIONS[0] and player == OPTIONS[1]:
        print("One point for " + player_name)
        SCORE["Player"] += 1

    elif computer == OPTIONS[1] and player == OPTIONS[0]:
        print("One point for Apollo")
        SCORE["Computer"] += 1

    elif computer == OPTIONS[1] and player == OPTIONS[2]:
        print("One point for " + player_name)
        SCORE["Player"] += 1

    elif computer == OPTIONS[2] and player == OPTIONS[1]:
        print("One point for Apollo")
        SCORE["Computer"] += 1

    elif computer == OPTIONS[0] and player == OPTIONS[2]:
        print("One point for Apollo")
        SCORE["Computer"] += 1

    elif computer == OPTIONS[2] and player == OPTIONS[0]:
        print("One point for " + player_name)
        SCORE["Player"] += 1


def result():
    """
    Prints who won the game
    :return: None
    """

    print("Game Over!")
    print("-" * 100)

    if SCORE["Player"] > SCORE["Computer"]:
        print("You Win!!!")
    else:
        print("I Win!!!")


def game_play():
    """
    The main gameplay function that initializes the game and that calls the proper functions to play
    rock, paper, scissors until there is a winner in the game

    :return: None
    """

    name = init()

    while not is_game_over():

        player_choice = input("Rock (r), Paper (p), Scissors (s) ?: ")
        computer_choice = random.choice(OPTIONS)

        print("-" * 100)

        if player_choice not in OPTIONS:
            print("Please enter a valid key!")
            print("-" * 100)

        else:
            combinations(player_choice, computer_choice, name)
            print("-" * 100)

        print(name + ": " + str(SCORE["Player"]))
        print("Apollo: " + str(SCORE["Computer"]))
        print("-" * 100)
        time.sleep(1.5)

    result()


if __name__ == "__main__":
    game_play()