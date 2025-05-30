#start of inspect charecter code
from game_assets import *
from helper_funcs import inq_select


#OLD CODE
#def old_get_char_stats(char_name):
 #   print(char_name)
  #  if len(char_name.attacks) != 0:
   #     print("Attacks:")
    #for i in range(len(char_name.attacks)):
     #   print(char_name.attacks[i])
    #print("\n")
    #if len(char_name.effects) != 0:
    #    print("Effects")
    #for i in range(len(char_name.effects)):
    #    print(char_name.effects[i])
    #for i in range(len(char_name.heals)):
    #    print(char_name.heals[i])
#OLD CODE

def get_char_stats(char_name):
    expand_settings = {
        "attacks": "expand", #sets expanded attacks menu to be not expanded by default to avoid visual clutter 
        "effects": "expand", #sets expanded attacks menu to be not expanded by default to avoid visual clutter. Expand means that it is currently collapsed, collapse means it is currently expanded.
        "heals": "expand" #sets expanded attacks menu to be not expanded by default to avoid visual clutter 
    }

    while True: #main charecter inspect menu loop 
        print(f"{char_name}\n") # prints all charecter information 

        for attr in ["attacks", "effects", "heals"]: # a for loop that instead of having i (attr is a replacment for i) be numbers, its the items inside the list provided, allowing for repatition unlike the code above which had the same function ran multiple times with names swapped out 
            items = getattr(char_name, attr) # getattr is get attrabutes, it allows the combination of variable values, to become a getting an attribute from a class, so on loop 1 it will get the name the coder entered + attacks which is the attacks list, so if they are inspecting the player it would be player.attacks
            if items: #if there are items in the list, so if there are no items in the effects list or such, it is skipped 
                print(f"{attr.title()}:") # prints the list name with capitalised title, its kept like this instead of having the capitalisation in the name to prevent any errors caused by it
                for item in items: # item is a replacment for i, items is a list, if you put a list as the replacment for range, as stated above, each item will = i instead of i = a number
                    if expand_settings[attr] == "collapse": #checks if expanded information is enabled for each item
                        print(item) #prints the item with extra information like how much damage it does and how many players it targets
                    else:
                        print(item.name) #prints the item with only its name, if the expanded info boleen is false 
                print(" ") #blank print to make a space, not /n because it would make two spaces instead of 1, which i dont want in my formatting

        selection = inq_select( #inquire.py select menu, please see helper_funcs.py for more info on how it works! (actually,  i worked really hard on it to make it efficient and well commented)
            f"Would you like to expand any details to see more information?",
            f"{expand_settings["attacks"]} attack descriptions",
            f"{expand_settings["effects"]} effect descriptions",
            f"{expand_settings["heals"]} healing descriptions",
            f"No thanks (Exit character inspect menu)"
        )

        if selection == 1: #logic behind choosing weather you want to expand the information on each of your items
            if char_name.attacks:
                if expand_settings["attacks"] == "expand": # this if statment checks wether its collapsed or expanded, and toggles it accordingly
                    expand_settings["attacks"] = "collapse"
                else:
                    expand_settings["attacks"] = "expand"
            else:                                          #this else statment is if there are no things in the list, which is rare, but can happen it Continues to avoid the 20 new lines at the end that it has already made
                print("\n" * 30)
                print("This character has no attacks to expand!")
                continue
        elif selection == 2:
            if char_name.effects:
                if expand_settings["effects"] == "expand":
                    expand_settings["effects"] = "collapse"
                else:
                    expand_settings["effects"] = "expand"
            else:
                print("\n" * 30)
                print("This character has no effects to expand!")
                continue
        elif selection == 3:
            if char_name.heals:
                if expand_settings["heals"] == "expand":
                    expand_settings["heals"] = "collapse"
                else:
                    expand_settings["heals"] = "expand"
            else:
                print("\n" * 30)
                print("This character has no healing abilities to expand!")
                continue
        elif selection == 4:
            break
        print("\n" * 30) #this makes it look like the terminal is updating in real time instead of having a bunch of new lines printed



    

get_char_stats(player)