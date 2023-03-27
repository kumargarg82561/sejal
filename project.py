import random

while True:
    playeraction = input("Enter a choice (rock, paper, scissors): ")
    actionpossible = ["rock", "paper", "scissors"]
    laptopaction = random.choice(actionpossible)
    print(f"\nYou chose {playeraction}, computer chose {laptopaction}.\n")

    if playeraction == laptopaction:
        print(f"Both players selected {playeraction}. It's a tie!")
    elif playeraction == "rock":
        if laptopaction == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif playeraction == "paper":
        if laptopaction == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif playeraction == "scissors":
        if laptopaction == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break