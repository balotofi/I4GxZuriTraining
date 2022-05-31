from random import random


play_options = {
    R: "rock", 
    P: "paper", 
    S: "scissors"}

def user_play_rps(play):
    play = input("Type your play [R, P, S]:")
    for option in play_options:
        if play == option:
            print("user played", option)

def cpu_play_rps():
    play = random.choice(R, P, S)
    for option in play_options:
        if play == option:
            print("cpu played", option)
    



if __name__ == main:
    run __name__
