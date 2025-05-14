from helper_funcs import inq_select
import game_assets
from image_loader import display_image
def extras_main():
    while True:
        debug_str = f"Debug attacks: {game_assets.debug_mode}"
        choice = inq_select("Modify:", debug_str, "View map", "Unused inspect characters", "Exit to main menu")

        match choice:
            case 1:
                if game_assets.debug_mode:
                    game_assets.debug_mode = False
                elif not game_assets.debug_mode:
                    game_assets.debug_mode = True
            case 2:
                display_image()
            case 3:
                print("WIP")

    

extras_main()
