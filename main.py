from InquirerPy import inquirer
from dialogue_reader import read_dialogue
from battle import battle
from game_assets import *
import save_load
from explore import *

def start_game():
    read_dialogue('Dialogue\opening_cutscene.txt')
    battle(save_load.player_data['allies'], [viyh], 'Dialogue/tutorial1.txt', 'Dialogue/viyh_closing.txt', save_load.player_data['inventory'])
    explore(main_locations[0], 0)
    save_load.player_data['allies'].append(zeep_vorp_ally)
    explore(main_locations[2], 2)
    # battle(save_load.player_data['allies'], [skellybones_boss], 'Dialogue\skellybones_intro.txt', 'Dialogue/skellybones_outro.txt', save_load.player_data['inventory'])
    #battle([player, skellybones_ally, zeep_vorp_ally], santa_fight.enemies, santa_fight.opening, santa_fight.closing, [sin_off_item, sin_self_item])

def main():
    game_title = "Quest For The Country!"

    while True:
        # Display the title screen header
        print("\n" + "=" * 60)
        print(f"{game_title.center(60)}")
        print("A text-based adventure by Yenesis, Amber, Avery, and Darius".center(60))
        print("=" * 60)
        print()  # Spacing

        choice = inq_select('Use Arrow Keys and "Enter" to navigate menu!', 'New Game', 'Load Game', 'Settings')

        if choice == 1:
            start_game()
        elif choice == 2:
            start_game()
        elif choice == 3:
            settings = inq_select('Which settings would you like to toggle?', 'Fast Skip', 'Debug Mode', 'Back')

        input("\nPress Enter to return to the main menu...")

main()

