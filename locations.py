from InquirePy import inquirer
import time

# InquirePy menu
def inq_select(*args):
    items = [f"({i+1}) {args[i+1]}" for i in range(len(args)-1)]
    menu_input = inquirer.select(
        message=args[0],
        choices=items,
        filter=lambda result: int(result.split(")")[0][1:])
    ).execute()
    return menu_input

# Locations with 8 levels, characters, and bosses
levels = [
    {
        "name": "Location 1: [Insert Location Name]",
        "characters": ["[Insert Character 1]", "[Insert Character 2]"],
        "boss": "[Insert Boss Name]",
        "boss_defeated": False
    },
    {
        "name": "Location 2: [Insert Location Name]",
        "characters": ["[Insert Character 1]"],
        "boss": "[Insert Boss Name]",
        "boss_defeated": False
    },
    {
        "name": "Location 3: [Insert Location Name]",
        "characters": ["[Insert Character 1]"],
        "boss": "[Insert Boss Name]",
        "boss_defeated": False
    },
    {
        "name": "Location 4: [Insert Location Name]",
        "characters": ["[Insert Character 1]"],
        "boss": "[Insert Boss Name]",
        "boss_defeated": False
    },
    {
        "name": "Location 5: [Insert Location Name]",
        "characters": ["[Insert Character 1]"],
        "boss": "[Insert Boss Name]",
        "boss_defeated": False
    },
    {
        "name": "Location 6: [Insert Location Name]",
        "characters": ["[Insert Character 1]"],
        "boss": "[Insert Boss Name]",
        "boss_defeated": False
    },
    {
        "name": "Location 7: [Insert Location Name]",
        "characters": ["[Insert Character 1]"],
        "boss": "[Insert Boss Name]",
        "boss_defeated": False
    },
    {
        "name": "Location 8: [Insert Location Name]",
        "characters": ["[Insert Character 1]"],
        "boss": "[Insert Boss Name]",
        "boss_defeated": False
    }
]

current_level_index = 0

def load_level(index):
    level = levels[index]
    print("\n  Loading:", level["name"])
    print(" Characters:", ", ".join(level["characters"]))
    print(" Boss:", level["boss"], "\n")
    time.sleep(1)

def multiple_location_system():
    global current_level_index

    load_level(current_level_index)

    while current_level_index < len(levels):
        current_level = levels[current_level_index]

        # If the boss is not defeated, player can only stay and re-fight the boss
        while not current_level["boss_defeated"]:
            print(f"\n⚔️ You are fighting {current_level['boss']}...\n")
            # This is where the fight logic would occur (you'll handle that separately)
            # For now, I’ll simulate that the boss is defeated.
            current_level["boss_defeated"] = True  # Mark as defeated after fighting

        # After boss is defeated, allow player to decide: Explore or Move On
        move_on = inq_select(
            "Boss defeated! What would you like to do?",
            "Explore the location",
            "Move on to the next level"
        )

        if move_on == 1:
            print("\n Exploring the location...\n")
            # I will add the exploration content like talking to NPCs, picking up items, etc.
            # For now, it's just a placeholder since I’m not sure on what you exactly want here
            time.sleep(1)
            print("\nYou explore the location and find some hidden treasures!")
            # After exploring, the player will be asked again whether they want to move on.
            continue
        else:
            # Move on to the next level
            current_level_index += 1
            if current_level_index < len(levels):
                load_level(current_level_index)
            else:
                print("\n Congratulations! You've beaten all available levels!\n")
                break

if __name__ == "__main__":
    multiple_location_system()



