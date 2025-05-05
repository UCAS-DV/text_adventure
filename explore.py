# See when the player can explore certain areas and give them the options to explore that scetion of the map they unlocked frm defeting the previous boss
# Chicken jockey

# Avery, exploring

import random

# Class for each place in a location
class Place:
    def __init__(self, name):
        self.name = name
        self.explored = False
        self.content = None

# Class for each main location
class Location:
    def __init__(self, name, contents):
        self.name = name
        self.places = [Place(f"Place {i+1}") for i in range(5)]
        self.contents = contents
        self.setup_contents()

    # Randomly assign content to places; boss is always last
    def setup_contents(self):
        keys = list(self.contents.keys())
        boss_key = [k for k in keys if "Boss" in k][0]
        keys.remove(boss_key)
        random.shuffle(self.places)
        for key in keys:
            self.places.pop().content = (key, self.contents[key])
        self.places[0].content = (boss_key, self.contents[boss_key])

    # Explore an unvisited place
    def explore(self):
        options = [p for p in self.places if not p.explored]
        for i, p in enumerate(options):
            print(f"{i+1}. {p.name}")
        choice = int(input("Choose a place to explore: ")) - 1
        chosen = options[choice]
        chosen.explored = True
        key, value = chosen.content
        print(f"You found: {key} - {value}")
        return key, value

# Locations with content
game_map = [
    ("House", {
        "NPC": "Cat (says 'meow' in a deep voice)",
        "Item": "Hopes and Determination",
        "Boss": "Voice In Your Head"
    }),
    ("Spookyland", {
        "NPC": "Skeleton in the carnival",
        "Encounter": "Ghouls and Ghosts",
        "Item": "Monocle of Skellybones",
        "Boss": "Mr. Skellybones",
        "Ally": "Mr. Skellybones"
    }),
    ("Area 51", {
        "NPC": "Zeep Vorp",
        "Encounter": "Hostile Aliens",
        "Item": "Alien Cat",
        "Ally": "Zeep Vorp"
    }),
    ("North Pole", {
        "NPC": "Mrs. Claus",
        "Encounter": "Special Ops Elf and Reindeer Team",
        "Item": "Hat of Santa Claus",
        "Boss": "Santa Claus",
        "Ally": "Special Ops Elf"
    }),
    ("White House", {
        "NPC": "President and Vice President",
        "Item": "Block of Patriotism",
        "Boss": "Zeep Vorp"
    })
]

# Track what has been gained
obtained_items = set()
obtained_allies = set()
encounters_done = set()
defeated_bosses = set()

# Go through each main location
for loc_name, contents in game_map:
    print(f"\n--- {loc_name} ---")
    location = Location(loc_name, contents)
    while True:
        key, value = location.explore()
        if "Boss" in key:
            print(f"Boss fight triggered: {value}")
            defeated_bosses.add(value)
            break
        elif key == "Item":
            if "Boss" in contents and contents["Boss"] in defeated_bosses:
                obtained_items.add(value)
                print(f"Item obtained: {value}")
            elif "Boss" not in contents:
                obtained_items.add(value)
                print(f"Item obtained: {value}")
            else:
                print(f"You must defeat {contents['Boss']} to gain this item.")
        elif key == "Ally":
            if "Boss" in contents and contents["Boss"] in defeated_bosses:
                obtained_allies.add(value)
                print(f"Ally joined: {value}")
            elif "Encounter" in contents and contents["Encounter"] in encounters_done:
                obtained_allies.add(value)
                print(f"Ally joined: {value}")
            else:
                print("You need to trigger the right condition to unlock this ally.")
        elif key == "Encounter":
            encounters_done.add(value)
            print(f"Encounter complete: {value}")
        elif key == "NPC":
            print(f"NPC encountered: {value}")

print("\nAll locations explored. Game progression complete.")