
# Converts choosen dialogue file to a list of strings
def read_dialogue_file(filepath):
    with open(filepath, 'r') as dialogue_file:
        dialogue_string = dialogue_file.read()
        dialogue = dialogue_string.split('\n')

    return dialogue

# Prints dialogue
def read_dialogue(filepath):

    # Gets dialogue string and beginning dialogue path
    dialogue = read_dialogue_file(filepath)
    target_path = '1'

    for line in dialogue:
        path = line[:1]

        # IF dialogue on current path, print dialogue
        if path == target_path:
            input(f'{line[1:]} (Enter to Continue)')
        
        elif path == '`':
            decisions = line.split('`')

            # Present dialogue options
            while True:
                print(f'1. {decisions[1]}')
                print(f'2. {decisions[2]}')
                target_path = input('What do you want to do (Enter Number): ')

                if target_path in ['1', '2']:
                    break

def read_description(description):
    for line in description:
        input(f'{line} (Enter to Continue)')

# read_dialogue('Dialogue/opening_cutscene.txt')