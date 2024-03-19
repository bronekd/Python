print("Hello world")
# příkaz git pull stáhnu doma na PC


def print_menu():
    print("""
    [1] - vypiš položky
    [2] - vyhledej položky
    [3] - přidej položky
    [4] - smaž položky
    [5] - nahrad položky
    [6] - exit
    """)

def search(db, name):
    for db in my_items:
        print(db)

def add_item():
    pass

def print_item(db):
    print("Aktuální seznam knížek")
    for item in db:
        print(f"Jméno: {item['name']}, autor: {item['author']}")
    print("----------------------------")
    print()
def delete_item():
    pass

def replace_item():
    pass

def get_input():
    input("Zadej hodnotu výběru: ")


def run():
    # seznam se slovníkem
    db = [{"name": "Hamlet",
          "author": "Schakespeare"},
          {"name": "harry potter",
           "author": "jk rowling"}]
    # ukázka db2
    db2 = {"adam": 198,
           "tom": 206}

    print(" vítej v programu")

    while True:
        print_menu()
        user_choice = get_input()

        if user_choice == 1:
            print_item(db)

        elif user_choice == 2:
            #print(search(db, "harry potter"))
            pass

        elif user_choice == 3:
            pass

        elif user_choice == 4:
            pass

        elif user_choice == 5:
            pass

        elif user_choice == 6:
            break

        else:
            print("Zadal jsi špatnou hodnotu. Zadej ji znovu")

run()