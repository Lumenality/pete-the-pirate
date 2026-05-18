# from game.characters.player import Player
from game.gameplay import introduction
from colors import Colors

def main():
    print("\nWhat would you like to do?")
    print("1: Play game")
    print("0: Exit\n")
    choice = input(f"{Colors.BOLD}")
    print(f"{Colors.ENDC}")
    match choice:
        case "1":
            introduction()
            main()
        case "0":
            return 0
        case _:
            print(f"{Colors.FAIL}ERR:{Colors.FAIL}Something probably went wrong, try again!")
            main()

if __name__ == "__main__":
    print(",-------------------------------.")
    print(f"|  {Colors.OKGREEN}Welcome to Pete the Pirate!{Colors.ENDC}  |")
    print("'-------------------------------'")
    main()