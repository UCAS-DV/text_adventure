# Story progression system
# Chicken jockey

from game_assets import *
from battle import battle
from save_load import player_data

# Avery, exploring

# Each main location now has unique mini-locations
main_locations = [
   {
       "name": "Spookyland",
       "mini_locations": ["Carnival Tent", "Haunted Maze", "Graveyard", "Mirror Room", "Ghost Ship"],
       "npcs": ["Carnival Skeleton"],
       "item": "Monocle of Skellybones",
       "boss": skellybones_fight,
       "ally": "Mr. Skellybones"
   },
   {
       "name": "Area 51",
       "mini_locations": ["Alien Lab", "Crash Site", "Hologram Hall", "Containment Cell", "Hover Pad"],
       "npcs": ["Zeep Vorp"],
       "item": "Alien Cat",
       "boss": None,
       "ally": "Zeep Vorp"
   },
   {
       "name": "North Pole",
       "mini_locations": ["Workshop", "Sleigh Garage", "Elf Dorms", "Gift Storage", "Reindeer Field"],
       "npcs": ["Mrs. Claus"],
       "item": "Hat of Santa Claus",
       "boss": "Santa Claus",
       "ally": "Special Ops Elf"
   },
   {
       "name": "White House",
       "mini_locations": ["Oval Office", "War Room", "Press Room", "Garden", "Lincoln Bedroom"],
       "npcs": ["President", "Vice President"],
       "item": "Block of Patriotism",
       "boss": "Zeep Vorp",
       "ally": None
   }
]


# Placeholder inventory and allies system
inventory = []
allies = []


def add_to_inventory(item):
   print(f"Adding '{item}' to inventory...")
   inventory.append(item)


def local_encounter(encounter):
   battle(player_data['allies'], encounter.enemies, encounter.opening, encounter.closing, player_data['inventory'])


def explore(location):
    # Go through all main locations
    print(f"\n== Entering {location['name']} ==")


    explored = []
    seen_npcs = set()


    while len(explored) < 5:
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


        # NPC interaction (happens once per NPC)
        for npc in location["npcs"]:
            if npc not in seen_npcs:
                print(f"You meet {npc}!")
                if npc == "Cat":
                    print('"Meow," says the cat in a deep voice.')
                elif npc == "Carnival Skeleton":
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


        if location["ally"] and location["ally"] not in allies:
            print(f"{location['ally']} has joined your team!")
            allies.append(location["ally"])

    else:
        # If ally is gained from exploring only
        if location["ally"] and location["ally"] not in allies:
            print(f"You’ve found {location['ally']} while exploring!")
            allies.append(location["ally"])


explore(main_locations[0])