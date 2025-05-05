from battle import battle

class enemy:
    def __init__(self, name, max_hp, max_nerves, min_nerves, attacks, abilities, healing_abilities, effects):
        self.name = name

        self.max_hp = max_hp
        self.hp = max_hp

        self.max_nerves = max_nerves
        self.nerves = max_nerves
        self.min_nerves = min_nerves

        self.attacks = attacks
        self.abilities = abilities
        self.heals = healing_abilities

        self.effects = effects

    def __str__(self):
        return f'-~-~-~-~-{self.name}-~-~-~-~-\nHP: {self.hp}/{self.max_hp}\nNerves: {self.nerves}/{self.max_nerves}\nMinimum Nerves: {self.min_nerves}'

class ally:
    def __init__(self, name, max_hp, max_nerves, min_nerves, attacks, effects):
        self.name = name

        self.max_hp = max_hp
        self.hp = max_hp

        self.max_nerves = max_nerves
        self.nerves = max_nerves
        self.min_nerves = min_nerves

        self.attacks = attacks
        self.effect = effects

    def __str__(self):
        return f'-~-~-~-~-{self.name}-~-~-~-~-\nHP: {self.hp}/{self.max_hp}\nNerves: {self.nerves}/{self.max_nerves}\nMinimum Nerves: {self.min_nerves}'

class attack:
    def __init__(self, class_name, display_name, description, hp, nerves, offensive, multi, super_success, success, fail, super_fail, ability):
        #ADD ABILITY AFTER MULTI
        self.class_name = class_name
        self.name = display_name
        self.desc = description

        self.hp = hp
        self.nerves = nerves

        self.offensive = offensive
        self.multi = multi


        self.super_success = super_success
        self.success = success
        self.fail = fail
        self.super_fail = super_fail
        self.ability = ability

    def __str__(self):
        # Affects single enemy
        if self.offensive and not self.multi:
            return f'{self.name}:\n    {self.desc}\n    Damage: {-self.hp}\n    Nerves: {self.nerves}\n    Target: Enemy'
        # Affects multiple enemies
        elif self.offensive and self.multi:
            return f'{self.name}:\n    {self.desc}\n    Damage: {-self.hp}\n    Nerves: {self.nerves}\n    Target: All Enemies'
        # Affects single ally
        elif not self.offensive and not self.multi:
            return f'{self.name}:\n    {self.desc}\n    HP Gained: {self.hp}\n    Nerves: {self.nerves}\n    Target: Ally'
        # Affects multiple allies
        elif not self.offensive and self.multi:
            return f'{self.name}:\n    {self.desc}\n    HP Gained: {self.hp}\n    Nerves: {self.nerves}\n    Target: All Allies'

class item:
    def __init__(self, name, item_description, hp, nerves, offensive, multi, ability, action_description):
        self.name = name
        self.i_desc = item_description
        self.a_desc = action_description

        self.hp = hp
        self.nerves = nerves
        self.ability = ability
        
        self.offensive = offensive
        self.multi = multi

    def __str__(self):
        # Affects single enemy
        if self.offensive and not self.multi:
            return f'{self.name}:\n    {self.i_desc}\n    Damage: {-self.hp}\n    Nerves: {self.nerves}\n    Target: Enemy'
        # Affects multiple enemies
        elif self.offensive and self.multi:
            return f'{self.name}:\n    {self.i_desc}\n    Damage: {-self.hp}\n    Nerves: {self.nerves}\n    Target: All Enemies'
        # Affects single ally
        elif not self.offensive and not self.multi:
            return f'{self.name}:\n    {self.i_desc}\n    HP Gained: {self.hp}\n    Nerves: {self.nerves}\n    Target: Ally'
        # Affects multiple allies
        elif not self.offensive and self.multi:
            return f'{self.name}:\n    {self.i_desc}\n    HP Gained: {self.hp}\n    Nerves: {self.nerves}\n    Target: All Allies'

# Testing Assets Start
test_enemy_attack = attack('sin_off', 'Test Attack 1', 'An attack for testing', 20, 20, True, False, ['0'], ['1'], ['2'], ['3'],[])
test_ally_attack = attack('sin_off', 'Test Attack 2', 'An attack for testing', 20, 20, True, False, ['0'], ['1'], ['2'], ['3'],[])
falcon_punch = attack('heal', 'FALCON PUNCH', 'An attack for testing', 2000, 2000, True, False, ['0'], ['1'], ['2'], ['3'],[])
resign = attack('heal', 'resign', 'An attack for testing', 2000, 2000, False, False, ['0'], ['1'], ['2'], ['3'],[])

sin_off_item = item(name='Item 1',item_description='An item made for testing!',hp=-20, nerves=-20,
                 action_description=['This is an item.', 'It is being used.'],
                 offensive=True, multi=False, ability=[])
mult_off_item = item(name='Item 2',item_description='An item made for testing!',hp=-20, nerves=-20,
                 action_description=['This is an item.', 'It is being used.'],
                 offensive=True, multi=True, ability=[])
sin_self_item = item(name='Item 3',item_description='An item made for testing!',hp=20, nerves=20,
                 action_description=['This is an item.', 'It is being used.'],
                 offensive=False, multi=False, ability=[])
mult_self_item = item(name='Item 4',item_description='An item made for testing!',hp=20, nerves=20,
                 action_description=['This is an item.', 'It is being used.'],
                 offensive=False, multi=True, ability=[])

test_inventory = [sin_off_item, mult_off_item, sin_self_item, mult_self_item]
test_attacks = [test_ally_attack, falcon_punch, resign]

test_enemy = enemy(name='Test Enemy',
                   max_hp=50, max_nerves=100, min_nerves=10,
                   attacks=[test_enemy_attack],abilities=[],healing_abilities=[],effects=[])

test_ally = ally(name='Test Ally', 
              max_hp=100, max_nerves=100, min_nerves=10, 
              attacks=[test_ally_attack],effects=[])
# Testing Assets End

viyh = enemy(name='The Voice In Your Head', 
             max_hp=50, max_nerves=100, min_nerves=10, 
             attacks=[test_enemy_attack],abilities=[],healing_abilities=[],effects=[])

player = ally(name='Unpaid Intern', 
              max_hp=100, max_nerves=100, min_nerves=30, 
              attacks=test_attacks,effects=[])

allies = [player]
enemies = [viyh]
inventory = []

def level_up():
    for ally in allies:
        ally.max_hp += 15
        ally.hp = ally.max_hp

        ally.max_nerves += 15 
        ally.nerves = ally.max_nerves
        ally.min_nerves += 5 

#victory, inventory = battle(allies, [viyh, test_enemy], 'Dialogue\opening_cutscene.txt', 'Dialogue/tutorial1.txt', test_inventory)

