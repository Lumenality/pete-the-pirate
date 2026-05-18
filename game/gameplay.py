from game.characters.player import Player
from colors import Colors


def gameplay():
    print("Welcome to the game")
    player_name = input(f"What is your name?\n{Colors.BOLD}")
    print(f"{Colors.ENDC}")
    player_character = Player(player_name)
    print(f"\n{Colors.OKGREEN}Welcome to the ship {player_name}{Colors.ENDC}")
    
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