main_locations = [
   {
       "name": "House",
       "mini_locations": ["Living Room", "Kitchen", "Backyard", "Bathroom", "Basement"],
       "npcs": ["Cat"],
       "item": "Hopes and Determination",
       "boss": "Voice In Your Head",
       "ally": None
   },
   {
       "name": "Spookyland",
       "mini_locations": ["Carnival Tent", "Haunted Maze", "Graveyard", "Mirror Room", "Ghost Ship"],
       "npcs": ["Skeleton in the carnival"],
       "item": "Monocle of Skellybones",
       "boss": "Mr. Skellybones",
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


def start_boss_battle(boss_name):
   print(f"\n*** Boss Battle Started: {boss_name} ***\n")


# Go through all main locations
for location in main_locations:
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
               elif npc == "Skeleton in the carnival":
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
       start_boss_battle(location["boss"])


       if location["ally"] and location["ally"] not in allies:
           print(f"{location['ally']} has joined your team!")
           allies.append(location["ally"])


   else:
       # If ally is gained from exploring only
       if location["ally"] and location["ally"] not in allies:
           print(f"You’ve found {location['ally']} while exploring!")
           allies.append(location["ally"])


print("\n== STORY COMPLETE ==")
import csv
import os
from InquirerPy import inquirer

# Inquire function
def inq_select(*args):
    items = [f"({i+1}) {args[i+1]}" for i in range(len(args)-1)]
    menu_input = inquirer.select(
        message=args[0],
        choices=items,
        filter=lambda result: int(result.split(")")[0][1:])
    ).execute()
    return menu_input

# File to store saves
SAVE_FILE = "save_file.csv"

# Empty player data (waiting to be loaded)
player_data = {
    "location": None,
    "allies": [],
    "inventory": []
}

def save_game(data):
    with open(SAVE_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Level", "Location", "Allies", "Inventory"])
        writer.writerow([data["location"], ";".join(data["allies"]), ";".join(data["inventory"])])
    print("\n Game saved successfully!\n")

def load_game():
    if not os.path.exists(SAVE_FILE):
        print("\n No save file found.\n")
        return None

    with open(SAVE_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        
        # Make sure we're reading a valid row (not empty or malformed)
        for row in reader:
            # Check if the necessary fields are present and not empty
            level_str = row["Level"].strip()
            if not level_str:  # If the level is empty
                print("\nError: Level data is missing or invalid.\n")
                return None
            
            try:
                data = {
                    "level": int(level_str),  # Convert level safely
                    "location": row["Location"].strip() if row["Location"] else "Unknown",
                    "allies": row["Allies"].split(";") if row["Allies"] else [],
                    "inventory": row["Inventory"].split(";") if row["Inventory"] else []
                }
                print("\n Game loaded successfully!\n")
                return data
            except ValueError:
                print("\nError: Invalid value for level in the save file.\n")
                return None  # In case of a malformed level, return None
    return None

def main_menu():
    while True:
        choice = inq_select(
            "Main Menu:",
            "Save Game",
            "Load Game",
            "Show Current Data",
            "Exit"
        )

        if choice == 1:
            save_game(player_data)
        elif choice == 2:
            loaded_data = load_game()
            if loaded_data:
                player_data.update(loaded_data)
        elif choice == 3:
            print("\n Current Player Data:")
            print(f"Location: {player_data['location']}")
            print(f"Allies: {player_data['allies']}")
            print(f"Inventory: {player_data['inventory']}\n")
        elif choice == 4:
            print("\n Exiting the game. Goodbye!")
            break

if __name__ == "__main__":
    main_menu()



