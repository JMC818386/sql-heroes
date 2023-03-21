from database.db_connection import execute_query

def get_all_heroes():
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

def question_prompt():
    answer = input("Press Enter to see a list of heroes...")
    if answer == "": 
        print(get_all_heroes())

question_prompt()