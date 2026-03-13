import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    choice={'player': player_choice, 'computer': computer_choice}
    return choice

choice=get_choices()
print(f"You chose: {choice['player']}, Computer chose: {choice['computer']}")