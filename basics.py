import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    choice={'player': player_choice, 'computer': computer_choice}
    return choice

choices = get_choices()



def check_win(player,computer):
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "paper":
            return "You lose!"
        else:
            return "You win!"
    elif player == "paper":
        if computer == "scissors":
            return "You lose!"
        else:
            return "You win!"
    elif player == "scissors":
        if computer == "rock":
            return "You lose!"
        else:
            return "You win!"
result = check_win(choices['player'], choices['computer'])
  
print(f"You chose: {choices['player']}, Computer chose: {choices['computer']}")
print(result)
