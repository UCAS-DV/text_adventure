from dialogue_reader import *
from helper_funcs import inq_select
import random

# Rolls random multipler based off of nerves
def roll_nerves(nerves, attack):

    roll = random.randint(1,100)

    if roll < nerves * 0.1:
        read_description(attack.super_success + [f'{attack.name} was super successful!'])
        return 1.5
    elif roll < nerves:
       read_description(attack.success + [f'{attack.name} was successful!'])
       return 1
        
    if roll > nerves * 1.5:
        read_description(attack.super_fail + [f'{attack.name} was a complete failure!'])
        return 0
    elif roll > nerves:
        read_description(attack.fail + [f'{attack.name} was a ineffective!'])
        return 0.5

# Attacks target   
def attack_them(att, target, nerves):
    dmg = att.hp
    discomfort = att.nerves

    nerve_multiplier = roll_nerves(nerves, att)

    # Multiply damage and nerve damage by nerve multiplier
    dmg *= nerve_multiplier
    discomfort *= nerve_multiplier

    # Apply effects if applicable
    if 1 in target.effects:
        dmg *= 1.5
    if 2 in target.effects:
        dmg *= 0.75

    dmg = round(dmg)
    target.hp -= dmg

    discomfort = round(discomfort)
    target.nerves -= discomfort

    # Sets hp to 0 if it's below 0
    if target.hp < 0:
        target.hp = 0

    # Sets nerves to minimum if it's below minimum
    if target.nerves < target.min_nerves:
        target.nerves = target.min_nerves

    # Print the amount of damage done
    if dmg < 0:
        print(f'{target.name} gained {dmg} health!')
    elif dmg > 0:
        print(f'{target.name} lost {dmg} health!')

    # Print the amount of discomfort done
    if discomfort < 0:
        print(f'{target.name} gained {discomfort} nerves!')
    elif discomfort > 0:
        print(f'{target.name} lost {discomfort} nerves!')

# Formats items so it can be used in UI
def format(unformatted_list):

    list_info = []
    for list_item in unformatted_list:
        list_info.append(f'{list_item}')

    return list_info

# Applies item effects
def use_item(item, allies, enemies):

    while True:
        if item.offensive:
            # IF item affects multiple enemies
            if item.multi:

                read_description(item.a_desc)

                # Applies effects to all enemies
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

                read_description(item.a_desc)

                # Apply Effects
                enemy_selected.hp += item.hp
                enemy_selected.nerves += item.nerves

                enemies.append(enemy_selected)

                input(f'{enemy_selected.name} lost {-item.hp} health.\n{enemy_selected.name} lost {-item.nerves} nerves.')
                break
        else:
            # IF item affects multiple allies
            if item.multi:

                read_description(item.a_desc)

                # Applies effects to all allies
                for ally in allies:  
                    ally.hp += item.hp
                    ally.nerves += item.nerves

                input(f'All allies gained {item.hp} health.\nAll enemies gained {item.nerves} nerves.')

                break
            else:
                
                # Print out all enemy info and have user select enemy
                ally_info = []
                for ally in allies:
                    ally_info.append(f'{ally}')
                ally_selected = allies[inq_select('Which item would you like to select? ', *ally_info) - 1]

                allies.remove(ally_selected)

                read_description(item.a_desc)

                # Apply Effects
                ally_selected.hp += item.hp
                ally_selected.nerves += item.nerves

                allies.append(ally_selected)   

                input(f'{ally_selected.name} gained {item.hp} health.\n{ally_selected.name} gained {item.nerves} nerves.')

                break
    return allies, enemies

# Main battle function
def battle(allies, enemies, opening, closing, inventory):

    read_dialogue(opening)

    turn = 0
    battle_ended = False
    victory = False

    while not battle_ended:
        
        # Checks if every ally has been knocked down
        lost = True
        for ally in allies:
            if ally.hp > 0:
                lost = False

        # Checks if every enemy has been knocked down
        won = True
        for enemy in enemies:
            if enemy.hp > 0:
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
                    match inq_select('Whose stats would you like to look at?', 'Team', 'Enemies', 'All'):
                        # Team Stats
                        case 1:
                            for ally in allies:
                                print(ally)
                        # Enemies Stats
                        case 2:
                            for enemy in enemies:
                                print(enemy)
                        # All Stats
                        case 3:
                            for ally in allies:
                                print(ally)
                            for enemy in enemies:
                                print(enemy)

                # Attacks
                case 2:

                    ally_info = format(allies)
                    ally_selected = allies[inq_select('Which ally would you like to select? ', *ally_info) - 1]

                    if ally_selected.hp > 0:
                        attack_info = format(ally_selected.attacks)
                        attack_selected = ally_selected.attacks[inq_select('Which attack would you like to select? ', *attack_info) - 1]

                        if not attack_selected.multi:

                            if attack_selected.offensive:
                                target_info = format(enemies)
                                target = enemies[inq_select('Which enemy would you like to attack? ', *target_info) - 1]
                            else:
                                target = allies[inq_select('Which ally would you like to select? ', *ally_info) - 1]

                            if target.hp > 0:
                                attack_them(attack_selected, target, ally_selected.nerves)
                            else:
                                input('Oops! Seems like your target is already downed')

                        else:

                            if attack_selected.offensive:
                                for enemy in enemies:
                                    attack_them(enemy)
                            else:
                                for ally in allies:
                                    attack_them(ally)

                    else: input('Oops! Seems like you selected a downed ally!')

                
                # Use Item
                case 3:

                    item_info = format(inventory)

                    item_selected = inventory[inq_select('Which item would you like to select? ', *item_info) - 1]
                    
                    allies, enemies = use_item(item_selected, allies, enemies)
                    inventory.remove(item_selected)

                    turn += 1

        # Enemy Turn (Amber)
        else:
            pass
    
    if victory:
        read_dialogue(closing)
        
    return victory, inventory