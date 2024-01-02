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

user_choice = int(input("What do you want to choose. 0 for rock, 1 for paper, 2 for scissors"))
if user_choice > 2:
    print("You typed an invalid number. YOu lose!!")
    
    print(art_list[user_choice])
    computer_choice = random.randint(0,2)
    print(art_list[computer_choice])


    if computer_choice == user_choice:
        print("It's a draw")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice > computer_choice:
        print("You win")