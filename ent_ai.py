import game_assets
import random


def action(self_name): #self_name is so you can enter the enemies name into the paramater for their turn 
    actions = []
    hpercent = (game_assets.self_name.hp*100)/game_assets.self_name.max_hp
    if hpercent <= random.randint(50,75):
        actions.append("action")
    if hpercent <= random.randint(25,40):
        actions.append("action")
        #makes enemy more likley to preform actions bassed what hp they have, and the hp of your allies
    for i in range(len(game_assets.allies)):
        ally_hpercent = (game_assets.allies(i).hp*100)/game_assets.allies(i).max_hp
        if ally_hpercent <= random.randint(25,30):
            actions.append("attack")
        ally_hpercent = 0
    
#NOT FINISHED YET DONT USE IN CODE 


def who_to_attack(*chars):
    print(chars)
    chars.sort()
    print(chars)