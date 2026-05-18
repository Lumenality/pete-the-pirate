def combat(player_character, enemy):
    '''
    The games combat loop, puts the player against one enemy entity (for now) and lets them duke it out
    '''
    is_victory = False

    while player_character.health > 0 and enemy.health > 0:
        
        player_character.attack(enemy)
        print(f"{player_character.name} hits {enemy.name} for {player_character.damage} damage. (Remaining health: {enemy.health})")
        enemy.attack(player_character)
        print(f"{enemy.name} hits {player_character.name} for {enemy.damage} damage. (Remaining health: {player_character.health})")

    if player_character.health > enemy.health:
        print(f"You win! The {enemy.name} is defeated!")
        is_victory = True
    else:
        print("You died!")
    return is_victory