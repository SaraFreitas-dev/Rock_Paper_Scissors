import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def play_game():
    while True:
        try:
            user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
            if user_choice < 0 or user_choice > 2:
                raise ValueError("Invalid choice. Please choose 0, 1, or 2.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Invalid answer. Please try again.")

    # Generate the computer's choice
    pc_choice = random.randint(0, 2)

    #############USER##########
    if user_choice == 0:
        print(f"You choose:\n{rock}")
    elif user_choice == 1:
        print(f"You choose:\n{paper}")
    else:
        print(f"You choose:\n{scissors}")

    #############PC###########
    if pc_choice == 0:
        print(f"Computer chooses:\n{rock}")
    elif pc_choice == 1:
        print(f"Computer chooses:\n{paper}")
    else:
        print(f"Computer chooses:\n{scissors}")

    #########Result############
    if user_choice == pc_choice:
        print("It's a draw!")
    elif (user_choice == 0 and pc_choice == 2) or (user_choice == 1 and pc_choice == 0) or (user_choice == 2 and pc_choice == 1):
        print("You win!")
    else:
        print("You lose!")

# Main loop to play the game repeatedly
while True:
    play_game()
    
    # Ask the user if they want to play again
    replay = input("Do you want to play again? Type 'yes' or 'no': ").strip().lower()
    if replay != 'yes':
        print("Thanks for playing! Goodbye.")
        break
