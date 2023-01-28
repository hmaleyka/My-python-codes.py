current_level = 0
final_level = 10

game_completed = True

while current_level <= final_level:
    if game_completed:
        print('You have passed level', current_level)
        current_level += 1

print('Level Ends')