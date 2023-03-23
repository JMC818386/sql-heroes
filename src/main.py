from database.db_connection import execute_query


def begin_game():
    answer = input("Press ENTER begin")
    if answer == "": 
        load_start_menu()


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


def input_main_menu():
    answer = input("Enter the number next your selection and press ENTER!")
    if answer == "1": 
        print(input_create_hero())
    elif answer == "2":
        print(input_get_heroes())
    elif answer == "3":
        print(input_update_hero())
    elif answer == "4":
        print(input_delete_hero())
    print(return_to_main_menu())


def get_all_heroes():
    query = """
        SELECT name FROM heroes
    """ 
    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"{count + 1}: {value[0]}")
    


def input_get_heroes():
    get_all_heroes()
    hero_number = input("Type the number next to the hero you want to see...")
    get_hero_profile(hero_number)

def get_hero_profile(num):
    query = f"""
        SELECT
            id,
            name,
            about_me,
            biography
        FROM heroes
        WHERE heroes.id = {num};
    """ 

    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"""
        {value[0]}: {value[1]}
        {value[2]}
        {value[3]}""")


def input_hero_profile():
    answer = input("Type the number next to the hero you want to see...")
    if answer == "": 
        get_hero_profiles()


def return_to_main_menu():
    answer = input("Press ENTER to return to the main menu.")
    if answer == "": 
        print(load_start_menu())

begin_game()




