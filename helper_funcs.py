from InquirerPy import inquirer

def inq_select(*args): # *args allows for indefinite parameters, stored in a list, named args 


    items = [f"({i+1}) {args[i+1]}" for i in range(len(args)-1)]   #adds items to a list named items 


    menu_input = inquirer.select( # inquirer.select is a function that’s apart of inquirepy, it has variables in it to determine what it does


        message=args[0], #message is the message at the top, args[0] is the first item in the list, which is the first parameter


        choices=items, #this is the choices the user has to choose from, uses the pre made list items


        filter=lambda result: int(result.split(")")[0][1:])  # takes the users input 


    ).execute() # this runs the code inside of the inquirer.select


    return menu_input #returns the number that the user selected as an integer
