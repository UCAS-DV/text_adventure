import inquirer

def main_menu():
    game_title = "[ Quest for the Country]"

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
            " Save Game",
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
            print("Starting a new game... (placeholder)")
        elif answer == " Load Game":
            print("Loading game... (placeholder)")
        elif answer == " Save Game":
            print("Saving game... (placeholder)")
        elif answer == " Settings":  
            print("Opening settings... (placeholder)")
        elif answer == " Exit":
            print("Exiting game. Goodbye!")
            break

        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main_menu()




