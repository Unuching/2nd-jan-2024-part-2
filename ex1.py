import random
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

art_list = [Rock, Paper, Scissors]

user_choice = int(input("What do you want to choose. 0 for rock, 1 for paper, 2 for scissors\n"))
if user_choice >= 3 or user_choice < 0:
    print("You Typed an invalid number. You lose.")
else:
    print(art_list[user_choice])
    computer_choice = random.randint(0,2)
    print(art_list[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!!!!")
    elif computer_choice == 0 and user_choice == 2:
        print("You loose")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!!")


