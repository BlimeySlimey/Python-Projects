import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

action = [rock, paper, scissors]

player_choice = int(input("Choose your item. 0 - rock, 1 - paper, 2 - scissors "))
if player_choice >= 0 and player_choice <= 2:
    print(action[player_choice])
computer_choice = random.randint(0,2)
print(f"Computer chose:" )
print(action[computer_choice])


if player_choice >= 3 or player_choice < 0: 
    print("You didn't even choose a valid number.")
elif player_choice == 0 and computer_choice == 2:
    print("Good job")
elif computer_choice == 0  and player_choice == 2:
    print("You lose")
elif computer_choice > player_choice:
    print("FUCK YOU")
elif player_choice > computer_choice:
    print("AYY")
elif computer_choice == player_choice:
    print("Draw!")
    



