from database.db_connection import execute_query
import os
#
os.system('clear')
#-------------------------------------------ONLOAD INITIATE PROGRAM------------------------------------------#

def begin_game():
    os.system('clear')
    answer = input("Press ENTER begin")
    if answer == "": 
        load_start_menu()

#----------------------------------------------MAIN MENU------------------------------------------#

def load_start_menu():
    os.system('clear')
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
    answer = input("""
    Enter the number next your selection and press ENTER!""")
    if answer == "1": 
        input_create_hero()
    elif answer == "2":
        input_get_heroes()
    elif answer == "3":
        input_update_name()
    elif answer == "4":
        input_delete_hero()



#-------------------------------------GENERATE HERO LIST------------------------------------------#

def get_all_heroes():
    query = """
        SELECT id, name FROM heroes
    """ 
    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"{value[0]}: {value[1]}")


#-------------------------------------CREATE NEW HERO------------------------------------------#
def new_hero_ascii():
    print("""
    
.__   __.  ___________    __    ____     __    __   _______ .______        ______   
|  \ |  | |   ____\   \  /  \  /   /    |  |  |  | |   ____||   _  \      /  __  \  
|   \|  | |  |__   \   \/    \/   /     |  |__|  | |  |__   |  |_)  |    |  |  |  | 
|  . `  | |   __|   \            /      |   __   | |   __|  |      /     |  |  |  | 
|  |\   | |  |____   \    /\    /       |  |  |  | |  |____ |  |\  \----.|  `--'  | 
|__| \__| |_______|   \__/  \__/        |__|  |__| |_______|| _| `._____| \______/  


    """)
def input_create_hero():
    os.system('clear')
    new_hero_ascii()
    name = input("""
    Enter your new hero's name: """)
    about = input("""
    Enter one sentence to describe your new hero: """)
    biography = input("""
    Enter a few sentences about your hero's back story: """)
    create_new_hero(name, about, biography)

def create_new_hero(name, about, biography):
    query = f"""
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
    """
    execute_query(query, (name, about, biography))
    os.system('clear')
    new_hero_ascii()
    get_all_heroes()
    print(f"""
    YOU JUST CREATED A NEW HERO NAMED {name}!
    """)
    return_to_create_hero()

#----------------------------------RETURN TO CREATE HERO PROMPT----------------------------------#

def return_to_create_hero():
    answer = input("""
    Would you like to to create another hero? (Y/N): """)
    if answer == "Y": 
        input_create_hero()
    elif answer == "N":
        load_start_menu()
    elif answer != "Y" or "N":
        return_to_create_hero()

#----------------------------------------------------------------------------------------------#


#-------------------------------------READ HERO PROFILE------------------------------------------#
def profile_ascii():
    print("""

.______   .______        ______    _______  __   __       _______     _______.
|   _  \  |   _  \      /  __  \  |   ____||  | |  |     |   ____|   /       |
|  |_)  | |  |_)  |    |  |  |  | |  |__   |  | |  |     |  |__     |   (----`
|   ___/  |      /     |  |  |  | |   __|  |  | |  |     |   __|     \   \    
|  |      |  |\  \----.|  `--'  | |  |     |  | |  `----.|  |____.----)   |   
| _|      | _| `._____| \______/  |__|     |__| |_______||_______|_______/    
                                                                              

    """)

def input_get_heroes():
    os.system('clear')
    profile_ascii()
    get_all_heroes()
    hero_number = input("""
    Type the number next to the hero you want to see: """)
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
    os.system('clear')
    profile_ascii()
    for count, value in enumerate(names):
        print(f"""
Name:
{value[1]}

About:
{value[2]}

Bio:
{value[3]}

""")

    return_to_read_profile()
#----------------------------------RETURN TO READ PROFILE PROMPT----------------------------------#

def return_to_read_profile():
    answer = input("""
    Would you like to to read another heroes profile? (Y/N): """)
    if answer == "Y": 
        input_get_heroes()
    elif answer == "N":
        load_start_menu()
    elif answer != "Y" or "N":
        return_to_read_profile()

#----------------------------------------------------------------------------------------------#

#-------------------------------------UPDATE HERO NAME------------------------------------------#
def update_ascii():
    print("""

 __    __  .______    _______       ___   .___________. _______ 
|  |  |  | |   _  \  |       \     /   \  |           ||   ____|
|  |  |  | |  |_)  | |  .--.  |   /  ^  \ `---|  |----`|  |__   
|  |  |  | |   ___/  |  |  |  |  /  /_\  \    |  |     |   __|  
|  `--'  | |  |      |  '--'  | /  _____  \   |  |     |  |____ 
 \______/  | _|      |_______/ /__/     \__\  |__|     |_______|
                                                                

    """)

def input_update_name():
    os.system('clear')
    update_ascii()
    get_all_heroes()
    number = input("""
    Enter the number next to the hero you want to update: """)
    name = input("""
    Enter the hero's new name: """)
    update_hero_name(name, number)

def update_hero_name(name, number):
    os.system('clear')
    query = f"""
        UPDATE heroes
        SET name = '{name}'
        WHERE id = {number}
    """
    execute_query(query)
    os.system('clear')
    update_ascii()
    get_all_heroes()
    print(f"""
    YOU'VE JUST UPDATED THIS HERO'S NAME TO {name}!
    """)
    return_to_update_name()

#----------------------------------RETURN TO UPDATE NAME PROMPT----------------------------------#

def return_to_update_name():
    answer = input("""
    Would you like to update another hero's name? (Y/N): """)
    if answer == "Y": 
        input_update_name()
    elif answer == "N":
        load_start_menu()
    elif answer != "Y" or "N":
        return_to_update_name()
    

#----------------------------------------------------------------------------------------------#

#-------------------------------------DELETE HERO------------------------------------------#
def delete_ascii():
    print("""

 _______   _______  __       _______ .___________. _______ 
|       \ |   ____||  |     |   ____||           ||   ____|
|  .--.  ||  |__   |  |     |  |__   `---|  |----`|  |__   
|  |  |  ||   __|  |  |     |   __|      |  |     |   __|  
|  '--'  ||  |____ |  `----.|  |____     |  |     |  |____ 
|_______/ |_______||_______||_______|    |__|     |_______|
                                                           
                                                     
    """)

def input_delete_hero():
    os.system('clear')
    delete_ascii()
    get_all_heroes()
    num = input("""
    Type the number next to the hero you want to delete...""")
    delete_hero(num)

def delete_hero(num):
    os.system('clear')
    delete_ascii()
    get_all_heroes()
    query = f"""
        DELETE FROM heroes 
        WHERE id = '{num}'
    """
    execute_query(query)
    os.system('clear')
    delete_ascii()
    get_all_heroes()
    return_to_delete_hero()

#----------------------------------RETURN TO DELETE HERO PROMPT----------------------------------#

def return_to_delete_hero():
    answer = input("""
    Would you like to delete another hero? (Y/N): """)
    if answer == "Y": 
        input_delete_hero()
    elif answer == "N":
        load_start_menu()
    elif answer != "Y" or "N":
        return_to_delete_hero()

#----------------------------------------------------------------------------------------------#

begin_game()




