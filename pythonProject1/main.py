#codeium

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

def search_item(db):
    name = input("Zadej jméno knížky, kterou chceš vyhledat: ")
    #to do vylepšit podle hledání knížky nebo autora

    for i in range(len(db)):
        if db[i]["name"] == name:
            return

    return None

def add_item(db):
    name = input("Zadej jméno knížky: ")
    author = input("Zadej jméno autora: ")

    db.append({"name": name, "author": author})

def print_items(db):
    print("Aktuální seznam knížek")
    for item in db:
        print(f"Jméno: {item['name']}, autor: {item['author']}")
    print("----------------------------")
    print()


def delete_item():
    name = input("Zadej nazev knihy, kterou chceš smazat: ")

    for i in range(len(db)):
        if db[i]["name"] == name:
            del db[i]
            return True
    return False

def replace_item():
    name = input("Zadej název knihy, kterou chceš updatnout: ")
    # Vylepšení o různé update, name, autor, .....
    update_index = None
    for i in range(len(db)):
        if db[i]["name"] == name:
            update_index = i

    if update_index is None:
        print("kniha se nenašla")
        return False

    autor = input("Zadej jméno autora: ")
    db[update_index]["autor"] = autor

def get_input():
    return int(input("Zadej hodnotu výběru: "))


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
            print_items(db)

        elif user_choice == 2:
            search_item(db)

        elif user_choice == 3:
            add_item(db)

        elif user_choice == 4:
            delete_item(db)

        elif user_choice == 5:
            pass

        elif user_choice == 6:
            break

        else:
            print("Zadal jsi špatnou hodnotu. Zadej ji znovu")

run()
print("Děkuji")