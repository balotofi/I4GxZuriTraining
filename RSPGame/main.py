import random

play_options = [
    "rock", 
    "paper", 
    "scissors"]


# def user_play_rps(play):
user_play_rps = input("Type your play ['rock', 'paper', 'scissors']:")

# def cpu_play_rps():
cpu_play_rps = random.choice(play_options)
print(f"cpu played {cpu_play_rps} and you played {user_play_rps}")


# def battle():
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

