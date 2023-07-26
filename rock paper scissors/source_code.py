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

human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if human == 1:
  print(paper)
elif human == 0:
  print(rock)
elif human == 2:
  print(scissors)
else:
  print("invalid choice you lost the  game")
# else:
#   print("invalid")
print("computer choice")
computer = random.randint(0,2)
if computer == 0:
  print(rock)
elif computer== 1:
  print(paper)
elif computer == 2:
  print(scissors)
#if human >=3:
#   print("you choose a invalid choice you lost the game")
if human == 0 and computer == 0 or human == 1 and computer == 1 or human == 2 and computer == 2 :
  print("tie ")
elif human == 1 and computer == 0 or human == 2 and computer == 1 or human == 0 and computer == 2 :
  print("you win")
elif human < computer:
  print("you loose")

