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

lst = [rock , paper ,scissors]


n=int(input("1- ROCK, 2- PAPER, 3- SCISSORS : \n"))
print("YOU CHOOSE ",lst[n-1])
cpu = random.randint(0,2)
print("COMPUTER DRAWS - ",lst[cpu])
