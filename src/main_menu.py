from database.db_connection import execute_query

def load_start_menu():
    print("     _______.  ______      __          __    __   _______ .______        ______    _______     _______.")
    print("    /       | /  __  \    |  |        |  |  |  | |   ____||   _  \      /  __  \  |   ____|   /       |")
    print("   |   (----`|  |  |  |   |  |        |  |__|  | |  |__   |  |_)  |    |  |  |  | |  |__     |   (----`")
    print("    \   \    |  |  |  |   |  |        |   __   | |   __|  |      /     |  |  |  | |   __|     \   \    ")
    print(".----)   |   |  `--'  '--.|  `----.   |  |  |  | |  |____ |  |\  \----.|  `--'  | |  |____.----)   |   ")
    print("|_______/     \_____\_____\_______|   |__|  |__| |_______|| _| `._____| \______/  |_______|_______/    ")
    print("                                                                                                       ")
    print("                             If you're not having fun, you're wrong.")
    print("                                                                                                       ")
    print("                                                                                                       ")
    print("1: Create a New Hero")
    print("2: Read a Hero's Profile")
    print("3: Update Hero's Ability")
    print("4: Delete a Hero")
    print("                                                                                                       ")
    input_main_menu()


    
def get_all_heroes():
    query = """
        SELECT name FROM heroes
 
    """ 

    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"{count + 1}: {value[0]}")

def input_main_menu():
    answer = input("Enter the number next your selection and press ENTER!")
    if answer == "1": 
        print(get_all_heroes())
    elif answer == "2":
        print(get_all_heroes())
    elif answer == "3":
        print(get_all_heroes())
    elif answer == "4":
        print(get_all_heroes())

load_start_menu()