import os
from datetime import datetime

from entities.crosswords import Crossword
from entities.user import User
from entities.repositories import UserRepository, CrosswordRepository
from functions.menu import login
from functions.after_login import stats, play_options, play_environment, projects
from functions.using_crosswords import create_crossword, play_crossword

def run_menu():
    dirname = os.path.dirname(__file__)

    users = UserRepository(os.path.join(dirname, "data", "users.csv"))
    crosswords = CrosswordRepository(os.path.join(dirname, "data", "crosswords"))

    while True:
        result = login()
        if type(result) == bool:
            continue
        else:
            user = result

    if login:
        while True:
            print("-------------------------------------------------------------")
            print("1: Pelaa")
            print("2: Luo sanaristikko")
            print("3: Muokkaa keskeneräistä sanaristikkoa")
            print("4: Tilastot")
            print("5: Kirjaudu ulos")
            choice = input("Valitse 1-5: ")
            
            if choice == "1":
                options = play_options()
                if len(options) == 0:
                    print("Ei pelattavia ristikoita.")
                    continue
                else:
                    pick = input("Kirjoita haluamasi ristikon nimi: ")
                    if pick in options:
                        play_environment(pick, user)
                    else:
                        print(f"Ei ristikkoa nimeltä {pick}")
                        continue

            elif choice == "2":
                name = input("Anna sanaristikollesi nimi: ")
                crossword = Crossword(name, user.return_name())
                create_crossword(crossword)
                pick = input("1: Julkaise, 2: Tallenna, 3: Hylkää ")
                if pick == "1":
                    crosswords.publish(crossword)
                elif pick == "2":
                    crosswords.save(crossword)

            elif choice == "3":
                works = projects(user)
                if len(works) == 0:
                    print("Sinulla ei ole keskeneräisiä töitä.")
                    continue
                else:
                    pick = input("Kirjoita haluamasi ristikon nimi: ")
                    if pick in works:
                        crossword = crosswords.load(pick + ".txt")
                        create_crossword(crossword)
                        pick = input("1: Julkaise, 2: Tallenna, 3: Hylkää")
                        if pick == "1":
                            crosswords.publish(crossword)
                        elif pick == "2":
                            crosswords.save(crossword)
                    else:
                        print("Sinulla ei ole tämän nimistä projektia")
                        continue

            elif choice == "4":
                if not stats():
                    print("Ei tilastoja")

            elif choice == "5":
                user = None
                print("Sinut on kirjattu ulos. Nähdään taas!")
                break

if __name__ == "__main__":
    run_menu()
