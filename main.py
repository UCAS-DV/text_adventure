from InquirerPy import inquirer
from dialogue_reader import read_dialogue
from battle import battle
from game_assets import *
from save_load import *
from explore import *
from extras import extras_main

# Runs game by going through game sequence
def start_game():
    save_game({
    "location": 0,
    "allies": [player],
    "inventory": []
    })
    read_dialogue('Dialogue/opening/opening_cutscene.txt')
    battle(player_data['allies'], [viyh], 'Dialogue/opening/tutorial1.txt', 'Dialogue/opening/viyh_outro.txt', player_data['inventory'])
    explore(main_locations[0], 0)
    explore(main_locations[1], 1)
    explore(main_locations[2], 2)
    player_data['allies'] = [player, skellybones_ally, pepper]
    explore(main_locations[3], 3)

# Runs game by going through game sequence depending on the progress the player has
def load_game_main():
    player_data = load_game()
    #print(player_data)

    # Loads
    match int(player_data['location']):
        case 0:
            explore(main_locations[0], 0)
            explore(main_locations[1], 1)
            explore(main_locations[2], 2)
            player_data['allies'] = [player, skellybones_ally, pepper]
            explore(main_locations[3], 3)
        case 1:
            explore(main_locations[1], 1)
            explore(main_locations[2], 2)
            player_data['allies'] = [player, skellybones_ally, pepper]
            explore(main_locations[3], 3)
        case 2:
            explore(main_locations[2], 2)
            player_data['allies'] = [player, skellybones_ally, pepper]
            explore(main_locations[3], 3)
        case 3:
            player_data['allies'] = [player, skellybones_ally, pepper]
            explore(main_locations[3], 3)

def main():
    game_title = "Quest For The Country!"

    while True:
        # Display the title screen header
        print("\n" + "=" * 60)
        print(f"{game_title.center(60)}")
        print("A text-based adventure by Yenesis, Amber, Avery, and Darius".center(60))
        print("=" * 60)
        print()  # Spacing

        choice = inq_select('Use the arrow keys and "Enter" to navigate the menus.', 'New Game', 'Load Game', 'Extras')

        match choice:
            case 1:
                start_game()
            case 2:
                load_game_main()
            case 3:
                extras_main()


main()
