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
    "level": None,
    "location": None,
    "allies": [],
    "inventory": []
}
#yayayaya

def save_game(data):
    with open(SAVE_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Level", "Location", "Allies", "Inventory"])
        writer.writerow([data["level"], data["location"], ";".join(data["allies"]), ";".join(data["inventory"])])
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
            print(f"Level: {player_data['level']}")
            print(f"Location: {player_data['location']}")
            print(f"Allies: {player_data['allies']}")
            print(f"Inventory: {player_data['inventory']}\n")
        elif choice == 4:
            print("\n Exiting the game. Goodbye!")
            break

if __name__ == "__main__":
    main_menu()



