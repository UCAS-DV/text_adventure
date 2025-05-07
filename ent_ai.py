import game_assets
import random

def test_enemy_decision_tree(enemy, attack_list, status_ability_list, healing_ability_list):
    #print(enemy)
    #print("enemy")
    #print("\n\n")
    #print(attack_list)
    #print("attack_list")
    #print("\n\n")
    #print(status_ability_list)
    #print("status ability list")
    #print("\n\n")
    #print(healing_ability_list)
    #print("healing ability list")
    #print("\n\n")

    enemy_team = game_assets.enemies
    player_team = game_assets.allies

    decision_list = ["attack", "ability", "heal"]
    #print ("created initial ability list")

    low_hp_enemies = []
    #print("created empty low_hp_enemies list")
    near_death_enemies = []
    #print("created empty near_death_enemies list")
    damaged_allies = []
    #print("created empty damaged_allies list")
    critical_allies = []
    #print("created empty critical_allies list")

    # Evaluate own team
    for i in range(len(enemy_team)):
        enemy_unit = enemy_team[i]
        hp_percent = (enemy_unit.hp * 100) / enemy_unit.max_hp
        if hp_percent <= 40:
            low_hp_enemies.append(enemy_unit)
        if hp_percent <= 20:
            near_death_enemies.append(enemy_unit)

    # Evaluate enemy team (including self)
    for i in range(len(player_team)):
        ally = player_team[i]
        hp_percent = (ally.hp * 100) / ally.max_hp
        if hp_percent <= 60:
            damaged_allies.append(ally)
        if hp_percent <= 20:
            critical_allies.append(ally)

    # Also include self in healing logic
    self_hp_percent = (enemy.hp * 100) / enemy.max_hp
    if self_hp_percent <= 60:
        damaged_allies.append(enemy)
    if self_hp_percent <= 20:
        critical_allies.append(enemy)

    if len(near_death_enemies) > 0:
        decision_list.extend(["heal"] * 3)
    if len(damaged_allies) > 0:
        decision_list.extend(["heal"] * 2)
    for i in range(3):
        main_choice = random.choice(decision_list)
        #print(decision_list)
        #print(main_choice)

        if main_choice == "attack":
            if len(attack_list) == 0:
                #print("no_attack_available"
                pass
            else:
                return random.choice(attack_list)

        if main_choice == "ability":
            if len(status_ability_list) == 0:
                #print("no_status_ability_available")
                pass
            else:
                return random.choice(status_ability_list)
        
        if main_choice == "heal":
            if len(healing_ability_list) == 0:
                #print("no_healing_ability_available")
                pass
            else:
                return random.choice(healing_ability_list)
 
# --- Example Attacks and Abilities using game_assets.attack ---

from game_assets import attack

slash = attack("slash", "Slash", "A quick slash with a blade.", 15, 0, True, False,
               "slashes fiercely!", "slashes!", "misses the slash!", "completely whiffs!", None)

fireball = attack("fireball", "Fireball", "Launches a fireball that hits all enemies.", 10, 5, True, True,
                  "engulfs the enemies in flames!", "hits with a fireball!", "fireball fizzles.", "burns their own hand!", None)

single_heal = attack("single_heal", "Single Heal", "Heals one ally significantly.", -30, 4, False, False,
                     "heals deeply!", "restores health!", "healing falters.", "drops the herbs!", None)

group_heal = attack("group_heal", "Group Heal", "Heals all allies a small amount.", -10, 6, False, True,
                    "waves healing light!", "casts group heal!", "misfires the spell.", "heals the enemy!", None)

blind_strike = attack("blind_strike", "Blind Strike", "Deals damage and blinds the enemy.", 10, 3, True, False,
                      "hits eyes directly!", "blinds the foe!", "misses!", "hits own foot!", 1)

shield_up = attack("shield_up", "Shield Up", "Raises a shield to reduce incoming damage.", 0, 2, False, False,
                   "perfect defense!", "raises a shield.", "shield slips!", "drops the shield!", 2)

# Function call
#print(test_enemy_decision_tree(game_assets.enemies[0], [], [], [group_heal]))




