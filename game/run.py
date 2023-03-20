from states import game_state
from process import welcome, process

moves = open(r'game\moves.txt', 'r', encoding='utf-8').read().split('\n')[1:-2]

# Introduce game
welcome()

# Assign turn variable for first turn
turn = 1

# Iterate through moves,
for move in moves:
    process(move, turn)
    turn += 1

# After final turn, assign final game state
final_state = game_state()

# Announce game over and print final game state
print('\nGAME OVER!\n')
print(final_state)

# Write final game state to JSON file
with open('game/final_state.json', 'w') as f:
    f.write(final_state)