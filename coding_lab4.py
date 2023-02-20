#ROCK PAPER SCISSORS
import os
import secrets

os.system("cls")
print("Welcome to rock paper scissors!\n")

while True:
    message = input("Do you want to play? (Type 'yes' or 'no') ").lower()
    if message == 'yes':
        player_choice = (input("Do you choose ROCK, PAPER, or SCISSORS? ")).upper()
        computer_choice = secrets.choice(['ROCK','PAPER','SCISSORS'])
        print(f"\nThe computer chose {computer_choice}")
        if player_choice == 'ROCK':
            print("You chose ROCK.")
                 
            if computer_choice == 'ROCK':
                print("---------IT'S A TIE---------")
            elif computer_choice == 'PAPER':
                print("---------YOU LOSE---------")
            else:
                print("---------YOU WIN---------")
                
        elif player_choice == 'PAPER':
            print("You chose PAPER.")

            if computer_choice == 'ROCK':
                print("---------YOU WIN---------")
            elif computer_choice == 'PAPER':
                print("---------IT'S A TIE---------")
            else:
                print("---------YOU LOSE---------")

        elif player_choice == 'SCISSORS':
            print("You chose SCISSORS.")

            if computer_choice == 'ROCK':
                print("---------YOU LOSE---------")
            elif computer_choice == 'PAPER':
                print("---------YOU WIN---------")
            else:
                print("---------IT'S A TIE---------")

        else:
            print("That is not a valid option.")

    elif message == 'no':
        break
    
    else: 
        print("error")