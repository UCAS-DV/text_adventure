from dialogue_reader import *

def battle(allies, enemies, opening, closing):

    read_dialogue(opening)

    turn = 0
    battle_ended = False
    victory = False

    while not battle_ended:
        
        # Checks if every ally has been knocked down
        lost = True
        for ally in allies:
            if ally.hp >= 0:
                lost = False

        won = True
        for enemy in enemies:
            if enemy.hp >= 0:
                won = False

        if lost:

            # Resets enemy stats
            for enemy in enemies:
                enemy.hp = enemy.max_health
                enemy.nerves = enemy.max_nerves

            # Resets allied stats
            for ally in allies:
                ally.hp = ally.max_health
                ally.nerves = ally.max_nerves

            battle_ended = True
            break

        if won:
            
            # Resets allied stats
            for ally in allies:
                ally.hp = ally.max_health
                ally.nerves = ally.max_nerves

            victory = True
            battle_ended = True
            break
        
        # IF player's turn
        if turn % 2 == 0:
            pass

