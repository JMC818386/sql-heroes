from database.db_connection import execute_query

def get_all_heroes():
    query = """
        SELECT id, name FROM heroes
    """ 
    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"{value[0]}: {value[1]}")

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


input_delete_hero()
