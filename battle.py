from dialogue_reader import *
from helper_funcs import inq_select

def show_stats(target):
    print(f'-~-~-~-~-{target.name}-~-~-~-~-')
    print(f'HP: {target.hp}/{target.max_hp}')
    print(f'Nerves: {target.nerves}/{target.max_nerves}')
    print(f'Minimum Nerves: {target.min_nerves}')

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
                enemy.hp = enemy.max_hp
                enemy.nerves = enemy.max_nerves

            # Resets allied stats
            for ally in allies:
                ally.hp = ally.max_hp
                ally.nerves = ally.max_nerves

            battle_ended = True
            break

        if won:
            
            # Resets allied stats
            for ally in allies:
                ally.hp = ally.max_hp
                ally.nerves = ally.max_nerves

            victory = True
            battle_ended = True
            break
        
        # IF player's turn
        if turn % 2 == 0:
            match inq_select('Which action would you like to perform?', 'Check Stats', 'Attack', 'Use Item'):
                case 1:
                    match inq_select('Whose stats would you like to look at?', 'Allies', 'Enemies', 'All'):
                        case 1:
                            for ally in allies:
                                show_stats(ally)
                        case 2:
                            for enemy in enemies:
                                show_stats(enemy)
                        case 3:
                            for ally in allies:
                                show_stats(ally)
                            for enemy in enemies:
                                show_stats(enemy)

    read_dialogue(closing)
    return victory

