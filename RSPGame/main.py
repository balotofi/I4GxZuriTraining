from random import random


play_options = {
    R: "rock", 
    P: "paper", 
    S: "scissors"}


def user_play_rps(play):
    play = input("Type your play ['R', 'P', 'S']:")
    for option in play_options:
        if play == option:
            print("user played", option)


def cpu_play_rps():
    play = random.choice('R', 'P', 'S')
    for option in play_options:
        if play == option:
            print("cpu played", option)


def battle():
    if user_play_rps == cpu_play_rps:
        print(f"Both players selected {user_play_rps}. It's a tie!")
    elif user_play_rps == "rock":
        if cpu_play_rps == "scissors":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
    elif user_play_rps == "paper":
        if cpu_play_rps == "rock":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
    elif user_play_rps == "scissors":
        if cpu_play_rps == "paper":
            print("Scissors beats paper! You win!")
        else:
            print("Rock beats scissors! You lose.")

if __name__ == main:
    run __name__
