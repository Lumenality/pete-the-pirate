from game.characters.player import Player
from game.characters.enemy import Enemy
from game.combat import combat
from colors import Colors

def introduction():
    '''
    This shows once at the start of a save file to introduce the player to the game,
    and to select their name (And possibly later class, when class choice is implemented)
    '''
    print(f"{Colors.OKGREEN}You wake up on a ship, your head is spinning and you can't quite see straight")
    print(f"Through the fog you see two pirates aproach you, merging into one{Colors.ENDC}")
    player_name = input(f"{Colors.OKGREEN}The unknown pirate asks:{Colors.ENDC} {Colors.OKCYAN}What is your name?{Colors.ENDC} (Default: Pete)\n\nName: {Colors.BOLD}")
    if player_name == "":
        player_name = "Pete"
    print(f"{Colors.ENDC}")
    player_character = Player(player_name)
    print(f"{Colors.OKCYAN}Welcome back to the land of the living {player_character.name}")
    print(f"You hit your head pretty hard there, but we're going to need you to savvy up!{Colors.ENDC}")

    print(f"\n{Colors.OKGREEN}You are unsure what happened, but you know you need to get out of here and find some treasure!")
    print(f"What would you like to do?{Colors.ENDC}")
    print("1: Start exploring!")
    print("0: Exit to main menu\n")
    choice = input()
    match choice:
        case "1":
            # RIGHT NOW THIS JUST PLACES US RIGHT INTO THE START OF THE LOOP
            gameplay(player_character)
        case "0":
            return 0
        case _:
            print(f"{Colors.FAIL}ERR:{Colors.FAIL}Something probably went wrong, try again!")
            gameplay(player_character)

def gameplay(player_character):
    '''
    Core gameplay loop, where you explore the rooms of
    '''
    print(f"{Colors.OKGREEN}Before you, you see two rooms")
    print(f"What do you do?{Colors.ENDC}")
    print("1: Enter room 1")
    print("2: Enter room 2")
    print("i: Check your inventory")
    print("0: Start over\n")
    choice = input(f"{Colors.BOLD}").lower()
    print(f"{Colors.ENDC}")
    match choice:
        case "1":
            print(f"{Colors.OKGREEN}You enter room 1:{Colors.ENDC}")
            print(f"Inside you find a {Colors.FAIL}heinous beast{Colors.ENDC}!\n")
            enemy = Enemy("Angy Crab")
            is_victory = combat(player_character,enemy)
            if not is_victory:
                return
            gameplay(player_character)
        case "2":
            print(f"{Colors.OKGREEN}You enter room 2:")
            print(f"{Colors.WARNING}+10 Gold{Colors.ENDC} Treasure or whatever\n")
            player_character.inventory["gold"] += 10
            gameplay(player_character)
        case "i":
            print(f"Shirt: {player_character.inventory["equipment"]["shirt"]}")
            print(f"Gold: {Colors.WARNING}{player_character.inventory["gold"]}{Colors.ENDC}")
            gameplay(player_character)
        case "0":
            introduction()
        case _:
            print(f"{Colors.FAIL}ERR:{Colors.FAIL}Something probably went wrong, try again!")
            gameplay(player_character)
