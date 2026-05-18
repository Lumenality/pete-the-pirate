from game.characters.player import Player
from colors import Colors

def gameplay():
    print(f"Welcome to the game")
    player_name = input("What is your name?\n")
    player_character = Player(player_name)
    print(f"\nWelcome to the ship {player_name}")
    
    print("\nWhat would you like to do?")
    print("1: Restart")
    print("0: Exit to main menu\n")
    choice = input()
    match choice:
        case "1":
            print(f"\n{player_character}")
            gameplay()
        case "0":
            return 0
        case _:
            print(f"{Colors.FAIL}ERR:{Colors.FAIL}Something probably went wrong, try again!")
            gameplay()