from database.db_connection import execute_query

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




