from game_assets import *
from battle import battle
from save_load import player_data
from dialogue_reader import *

# Avery, exploring

# Each main location now has unique mini-locations
main_locations = [
   {
       "name": "Spookyland",
       "mini_locations": ["High Density Housing", 
                          "Pumpkin Patch", 
                          "Abandoned Carnival", 
                          "Mirror Room",
                          "Ghost Ship"],
       'mini_local_desc': [['Following your map, you go to the high density housing.', 'Looking around, you see rows upon rows of graves.', 'Huh, did we wrong turn somewhere.', 'Oh... this is spookyland.'],
                            ['You enter the 87th Annual Spookyland Pumpkin Patch.', 'Given that this is Spookyland, all of the pumpkins are alive!', '"Hey! Human!" says one of the pumpkin.', '"I can make you rich and famous!"',
                             '"Just you wait! I will be the greatest pumpkin the world has ever seen!"', '"I am going solve homelessness and poverty."', '"I am gonna be the greatest philanthropist."', 
                             'As you listen to the pumpkin, a skeleton with carving tools picks it up and takes it away.', '"Just you wait!" says the pumpkin.', 'You never see it again.'],
                            ['You find an abandoned carnival.', "It's barron, empty, and indeed, very spooky.", "You wander around trying to find something or someone.", 'There you find a single skeleton'],
                            ['This is a mirror room'],
                            ['This is a ghost ship']],
       "npcs": ["Carnival Skeleton"],
       "item": "Monocle of Skellybones",
       "boss": skellybones_fight,
       "ally": skellybones_ally,
       "encounter": spooky_monsters_fight,
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
   print(f"Adding '{item}' to inventory...")
   inventory.append(item)

def local_encounter(encounter):
   return battle(player_data['allies'], encounter.enemies, encounter.opening, encounter.closing, player_data['inventory'])

def explore(location):
    # Go through all main locations
    print(f"\n== Entering {location['name']} ==")


    explored = []
    seen_npcs = set()
    victory = False

    while not victory:
        print("\nMini-locations:")
        for i, mini in enumerate(location["mini_locations"], 1):
            status = "✓" if mini in explored else " "
            print(f"{i}. [{status}] {mini}")


        choice = input("Choose a place to explore (1-5): ")
        if not choice.isdigit() or not (1 <= int(choice) <= 5):
            print("Invalid choice.")
            continue


        selected = location["mini_locations"][int(choice) - 1]
        if selected in explored:
            print("You already explored that.")
            continue


        print(f"\nExploring {selected}...")
        if location['mini_local_desc']:
            read_description(location['mini_local_desc'][int(choice) - 1], all_allies)

        if len(explored) > 1:
            # NPC interaction (happens once per NPC)
            for npc in location["npcs"]:
                if npc not in seen_npcs:
                    print(f"You meet {npc}!")
                    if npc == "Carnival Skeleton":
                        print('"Step right up! Step right up!" he says.')
                    elif npc == "Zeep Vorp":
                        print('"Zorp! You’re not supposed to see this!"')
                    elif npc == "Mrs. Claus":
                        print('"Cookies and cocoa, dear?"')
                    elif npc == "President":
                        print('"God bless America."')
                    elif npc == "Vice President":
                        print('"Keep it patriotic."')
                    seen_npcs.add(npc)

        if len(explored) > 2:
            # Fighting the Encounters (happens once per Encounter)
            if location["encounter"]:
                input("Enter anything to fight the encounter...")
                victory = local_encounter(location["encounter"])
                
        explored.append(selected)

    # Once all 5 are explored, give item
    if location["item"]:
        print(f"\nYou have found the item: {location['item']}!")
        add_to_inventory(location["item"])

    # Now start the boss fight if there is one
    if location["boss"]:
        print(f"\nYou’ve reached the final challenge in {location['name']}...")
        input("Press Enter to confront the boss...")
        local_encounter(location["boss"])

        if location['boss'] != None:
            print(f"\nYou’ve reached the final challenge in {location['name']}...")
            input("Press Enter to confront the boss...")
            local_encounter(location["boss"])

        if location["ally"] and location["ally"] not in allies:
            print(f"{location['ally']} has joined your team!")
            player_data['allies'].append(location["ally"])

    else:
        # If ally is gained from exploring only
        if location["ally"] and location["ally"] not in allies:
            print(f"You’ve found {location['ally']} while exploring!")
            allies.append(location["ally"])


# explore(main_locations[0])