from database.db_connection import execute_query

# INSERT INTO movies VALUES (4, "Toy Story 4", "El Directore", 2015, 90);
def get_all_heroes():
    query = """
        SELECT name FROM heroes
    """ 
    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"{count + 1}: {value[0]}")

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

input_create_hero()