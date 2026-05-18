from game.characters.player import Player
from colors import Colors

def introduction():
    '''
    This shows once at the start of a save file to introduce the player to the game,
    and to select their name (And possibly later class, when class choice is implemented)
    '''
    print(f"{Colors.OKGREEN}Welcome to the game{Colors.ENDC}")
    player_name = input(f"What is your name?\n\nName: {Colors.BOLD}")
    print(f"{Colors.ENDC}")
    player_character = Player(player_name)
    print(f"{Colors.OKCYAN}Welcome to the ship {player_character.name}{Colors.ENDC}")
    
    print(f"\n{Colors.OKGREEN}What would you like to do?{Colors.ENDC}")
    print("1: Start exploring!")
    print("0: Exit to main menu\n")
    choice = input()
    match choice:
        case "1":
            # RIGHT NOW THIS JUST PLACES US RIGHT INTO THE START OF THE LOOP
            gameplay()
        case "0":
            return 0
        case _:
            print(f"{Colors.FAIL}ERR:{Colors.FAIL}Something probably went wrong, try again!")
            gameplay()

def gameplay():
    '''
    Core gameplay loop, where you explore the rooms of
    '''
    print(f"{Colors.OKGREEN}Before you, you see two rooms")
    print(f"What do you do?{Colors.ENDC}")
    print("1: Enter room 1")
    print("2: Enter room 2")
    print("0: Start over\n")
    choice = input(f"{Colors.BOLD}")
    print(f"{Colors.ENDC}")
    match choice:
        case "1":
            print(f"{Colors.OKGREEN}You enter room 1:{Colors.ENDC}")
            print(f"Inside you find a {Colors.FAIL}heinous beast{Colors.ENDC}!\n")
            gameplay()
        case "2":
            print(f"{Colors.OKGREEN}You enter room 2:")
            print(f"{Colors.WARNING}Treasures{Colors.ENDC} or whatever\n")
            gameplay()
        case "0":
            introduction()
        case _:
            print(f"{Colors.FAIL}ERR:{Colors.FAIL}Something probably went wrong, try again!")
            gameplay()
