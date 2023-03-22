from database.db_connection import execute_query

def load_start_menu():
    print("""
         _______.  ______      __          __    __   _______ .______        ______    _______     _______.
        /       | /  __  \    |  |        |  |  |  | |   ____||   _  \      /  __  \  |   ____|   /       |
       |   (----`|  |  |  |   |  |        |  |__|  | |  |__   |  |_)  |    |  |  |  | |  |__     |   (----`
        \   \    |  |  |  |   |  |        |   __   | |   __|  |      /     |  |  |  | |   __|     \   \    
    .----)   |   |  `--'  '--.|  `----.   |  |  |  | |  |____ |  |\  \----.|  `--'  | |  |____.----)   |   
    |_______/     \_____\_____\_______|   |__|  |__| |_______|| _| `._____| \______/  |_______|_______/    
                                                                                                           
                                 If you're not having fun, you're wrong.
                                                                                                           
                                                                                                           
    1: Create a New Hero
    2: Read a Hero's Profile
    3: Update Hero's Ability
    4: Delete a Hero
                                                                                                           
    """)
    input_main_menu()

def get_all_heroes():
    query = """
        SELECT name FROM heroes
 
    """ 

    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"{count + 1}: {value[0]}")
        

def input_main_menu():
    answer = input("Enter the number next your selection and press ENTER!")
    if answer == "1": 
        print(get_all_heroes())
    elif answer == "2":
        print(read_hero_profile())
    elif answer == "3":
        print(update_hero_ability())
    elif answer == "4":
        print(delete_hero())
    print(return_to_main_menu())

def return_to_main_menu():
    answer = input("Press ENTER to return to the main menu.")
    if answer == "": 
        print(load_start_menu())

def begin_game():
    answer = input("Press ENTER begin")
    if answer == "": 
        print(load_start_menu())

begin_game()