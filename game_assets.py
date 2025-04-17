from battle import battle

class enemy:
    def __init__(self, name, hp, nerves, attacks):
        self.name = name
        self.hp = hp
        self.nerves = nerves
        self.attacks = attacks

class ally:
    def __init__(self, name, hp, nerves, attacks):
        self.name = name
        self.hp = hp
        self.nerves = nerves
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

test_enemy_attack = attack('Test Attack 1', -20, -20, ['0'], ['1'], ['2'], ['3'])
test_ally_attack = attack('Test Attack 2', -20, -20, ['0'], ['1'], ['2'], ['3'])

viyh = enemy('The Voice In Your Head', 50, 100, [test_enemy_attack])
player = ally('Unpaid Intern', 
              100, 100, 
              [test_ally_attack])

battle([player], [viyh], ['Test', 'testing', 'tester'])