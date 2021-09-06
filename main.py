import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0, 2)
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
if user_choice == computer_choice:
    if user_choice == 0:
        print("You chose\n" + rock + "Computer chose\n" + rock)
    elif user_choice == 1:
        print("You chose\n" + paper + "Computer chose\n" + paper)
    else:
        print("You chose\n" + scissors + "Computer chose\n" + scissors)
    print("It's a tie! Would you like to play again?")
elif user_choice == 0 and computer_choice == 1:
    print("You chose\n" + rock + "Computer chose\n" + paper)
    print("You lose :( , would you like to play again?")
elif user_choice == 1 and computer_choice == 2:
    print("You chose\n" + paper + "Computer chose\n" + scissors)
    print("You lose :( , would you like to play again?")
elif user_choice == 2 and computer_choice == 0:
    print("You chose\n" + scissors + "Computer chose\n" + rock)
    print("You lose :( , would you like to play again?")
elif user_choice == 0 and computer_choice == 2:
    print("You chose\n" + rock + "Computer chose\n" + scissors)
    print("You win :) , would you like to play again?")
elif user_choice == 1 and computer_choice == 0:
    print("You chose\n" + paper + "Computer chose\n" + rock)
    print("You win :) , would you like to play again?")
elif user_choice == 2 and computer_choice == 1:
    print("You chose\n" + scissors + "Computer chose\n" + paper)
    print("You win :) , would you like to play again?")
elif user_choice < 0 or user_choice > 2:
    print("You entered an invalid number. You lose :( , would you like to play again?")