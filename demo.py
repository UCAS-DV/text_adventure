from helper_funcs import inq_select

def demo():

    if inq_select('What would you like to do?', 'Go into Bedroom', 'Go into Kitchen', 'Check Inventory') == 1:
        print('This is a place where place things happen')

        if inq_select('What would you like to do?', 'Go Upstairs', 'Enter Hallway', 'Check Inventory') == 1:
            print('Hello I am an NPC who does NPC things')

            if inq_select('What would you like to do?', 'Go into Basement', 'Go outside' 'Check Inventory') == 1:
                print('RAAH I AM A GROUP OF ENEMIES WHO DO ENEMY THINGS')

                if inq_select('What would you like to do?', 'Fight Boss', 'Leave', 'Check Inventory') == 1:
                    print('I AM THE BOSS WHO DOES BOSS THINGS')


demo()