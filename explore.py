from game_assets import *
from battle import battle
from save_load import player_data
from save_load import save_game
from dialogue_reader import *

# Avery, exploring

# Each main location now has unique mini-locations
main_locations = [
   {
       "name": "Spookyland",
       "mini_locations": ["Strength Tester", 
                          "Pumpkin Patch", 
                          "Ring Toss", 
                          "Haunted House",
                          "Entrance"],
       'mini_local_desc': [[''],
                            ['You enter the 87th Annual Spookyland Pumpkin Patch of the carnival!', 'Given that this is Spookyland, all of the pumpkins are alive!', '"Hey! Human!" says one of the pumpkin.', '"I can make you rich and famous!"',
                             '"Just you wait! I will be the greatest pumpkin the world has ever seen!"', '"I am going solve homelessness and poverty."', '"I am gonna be the greatest philanthropist."', 
                             'As you listen to the pumpkin, a skeleton with carving tools picks it up and takes it away.', '"Just you wait!" says the pumpkin.', 'You never see it again.'],
                            ['You find a ring toss game without an operator.', "There's a sign reading:", '"To the no one who is playing this game. Just take a prize. I really do not care."', 'You shrug and take a prize.'],
                            [''],
                            []],
       "intro": 'Dialogue\spookyland_entrance.txt',
       "npc": {'dialogue': "Dialogue\carnival_skeleton.txt", 'position': '1'},
       "item": {'item': sin_off_item, 'position': '3'},
       "boss": {'boss_encounter': skellybones_fight, 'position': '5'},
       "ally": skellybones_ally,
       "encounter": {'fight': spooky_monsters_fight, 'position': '4'},
   },
   {
       "name": "Area 51",
       "mini_locations": ["Alien Lab", "Crash Site", "Hologram Hall", "Containment Cell", "Hover Pad"],
       "npcs": ["Zeep Vorp"],
       "item": "Alien Cat",
       "boss": None,
       "ally": "Zeep Vorp",
       "encounter": None,
   },
   {
       "name": "North Pole",
       "mini_locations": ["Workshop", "Sleigh Garage", "Elf Dorms", "Gift Storage", "Reindeer Field"],
       "npcs": ["Mrs. Claus"],
       "item": "Hat of Santa Claus",
       "boss": "Santa Claus",
       "ally": "Special Ops Elf",
       "encounter": "Special Ops Elf and Reindeer Team",
   },
   {
       "name": "White House",
       "mini_locations": ["Oval Office", "War Room", "Press Room", "Garden", "Lincoln Bedroom"],
       "npcs": ["President", "Vice President"],
       "item": "Block of Patriotism",
       "boss": "Zeep Vorp",
       "ally": None,
       "encounter": None,
   }
]


# Placeholder inventory and allies system
inventory = []
allies = []

def add_to_inventory(item):
   player_data['inventory'].append(item)

def local_encounter(encounter):
   return battle(player_data['allies'], encounter.enemies, encounter.opening, encounter.closing, player_data['inventory'])

def explore(location, index):
    # Go through all main locations

    player_data['location'] = index 
    save_game(player_data)

    print(f"\n== Entering {location['name']} ==")

    read_dialogue(location['intro'])

    explored = []
    seen_npcs = set()
    victory = False
    boss_victory = False

    while not boss_victory:
        print("\nMini-locations:")
        for i, mini in enumerate(location["mini_locations"], 1):
            status = "✓" if mini in explored else " "
            print(f"{i}. [{status}] {mini}")


        choice = input("Choose a place to explore (1-5): ")
        if not choice.isdigit() or not (1 <= int(choice) <= 5):
            print("Invalid choice.")
            continue

        selected = location["mini_locations"][int(choice) - 1]

        # Read place description
        print(f"\nExploring {selected}...")

        # IF not at an npc, encounter, or boss fight, read place description
        if choice != location['npc']['position'] or choice != location['encounter']['position'] or choice != location['boss']['position']:
            read_description(location['mini_local_desc'][int(choice) - 1], all_allies)

        # IF at NPC location, read NPC dialogue
        if choice == location['npc']['position']:
            read_dialogue(location['npc']['dialogue'])

        # IF at encounter location, enter encounter
        if location['encounter'] != None:
            if choice == location['encounter']['position'] and victory == False:
                victory = local_encounter(location["encounter"]['fight'])
                
        explored.append(selected)

        # IF at item location, get item
        if choice == location["item"]['position']:
            print(f"\nYou have found the item: {location['item']['item'].name}!")
            add_to_inventory(location["item"]['item'])

        # Now start the boss fight if there is one
        if location['boss'] != None:
            if choice == location["boss"]['position']:
                boss_victory = local_encounter(location["boss"]['boss_encounter'])

    if location['ally'] != None:
        if location["ally"] and location["ally"] not in allies:
            print(f"{location['ally'].name} has joined your team!")
            player_data['allies'].append(location["ally"])

    else:
        # If ally is gained from exploring only
        if location["ally"] and location["ally"] not in allies:
            print(f"You’ve found {location['ally']} while exploring!")
            allies.append(location["ally"])

        


# explore(main_locations[0])