from battle import battle

class enemy:
    def __init__(self, name, max_hp, max_nerves, min_nerves, attacks):
        self.name = name

        self.max_hp = max_hp
        self.hp = max_hp

        self.max_nerves = max_nerves
        self.nerves = max_nerves
        self.min_nerves = min_nerves

        self.attacks = attacks

    def __str__(self):
        return f'-~-~-~-~-{self.name}-~-~-~-~-\nHP: {self.hp}/{self.max_hp}\nNerves: {self.nerves}/{self.max_nerves}\nMinimum Nerves: {self.min_nerves}'


class ally:
    def __init__(self, name, max_hp, max_nerves, min_nerves, attacks):
        self.name = name

        self.max_hp = max_hp
        self.hp = max_hp

        self.max_nerves = max_nerves
        self.nerves = max_nerves
        self.min_nerves = min_nerves

        self.attacks = attacks

    def __str__(self):
        return f'-~-~-~-~-{self.name}-~-~-~-~-\nHP: {self.hp}/{self.max_hp}\nNerves: {self.nerves}/{self.max_nerves}\nMinimum Nerves: {self.min_nerves}'

class attack:
    def __init__(self, name, hp, nerves, offensive, multi, super_success, success, fail, super_fail):
        self.name = name

        self.hp = hp
        self.nerves = nerves

        self.offensive = offensive
        self.multi = multi

        self.super_success = super_success
        self.success = success
        self.fail = fail
        self.super_fail = super_fail

class item:
    def __init__(self, name, item_description, hp, nerves, offensive, multi, action_description):
        self.name = name
        self.i_desc = item_description
        self.hp = hp
        self.nerves = nerves
        self.a_desc = action_description
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
test_enemy_attack = attack('Test Attack 1', -20, -20, True, False, ['0'], ['1'], ['2'], ['3'])
test_ally_attack = attack('Test Attack 2', -20, -20, True, False, ['0'], ['1'], ['2'], ['3'])

sin_off_item = item(name='Item 1',item_description='An item made for testing!',hp=-20, nerves=-20,
                 action_description=['This is an item.', 'It is being used.'],
                 offensive=True, multi=False)
mult_off_item = item(name='Item 2',item_description='An item made for testing!',hp=-20, nerves=-20,
                 action_description=['This is an item.', 'It is being used.'],
                 offensive=True, multi=True)
sin_self_item = item(name='Item 3',item_description='An item made for testing!',hp=20, nerves=20,
                 action_description=['This is an item.', 'It is being used.'],
                 offensive=False, multi=False)
mult_self_item = item(name='Item 4',item_description='An item made for testing!',hp=20, nerves=20,
                 action_description=['This is an item.', 'It is being used.'],
                 offensive=False, multi=True)

test_enemy = enemy(name='Test Enemy',
                   max_hp=50, max_nerves=100, min_nerves=10,
                   attacks=[test_enemy_attack])

test_ally = ally(name='Test Ally', 
              max_hp=100, max_nerves=100, min_nerves=10, 
              attacks=[test_ally_attack])
# Testing Assets End

viyh = enemy(name='The Voice In Your Head', 
             max_hp=50, max_nerves=100, min_nerves=10, 
             attacks=[test_enemy_attack])

player = ally(name='Unpaid Intern', 
              max_hp=100, max_nerves=100, min_nerves=10, 
              attacks=[test_ally_attack])

test_inventory = [sin_off_item, mult_off_item, sin_self_item, mult_self_item]

battle([player, test_ally], [viyh, test_enemy], 'Dialogue\opening_cutscene.txt', 'Dialogue/tutorial1.txt', test_inventory)