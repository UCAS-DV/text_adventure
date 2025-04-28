import game_assets
import random


josh = game_assets.enemy("Josh",50,50,10,[game_assets.test_enemy_attack],[2])
you = game_assets.ally("you",50,50,10,[game_assets.test_ally_attack],[])


def attack_them(att,name):
    dmg = att.hp
    if random.randint(1,10) == 5:
        print(att.super_success)
        dmg = att.hp*1.75
    if 1 in name.effects:
        dmg *= 1.5
    if 2 in name.effects:
        dmg *= 0.75

    dmg = round(dmg)
    name.hp -= dmg
    print(name.hp)

attack_them(game_assets.test_ally_attack,josh)