from database.db_connection import execute_query


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


input_get_heroes()

