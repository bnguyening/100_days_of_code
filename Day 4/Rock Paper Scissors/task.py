import random
print("Time to play Rock paper Scissors.")
print("Type 1 for Rock, 2 for paper, 3 for scissors.")
player_guess = int(input())

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

if player_guess == 1:
    print(rock)
if player_guess == 2:
    print(paper)
if player_guess == 3:
    print(scissors)

computer_guess = random.randint(1, 3)
print("Computer chose:")
if computer_guess == 1:
    print(rock)
if computer_guess == 2:
    print(paper)
if computer_guess == 3:
    print(scissors)

if computer_guess == player_guess:
    print("It's a tie. Try again")
if computer_guess == 1 and player_guess == 2:
    print("You won!")
if computer_guess == 2 and player_guess == 3:
    print("You Won!")
if computer_guess == 3 and player_guess == 1:
    print("You Won!")
if computer_guess == 1 and player_guess == 3:
    print("You Lose.")
if computer_guess == 2 and player_guess == 1:
    print("You Lose.")
if computer_guess == 3 and player_guess == 2:
    print("You Lose.")
else:
    print("You chose an invalid number please try again ")