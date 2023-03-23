from database.db_connection import execute_query

def create_new_hero():
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (name, about_me, biography);
    """

def input_new_hero():
    pass