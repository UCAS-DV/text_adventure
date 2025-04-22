from dialogue_reader import *
from helper_funcs import inq_select

def show_stats(target):
    print(f'-~-~-~-~-{target.name}-~-~-~-~-')
    print(f'HP: {target.hp}/{target.max_hp}')
    print(f'Nerves: {target.nerves}/{target.max_nerves}')
    print(f'Minimum Nerves: {target.min_nerves}')

def use_item(item, allies, enemies):

    read_description(item.a_desc)

    while True:
        if item.offensive:
            # IF item affects multiple enemies
            if item.multi:
                for enemy in enemies:  
                    enemy.hp += item.hp
                    enemy.nerves += item.nerves

                    input(f'All enemies lost {-item.hp} health.\nAll enemies lost {-item.nerves} nerves.')
                
                break
            else:
                
                # Print out all enemy info and have user select enemy
                enemy_info = []
                for enemy in enemies:
                    enemy_info.append(f'{enemy}')
                enemy_selected = enemies[inq_select('Which item would you like to select? ', *enemy_info) - 1]

                enemies.remove(enemy_selected)

                # Apply Effects
                enemy_selected.hp += item.hp
                enemy_selected.nerves += item.nerves

                enemies.append(enemy_selected)

                break

    return allies, enemies



def battle(allies, enemies, opening, closing, inventory):

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

                # Check Stats
                case 1:
                    match inq_select('Whose stats would you like to look at?', 'Allies', 'Enemies', 'All'):
                        # Allied Stats
                        case 1:
                            for ally in allies:
                                show_stats(ally)
                        # Enemies Stats
                        case 2:
                            for enemy in enemies:
                                print(enemy)
                        # All Stats
                        case 3:
                            for ally in allies:
                                show_stats(ally)
                            for enemy in enemies:
                                show_stats(enemy)

                # Use Item
                case 3: 
                    item_info = []
                    for item in inventory:
                        item_info.append(f'{item}')


                    item_selected = inventory[inq_select('Which item would you like to select? ', *item_info) - 1]
                    
                    allies, enemies = use_item(item_selected, allies, enemies)
                    inventory.remove(item_selected)
                        


    read_dialogue(closing)
    return victory, inventory

