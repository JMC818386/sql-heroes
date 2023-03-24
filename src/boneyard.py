from database.db_connection import execute_query

#----------------------------------RETURN TO MAIN MENU PROMPT----------------------------------#

def return_to_main_menu():
    answer = input("Press ENTER to return to the main menu.")
    if answer == "": 
        print(load_start_menu())

#----------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------#
# This function gets all names in a numbered list from heroes table
#------------------------------------------------------------------------------------------#

def get_all_heroes():
    query = """
        SELECT name FROM heroes
 
    """ 

    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"{count + 1}: {value[0]}")

def question_prompt():
    answer = input("Press Enter to see a list of heroes...")
    if answer == "": 
        print(get_all_heroes())

question_prompt()

#------------------------------------------------------------------------------------------#
# In these two functions I was attempting to get name, about_me and biography from an individual
# hero by creating a function for each hero, then using if/elif in an input function to call
# each function based on it's assigned list number
#------------------------------------------------------------------------------------------#
def get_chill_woman_profile():
    query = """
        SELECT 
            name, 
            about_me, 
            biography 
        FROM heroes 
        WHERE name LIKE 'Chill Woman'
    """ 

    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"{count + 1} : {value[0]} : {value[1]} : {value[2]}")

def get_the_seer_profile():
    query = """
        SELECT 
            name, 
            about_me, 
            biography 
        FROM heroes 
        WHERE name LIKE 'The Seer'
    """ 

    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"{count + 1} : {value[0]} : {value[1]} : {value[2]}")

def question_prompt():
    answer = input("Press Enter to see a list of heroes...")
    if answer == "1": 
        print(get_chill_woman_profile())
    elif answer == "2":
        print(get_the_seer_profile())

question_prompt()
