import random
player_name = input("Please enter your name: ")
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
computer_move = ""
player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move == scissors
else:
    raise SystemExit(f'Invalid Input. {player_name}, please try again...')

computer_random_number = random.randint(1, 3)

if computer_random_number == 1:
    computer_move = rock

elif computer_random_number ==2:
    computer_move = paper
else:
    computer_move = scissors

print(f"The computer chose {computer_move}.")

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print(f'You win, {player_name} ! Congratulations !')
elif (player_move == rock and computer_move == rock) or \
        (player_move == paper and computer_move == paper) or \
        (player_move == scissors and computer_move == scissors):
    print('We have draw !')

else:
    print(f'You lose, {player_name}. Better luck next time!')

