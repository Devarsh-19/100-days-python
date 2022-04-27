import random
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
    
print(cpu_cards)
print(user_cards)

time.sleep(5)