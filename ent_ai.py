import game_assets
import random

def test_enemy_decision_tree(enemy, attack_list, status_ability_list, healing_ability_list):
    enemies = game_assets.allies
    allies = game_assets.enemies

    decision_list = []

    low_hp_enemies = []
    near_death_enemies = []
    damaged_allies = []
    critical_allies = []

    # Evaluate enemy team
    for i in range(len(enemies)):
        enemy_unit = enemies[i]
        hp_percent = (enemy_unit.hp * 100) / enemy_unit.max_hp
        if hp_percent <= 40:
            low_hp_enemies.append(enemy_unit)
        if hp_percent <= 20:
            near_death_enemies.append(enemy_unit)

    # Evaluate own team (including self)
    for i in range(len(allies)):
        ally = allies[i]
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
        decision_list.extend(["attack"] * 3)
    if len(damaged_allies) > 0:
        decision_list.extend(["ability"] * 2)
    decision_list.append("attack")

    main_choice = random.choice(decision_list)

    if main_choice == "attack":
        if len(attack_list) == 0:
            return "no_attack_available"
        return random.choice(attack_list)

    if main_choice == "ability":
        ability_type_list = []

        if len(damaged_allies) >= 2:
            ability_type_list.extend(["group_heal"] * 3)
        if len(critical_allies) > 0:
            ability_type_list.extend(["single_heal"] * 4)

        ability_type_list.extend(["status"] * 3)

        ability_type = random.choice(ability_type_list)

        if "heal" in ability_type:
            if len(healing_ability_list) == 0:
                return "no_healing_available"
            return random.choice(healing_ability_list)
        else:
            if len(status_ability_list) == 0:
                return "no_status_ability_available"
            return random.choice(status_ability_list)

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
print(test_enemy_decision_tree(game_assets.enemies[0], [slash, fireball], [blind_strike, shield_up], [single_heal, group_heal]))




