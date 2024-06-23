import random

choices = ["rock", "paper", "scissors"]

computer_wins = 0
user_wins = 0
ties = 0

print("\nWelcome to The Rock-Paper-Scissors!")
print('''
RULES:
    ★ Choose one of the following: rock, paper, or scissors.
    ★ Rock beats scissors, scissors beats paper, and paper beats rock.
    ★ The total score will be displayed at the end of the game.
''')

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"\nYou chose       : {user_choice}")
    print(f"Computer chose  : {computer_choice}")

    if user_choice == "rock" and computer_choice == "scissors":
        print(">> You won! Rock crushes scissors.")
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print(">> You won! Paper covers rock.")
        user_wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print(">> You won! Scissors cuts paper.")
        user_wins += 1
    elif user_choice == computer_choice:
        print(">> It's a tie!")
        ties += 1
    else:
        print(f">> You lost! {computer_choice.capitalize()} beats {user_choice}.")
        computer_wins += 1

    print("\n-------------------------")
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    print("-------------------------\n")
    if play_again != 'y':
        break

total_games = user_wins + computer_wins + ties
print(f'''>>> Game Summary:
    Total games played: {total_games}
    You won: {user_wins} games
    Computer won: {computer_wins} games
    Ties: {ties}
''')
print("Thanks for playing! Visit again Soon!")
