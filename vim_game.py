import random

def play_viim_game():
    print("Welcome to the Viim Game!")
    
    # Set up the initial pile size
    pile_size = random.randint(15, 30)
    print(f"The game starts with a pile of {pile_size} stones.")

    # Decide who goes first
    player_turn = random.choice([True, False])
    print("You" + (" go first." if player_turn else "r opponent goes first."))

    while pile_size > 0:
        print(f"\nCurrent pile size: {pile_size}")
        if player_turn:
            # Player's turn
            while True:
                try:
                    player_move = int(input("Your turn! How many stones will you take (1-3)? "))
                    if 1 <= player_move <= 3 and player_move <= pile_size:
                        break
                    else:
                        print("Invalid move. You can take 1, 2, or 3 stones, and not more than are left.")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            # Opponent's turn (simple AI)
            player_move = min(pile_size, random.randint(1, 3))
            print(f"Opponent takes {player_move} stone(s).")

        # Update the pile
        pile_size -= player_move

        if pile_size == 0:
            if player_turn:
                print("\nYou took the last stone. You lose!")
            else:
                print("\nOpponent took the last stone. You win!")
            break

        # Switch turn
        player_turn = not player_turn

if __name__ == "__main__":
    play_viim_game()

