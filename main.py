from game.characters.player import Player
from game.gameplay import gameplay
from colors import Colors

def main():
    # Dummy-Define the player character
    player_character = Player("Pete")

    print("\nWhat would you like to do?")
    print("1: Play game")
    print("2: Exit\n")
    choice = input()
    match choice:
        case "1":
            print(f"\n{player_character}")
            gameplay()
        case "2":
            return 0
        case _:
            print(f"{Colors.FAIL}ERR:{Colors.FAIL}Something probably went wrong, try again!")
            main()

if __name__ == "__main__":
    print(",-------------------------------.")
    print(f"|  {Colors.OKGREEN}Welcome to Pete the Pirate!{Colors.ENDC}  |")
    print("'-------------------------------'")
    main()