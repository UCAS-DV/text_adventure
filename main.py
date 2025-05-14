from InquirerPy import inquirer
from dialogue_reader import read_dialogue
from battle import battle
from game_assets import *
import save_load
from explore import *

def start_game():
    read_dialogue('Dialogue/opening/opening_cutscene.txt')
    battle(save_load.player_data['allies'], [viyh], 'Dialogue/opening/tutorial1.txt', 'Dialogue/opening/viyh_outro.txt', save_load.player_data['inventory'])
    explore(main_locations[0], 0)
    save_load.player_data['allies'].append(zeep_vorp_ally)
    explore(main_locations[2], 2)
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

        choice = inq_select('Use the arrow keys and "Enter" to navigate the menus.', 'New Game', 'Load Game', 'Settings')

        match choice:
            case 1:
                start_game()

        input("\nPress Enter to return to the main menu...")

main()
