"""Requirements – Stage 1: Write a program that plays Rock, Paper, Scissors. Ask
the user for their choice of Rock, Paper, or Scissors (you can ask them for a
number 1, 2, or 3). Have the computer also “choose” Rock, Paper, or Scissors.
(Hint: you can use the randint function from the Python random module. There
are other similar functions in this same random module that can be used.) Print
what the user chose and what the computer chose, and the outcome of the
round. See sample messages below.
Stage 2: Add logic into your program to add in a while loop so that if the user
does not win, it will play again. Once the user wins, it will stop looping and the
program will end. See sample messages below."""
import random

def ask_for_int():
    while True:
        try:
            user_input = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
            if user_input not in [1, 2, 3]:
                print("Invalid input. Please enter 1, 2, or 3. Try again.")
            else:
                return user_input
        except ValueError:
            print("Please only enter an integer. Try again.")

def determine_outcome(user_choice, computer_choice):
    outcomes = [
        ["Tie", "Computer", "Human"],
        ["Human", "Tie", "Computer"],
        ["Computer", "Human", "Tie"]
    ]
    outcome = outcomes[user_choice - 1][computer_choice - 1]
    return outcome

human_wins = 0
computer_wins = 0

while True:
    user_choice = ask_for_int()
    computer_choice = random.randint(1, 3)

    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    print(f"You chose {choices[user_choice]}")
    print(f"The computer chose {choices[computer_choice]}")

    outcome = determine_outcome(user_choice, computer_choice)

    if outcome == "Tie":
        print("It's a tie!")
    else:
        print(f"{outcome} wins!")

    if outcome == "Human":
        human_wins += 1
    elif outcome == "Computer":
        computer_wins += 1

    print(f"Human: {human_wins} Computer: {computer_wins}")

    if human_wins == 2:
        print("You've won twice! Game over.")
        break
    elif computer_wins == 2:
        print("Computer has won twice! Game over.")
        break

print("Goodbye!")
