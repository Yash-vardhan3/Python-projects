import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid input. Please enter a number between 2-4.")

max_score = 50
player_scores = [0 for _ in range(players)]
winning_players = []

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y/n)? ")
            if should_roll.lower() != "y":
                break
                
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your score is:", current_score)
                player_scores[player_idx] += value

    max_score = max(player_scores)
    for idx, score in enumerate(player_scores):
        if score == max_score:
            winning_players.append(idx + 1)

print("The winners are players:", ", ".join(map(str, winning_players)), "with a score of:", max_score)