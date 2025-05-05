import inquirer
from dialogue_reader import read_dialogue
from battle import battle
from game_assets import *
import save_load

def start_game():
    read_dialogue('Dialogue\opening_cutscene.txt')
    battle(save_load.player_data['allies'], enemies, 'Dialogue/tutorial1.txt', 'Dialogue/test.txt', save_load.player_data['inventory'])

def main():
    game_title = "Quest For The Country!"

    while True:
        # Display the title screen header
        print("\n" + "=" * 60)
        print(f"{game_title.center(60)}")
        print("A text-based adventure by Yenesis, Amber, Avery, and Darius".center(60))
        print("=" * 60)
        print()  # Spacing

        # Menu options
        menu_options = [
            " Start New Game",
            " Load Game",
            " Settings",
            " Exit"
        ]

        questions = [
            inquirer.List(
                "menu",
                message="Use arrow keys to navigate and Enter to select:",
                choices=menu_options,
            )
        ]

        answer = inquirer.prompt(questions)["menu"]

        # Handle choices replace the placeholder text with actual game startup logic 
        if answer == " Start New Game":
            start_game()
        elif answer == " Load Game":
            print("Loading game... (placeholder)")
        elif answer == " Settings":  # Fixed the curly quotes here
            print("Opening settings... (placeholder)")
        elif answer == " Exit":
            print("Exiting game. Goodbye!")
            break

        input("\nPress Enter to return to the main menu...")

main()




