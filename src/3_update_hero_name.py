from database.db_connection import execute_query

def get_all_heroes():
    query = """
        SELECT id, name FROM heroes
    """ 
    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"{value[0]}: {value[1]}")

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

input_update_name()
    
