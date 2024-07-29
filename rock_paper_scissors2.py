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

import random


player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

if player_choice == 0:
    print(f"You chose: rock!{rock}")
elif player_choice == 1:
    print(f"You chose: paper!{paper}")
elif player_choice == 2:
    print(f"You chose: scissors!{scissors}")
else:
    print("You typed an invalid number. Please type 0, 1, or 2.")

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(f"Computer chose: rock!{rock}")
elif computer_choice == 1:
    print(f"Computer chose: paper!{paper}")
elif computer_choice == 2:
    print(f"Computer chose: scissors!{scissors}")

if player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
elif player_choice == computer_choice:
    print("Draw!")
else:
    print("You lose!")