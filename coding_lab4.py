
import os
import secrets

os.system("cls") #Clears screen for running program
print("Welcome to rock paper scissors!\n")

while True:
    response = input("Do you want to play? (Type 'yes' or 'no') ").lower()
    if response == 'yes':
        player_choice = (input("Do you choose ROCK, PAPER, or SCISSORS? ")).upper()
        computer_choice = secrets.choice(['ROCK','PAPER','SCISSORS'])
        print(f"\nThe computer chose {computer_choice}")
        if player_choice == 'ROCK':
            print("You chose ROCK.\n")
                 
            if computer_choice == 'ROCK':
                print("---------ITS A TIE---------\n")
            elif computer_choice == 'PAPER':
                print("---------YOU LOSE---------\n")
            else:
                print("---------YOU WIN---------\n")
                
        elif player_choice == 'PAPER':
            print("You chose PAPER.\n")

            if computer_choice == 'ROCK':
                print("---------YOU WIN---------\n")
            elif computer_choice == 'PAPER':
                print("---------ITS A TIE---------\n")
            else:
                print("---------YOU LOSE---------\n")

        elif player_choice == 'SCISSORS':
            print("You chose SCISSORS.\n")

            if computer_choice == 'ROCK':
                print("---------YOU LOSE---------\n")
            elif computer_choice == 'PAPER':
                print("---------YOU WIN---------\n")
            else:
                print("---------ITS A TIE---------\n")

        else:
            print(f"{player_choice} is not a valid option.")

    elif response == 'no':
        break
    
    else: 
        print(f"Sorry, {response} is invalid.")