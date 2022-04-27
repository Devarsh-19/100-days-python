import random
import os
import time
import logo

print(logo.logo)

user_cards = []
cpu_cards = []

def generate_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
    
for x in range(2):
    cpu_cards.append(generate_card())
    user_cards.append(generate_card())
    
print(f"YOUR CARDS- {user_cards}")
print(f"CPU CARDS- {cpu_cards}")

q1 = int(input("Press 1 to HIT and 2 to HOLD : "))

if q1 == 1:
    cpu_cards.append(generate_card())
    user_cards.append(generate_card())
else:
    cpu_cards.append(generate_card())
    
user_sum = sum(user_cards)
cpu_sum = sum(cpu_cards)

if user_sum >21 :
    print("YOU LOSE.")
elif user_sum <= 21 and user_sum > cpu_sum:
    print("YOU WIN.")

print(f"USER: SUM- {user_sum}  CARDS - {user_cards}")
print(f"CPU: SUM- {cpu_sum}  CARDS - {cpu_cards}")

time.sleep(5)