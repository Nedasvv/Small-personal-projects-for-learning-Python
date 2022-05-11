import random
ties = 0
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    while True:
        user_input = input("Type in Rock/Paper/Scissors or press Q to quit: ").lower()
        if user_input == "q":
            break

        if user_input not in options:
            continue

        random_number = random.randint(0, 2)
        computer_pick = options[random_number]

        computer_pick = computer_pick.capitalize()
        user_input = user_input.capitalize()
        print("Computer picked: " + computer_pick)
        print("You've picked: " + user_input)
        if user_input == "Rock" and computer_pick == "Scissors":
            user_wins += 1
            print("You've won! ")

        elif user_input == "Paper" and computer_pick == "Rock":
            user_wins += 1
            print("You've won! ")

        elif user_input == "Scissors" and computer_pick == "Paper":
            user_wins += 1
            print("You've won! ")

        elif user_input == computer_pick:
            ties += 1
            print("It's a tie! ")

        else:
            print("You've lost ")
            computer_wins += 1

        print("Computer wins: " + str(computer_wins))
        print("Your wins: " + str(user_wins))
        print("Ties: " +str(ties))


        print("You won " + str(user_wins) + " time(s) " )
        print("The computer won " + str(computer_wins) + " time(s) ")
        if user_wins > computer_wins:
            print("You have more wins. ")
        elif user_wins == computer_wins:
            print("You and the computer have the same amount of wins.")
        else:
            print("The computer has more wins than you. ")

    user_input = input("Would you like to play again? yes/no ").lower()

    if user_input == "yes":
        user_input = input("Would you like to  wipe the scores? ").lower()
        if user_input == "yes":
            ties = 0
            user_wins = 0
            computer_wins = 0

    else:
        quit()