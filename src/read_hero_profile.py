from database.db_connection import execute_query

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

def input_hero_profile():
    answer = input("Press Enter to see a list of heroes...")
    if answer == "1": 
        print(get_chill_woman_profile())
    elif answer == "2":
        print(get_the_seer_profile())

input_hero_profile()