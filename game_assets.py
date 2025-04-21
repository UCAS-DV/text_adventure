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

class ally:
    def __init__(self, name, max_hp, max_nerves, min_nerves, attacks):
        self.name = name

        self.max_hp = max_hp
        self.hp = max_hp

        self.max_nerves = max_nerves
        self.nerves = max_nerves
        self.min_nerves = min_nerves

        self.attacks = attacks

class attack:
    def __init__(self, name, hp, nerves, super_success, success, fail, super_fail):
        self.name = name
        self.hp = hp
        self.nerves = nerves
        self.super_success = super_success
        self.success = success
        self.fail = fail
        self.super_fail = super_fail

class item:
    def __init__(self, name, item_description, hp, nerves, action_description):
        self.name = name
        self.i_desc = item_description
        self.hp = hp
        self.nerves = nerves
        self.a_desc = action_description

test_enemy_attack = attack('Test Attack 1', -20, -20, ['0'], ['1'], ['2'], ['3'])
test_ally_attack = attack('Test Attack 2', -20, -20, ['0'], ['1'], ['2'], ['3'])

viyh = enemy(name='The Voice In Your Head', 
             max_hp=50, max_nerves=50, min_nerves=10, 
             attacks=[test_enemy_attack])

player = ally(name='Unpaid Intern', 
              max_hp=100, max_nerves=100, min_nerves=10, 
              attacks=[test_ally_attack])

test_item = item(name='Item',
                 item_description='An item made for testing!',
                 hp=-20, nerves=-20,
                 action_description=['This is an item.', 'It is being used.'])

battle([player], [viyh], 'Dialogue\opening_cutscene.txt', 'Dialogue/tutorial1.txt')