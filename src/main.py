from database.db_connection import execute_query

#-------------------------------------------ONLOAD INITIATE PROGRAM------------------------------------------#

def begin_game():
    answer = input("Press ENTER begin")
    if answer == "": 
        load_start_menu()

#----------------------------------------------MAIN MENU------------------------------------------#

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
    3: Update Hero's Name
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
        print(input_update_name())
    elif answer == "4":
        print(input_delete_hero())
    print(return_to_main_menu())


#-------------------------------------GENERATE HERO LIST------------------------------------------#

def get_all_heroes():
    query = """
        SELECT id, name FROM heroes
    """ 
    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"{value[0]}: {value[1]}")


#-------------------------------------CREATE NEW HERO------------------------------------------#

def input_create_hero():
    name = input("Enter your new hero's name: ")
    about = input("Enter one sentence to describe your new hero: ")
    biography = input("Enter a few sentences about your hero's back story: ")
    create_new_hero(name, about, biography)

def create_new_hero(name, about, biography):
    query = f"""
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
    """
    execute_query(query, (name, about, biography))
    get_all_heroes()


#-------------------------------------READ HERO PROFILE------------------------------------------#

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

#-------------------------------------UPDATE HERO NAME------------------------------------------#
def input_update_name():
    get_all_heroes()
    number = input("Enter the number next to the hero you want to update: ")
    name = input("Enter the hero's new name: ")
    update_hero_name(name, number)

def update_hero_name(name, number):
    query = f"""
        UPDATE heroes
        SET name = '{name}'
        WHERE id = {number}
    """
    execute_query(query)
    get_all_heroes()
    return_to_main_menu()

#-------------------------------------DELETE HERO------------------------------------------#

def input_delete_hero():
    get_all_heroes()
    num = input("Type the number next to the hero you want to delete...")
    delete_hero(num)

def delete_hero(num):
    get_all_heroes()
    query = f"""
        DELETE FROM heroes 
        WHERE id = '{num}'
    """
    execute_query(query)
    get_all_heroes()
    return_to_main_menu()

#----------------------------------RETURN TO MAIN MENU PROMPT----------------------------------#

def return_to_main_menu():
    answer = input("Press ENTER to return to the main menu.")
    if answer == "": 
        print(load_start_menu())

#----------------------------------------------------------------------------------------------#

begin_game()




