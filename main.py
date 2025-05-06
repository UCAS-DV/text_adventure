from helper_funcs import inq_select
import game_assets
import battle

def main():
    input('-~-~-~-~- Quest for the Country! -~-~-~-~-')

    victory, inventory = battle.battle(game_assets.allies, game_assets.enemies, 'Dialogue\opening_cutscene.txt', 'Dialogue/tutorial1.txt', game_assets.test_inventory)

main()

    