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
        stats = f'-~-~-~-~-{self.name}-~-~-~-~-\nHP: {self.hp}/{self.max_hp}\nNerves: {self.nerves}/{self.max_nerves}\nMinimum Nerves: {self.min_nerves}'

        for effect in self.effects:
            stats += f'\n{effect.capitalize()}'

        return stats

class ally:
    def __init__(self, name, max_hp, max_nerves, min_nerves, attacks, effects):
        self.name = name

        self.max_hp = max_hp
        self.hp = max_hp

        self.max_nerves = max_nerves
        self.nerves = max_nerves
        self.min_nerves = min_nerves

        self.attacks = attacks
        self.effects = effects

    def __str__(self):
        stats = f'-~-~-~-~-{self.name}-~-~-~-~-\nHP: {self.hp}/{self.max_hp}\nNerves: {self.nerves}/{self.max_nerves}\nMinimum Nerves: {self.min_nerves}'

        for effect in self.effects:
            stats += f'\n{effect.capitalize()}'

        return stats

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
            return f'{self.name}:\n    {self.desc}\n    Damage: {self.hp}\n    Nerves: {self.nerves}\n    Target: Enemy'
        # Affects multiple enemies
        elif self.offensive and self.multi:
            return f'{self.name}:\n    {self.desc}\n    Damage: {self.hp}\n    Nerves: {self.nerves}\n    Target: All Enemies'
        # Affects single ally
        elif not self.offensive and not self.multi:
            return f'{self.name}:\n    {self.desc}\n    HP Gained: {-self.hp}\n    Nerves: {-self.nerves}\n    Target: Ally'
        # Affects multiple allies
        elif not self.offensive and self.multi:
            return f'{self.name}:\n    {self.desc}\n    HP Gained: {-self.hp}\n    Nerves: {-self.nerves}\n    Target: All Allies'

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

class encounter:
    def __init__(self, enemies, opening, closing):
        self.enemies = enemies
        self.opening = opening
        self.closing = closing
        

all_enemies = enemy('All enemies', 0, 0, 0, [], [], [], [])
all_allies = enemy('All enemies', 0, 0, 0, [], [], [], [])

# ------------------------------------------------- Testing Assets Start ------------------------------------------------
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
# ------------------------------------------------- Testing Assets End -------------------------------------------------

# ------------------------------------------------- Player Moves -------------------------------------------------
kickflip = attack('sin_off', 'Kickflip', 'Wow everyone with a radical kickflip!', 15, 0, True, False, 
                  ['You run up and do the most rad', 'tubular', 'fresh', 'kickflip on {tname} the world has ever seen.'], 
                  ['You run up and RADICALLY kickflip {tname}.'], 
                  ['You run up and kickflip {tname} but it was only kinda cool.', 'Honestly, it was a 6/10 at best.'],
                  ['You run up and try to kickflip {tname} but you trip and fall onto a nearby skateboard.', 'You end up kickfliping the skateboard,', 'followed by 7 1080 flips', 
                   'and then a 1080 backflip off of the skateboard and onto another skateboard.', 'You end up winning the local "cool guy" competition but you dealt no damage.'],[])
declaration = attack('sin_off', 'Uncouth Declaration', "Forget physical damage! Emotional damage is where it's at!", 0, 15, True, False, 
                     ["Oh...", "wow...", "I get how intense this situation is but you didn't have to go that far.", "To be frank I don't even know if you can legally say that."],
                     ['You yell some very inflamatory statements.', 'The shock of your statements makes {tname} uneasy'], 
                     ['You yell some somewhat mean statements.', 'Honestly, {tname} is shocked at how you could come up with such mild statements'], 
                     ["Okay, so, pro tip...", 'Calling {tname} "Stinky" is not very effective past the first grade'],[])
pep_talk = attack('single_heal', 'Pep Talk', "Fear can't beat out the power of a good pep talk!", 0, -15, False, False, 
                     ['You give such an incredible, rousing self pep talk that even your enemies feel a little inspired.'],
                     ['You give an inspirational pep talk that relieves the stress of battle.'], 
                     ['You try to give yourself a pep talk but you suck at public speaking so it proves ineffective.'], 
                     ['...', "That was...", 'something.', "Don't beat yourself up about it,", 'just ensure that you will never have to do any sort of public speaking...', 'ever...'
        "and you'll be fine!"],[])
apple = attack('single_heal', 'Apple', 'As they say, an apple a day keep the doctor away! Although it might be better to have a doctor in this situation...', -15, 0, False, False,
                 ['The apple tastes funny.', 'In the bitemark you can see the signature of John Apple,', 'the inventor of apples.', "It's rumored that signed apples are only healthy if they deem the eater worthy.", 'Fortunately, the eater was worthy!'],
                 ["{tname} eats the apple and it's as healthy as ever!"],
                 ['It seems that you have Gala apple.', "I guess it's healthy but did you seriously have to have the worst type of apple.", '{tname} eats the apple unhappily.', "Fortunately it's still healthy"],
                 ['The apple tastes funny.', 'In the bitemark you can see the signature of John Apple,', 'the inventor of apples', '"You are NOT worthy!"', 'says the apple as it dissappears.', 'It seems like {tname} was not worthy of a signed apple.'],[])

# ------------------------------------------------- Player Moves End -------------------------------------------------

# ------------------------------------------------- VIYH Moves -------------------------------------------------
pessimism = attack('pessimism', 'Terrible Pessimism', '', 0, 10, True, False,
                 ["To be frank, given how absolutely dysfunctional the country was,", "I don't even think it's worth it."],
                 ["I'm going to be honest, I don't think we, an unpaid intern and a voice in that intern's head can save America like Madam Vice President wants us to."],
                 ['I believe that you will make a mistake at some point in time!', 'Take that!'],
                 ["I have so many negative things to say but what's even the point of sharing them?", 'Does it even matter?'],[])
pep_talk = attack('single_heal', 'Pep Talk', "Fear can't beat out the power of a good pep talk!", -10, -10, False, False, 
                      ['I give myself such an incredible, rousing self pep talk that even you feel a little inspired.', 'Wow, I should really pursue public speaking!', "You know, I think I might do so!", 'Yeah...', 'wait,', 'the only person who can hear me is you.', '...', 'Ow.'],
                     ['I give myself a pep talk and feel inspired by my own words.'], 
                     ["You know...", 'I am so happy that the only person who can hear me is you.'], 
                     ['Um...', "I thought I would be better at speaking given that it's the only thing I can do.", 'Just...', 'please forget everything I just said.'],[])
yell = attack('yell', 'Unbearable Yell', '', 10, 5, True, False,
              ['NO, YOU DID NOT WIN THAT ONLINE ARGUMENT LAST NIGHT!', 'YOU WERE JUST FLAT OUT WRONG!'],
              ["THE ORIGINAL MOVIE WASN'T THAT GOOD!", "YOU ARE JUST LOOKING AT IT WITH ROSE-TINTED GLASSES!"],
              ['aaaaaaa?'],
              ['Um...', 'uh...', "I don't have anywhere near enough energy to yell."], [])
# ------------------------------------------------- VIYH Moves End -------------------------------------------------

# ------------------------------------------------- Skellybones Moves -------------------------------------------------
bone_blow_enemy = attack('bone_blow', 'Funny Bone Blow', '', 20, 10, True, False,
                   ["With what you think is a deadpan expression", "(you can't really tell because he's just a faceless skeleton)", 
                    "He lightly taps your funny bone.", "You look at him confused but suddenly... what feels like a jolt of lightening traverses through your arm and-",
                    '...', '...', 'You good?', 'It seems like your brain was too focused on writhing in very unfunny pain to remember to conjure my existence.', "Uh, don't do that again.",
                    "It's kind of a buzzkill."],
                    ['He hits your funny bone in a very unfunny way'],
                    ['He tries to hit your funny bone in a very unfunny way but he only lightly taps it'],
                    ['He tries to hit your funny bone but he trips and hits his own funny bone.', 'He lays on the ground immobilized as you look down at him with pity.',
                    '"THIS IS NOT FUNNY RAAAAAAH"', 'Eventually he gets his footing and the battle continues.'], [])

# ------------------------------------------------- Santa Claus Fight -------------------------------------------------

blast = attack('blast', 'Christmas MegaBlast', '', 15, 0, True, True, 
               ['"Hohoho!"', '"I did not want to go this far but I will if I must."', '"I CALL UPON EVERY GREAT POWERS BEFORE I,"',
                '"FROM FATHER CHRISTMAS TO KRIS KRINGLE,"', '"I HARNESS THEE FOR A..."', '"CHRISTMAS"', '"ULTRA"', '"BLAST!"', "For a moment, all you can see is red, green, and white.",
                'Once the blast is over, you notice a several meter wide whole blasted through the wall behind you with a trail spanning to the horizon.', 'How did you even survive that?',
                'Do you have plot armor or something?'],
                ['Santa harnesses his Christmas Spirit and does his iconic and famous Christmas MegaBlast,', 
                'Completely blinding you in its brilliance.', 'Oh, classic Santa!'],
                ['Santa attempts to harness his Christmas Spirit but it seems that the stress of preparing for Christmas has gotten to him.', 'His spirit is considerably weaker.'],
                ['"Hohoho!"', '"I wanted to go this far as much as you but you leave me no choice"', '"CHRISTMAS"', '"SUPER"', '"BLA-"', 'His hat falls off his head, cancelling his attack',
                '"Oh! Pardon me!"'], [])
intimidation = attack('intimidation', 'Intimidation', '', 0, 15, True, True,
                      ['Santa walks up to you and places a hand on your shoulder.', '"220 N 330 W, Amber Avenue."', 'He walks up to Zeep Vorp next', '"114.234.123.65"', 'Finally he approaches Mr. Skellybones.', '"(555), 245-5555"', '"Am I correct?"'],
                      ['Santa pulls out his naughty list and he writes a few names in it.', 'You and your team stress out, worried that he put your names on the list.'],
                      ["Santa begins to charge up a Christmas MegaBlast and you panic for a little bit, until you realize he's been charging it for longer than usual.", 
                        'So you shrug, walk up, and knock his hat off his head.'],
                      ['"Why you have tested me patience for too long!"', '"I am going to say a horrible thing!"', '"You will not even believe what I am about to say!"',
                       'You stress out, worried that Santa is going to destroy his precious, pure image. You brace for the worst.', '"YOU ARE SUBPAR IN SOME OF YOUR HOBBIES!"', 
                       '"do not worry though, practice makes perfect"', '"BUT YOU WILL HAVE TO PRACTICE A LOT!"', 'Santa smirks, proud of his own audacity.'], [])


santa = enemy('Santa Claus', 150, 130, 10, [blast, intimidation], [], [], [])
agent_elf = enemy('Special Agent Pepper', 100, 100, 25, )

viyh = enemy(name='The Voice In Your Head', 
             max_hp=50, max_nerves=100, min_nerves=10, 
             attacks=[pessimism, yell], abilities=[], healing_abilities=[pep_talk], effects=[])

skellybones_boss = enemy('Mr. Skellybones', 70, 100, 10,
                    [bone_blow_enemy], [], [], [])

skellybones_fight = encounter([skellybones_boss], 'Dialogue\opening_cutscene.txt', 'Dialogue/test.txt')

player = ally(name='Unpaid Intern', 
              max_hp=100, max_nerves=100, min_nerves=25, 
              attacks=[kickflip, declaration, pep_talk, apple],effects=[])

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

#if victory:
    #level_up()

    #for ally_char in allies:
       # print(ally_char)
#else:
    #'YOU LOST IDIOT!!!!!!!!'

